import asyncio
import json
import logging
import sys
import traceback as tb

import httpx
from local_types import (Config, SlideElement, TranslatedElement,
                         TranslationResult)


def format_exception(exc: BaseException) -> str:
    """
    Format an exception as a string.

    Args:
        exc (BaseException): The exception to format.

    Returns:
        str: The formatted exception.
    """
    return "".join(tb.format_exception_only(type(exc), exc)).strip()



async def translate_text(config: Config, element: SlideElement, retries: int = 3) -> TranslationResult:
    """
    Asynchronously translates text using the Cloudflare API with retry logic.

    Args:
        config (Config): Configuration instance containing API keys and settings.
        element (SlideElement): Tuple containing the element ID and text to translate.
        retries (int): Number of retries for the API call.

    Returns:
        dict: A dictionary with original and translated texts, and error flag if applicable.
    """
    url = "https://api.cloudflare.com/client/v4/zones/{config.cloudflare_zone}/dns_records"
    headers = {'Authorization': f'Bearer {config.cloudflare_key}'}
    payload = {
        "text": element.text,
        "source_lang": config.input_lang,
        "target_lang": config.output_lang
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(url, json=payload, headers=headers)
            response.raise_for_status()
            return TranslationResult(
                original = element,
                translated = str(response.json()['result']['translated_text']),
                error=  False
            )
        except httpx.HTTPStatusError as e:
            logging.error(f"HTTP error occurred: {e.response.status_code} - {format_exception(e)}")
        except httpx.RequestError as e:
            logging.error(f"Request failed: {e}")
        if retries > 0:
            logging.info(f"Retrying translation for element: {element.slide_id}, attempts left: {retries - 1}")
            return await translate_text(config, element, retries - 1)
        else:
            logging.error(f"Failed to translate element: {element.slide_id}, no retries left.")
            return TranslationResult(
                original = element,
                translated = "Translation failed",
                error = True
            )

async def translate_async(input_file: str, output_file: str):
    """
    Main function to load text elements from a file, translate them, and save the results.
    """
    logging.basicConfig(level=logging.INFO)
    config: Config = Config.load_from_file('../config.json', input_file, output_file)

    with open(config.input_file, 'r', encoding='utf-8') as file:
        outputs = json.load(file)

    translated: list[TranslatedElement] = []
    batch_size = 5

    for i in range(0, len(outputs), batch_size):
        batch = [translate_text(config, element) for element in outputs[i:i + batch_size]]
        results = await asyncio.gather(*batch)
        translated.extend(results)

        logging.info(f"Batch {i//batch_size + 1} translated.")

    with open(config.output_file, 'w', encoding='utf-8') as file:
        json.dump(translated, file, indent=2)
        logging.info(f"Translation results saved to '{config.output_file}'.")

if __name__ == "main":
    if len(sys.argv) < 3:
        logging.error("CLI usage: python translate.py <input_file> <output_file>")
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    asyncio.run(translate_async(input_file, output_file))
