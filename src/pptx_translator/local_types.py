from dataclasses import dataclass
from enum import Enum

import json

class ExtractionMode(Enum):
    TEXT_BOXES = 'text_boxes'
    NOTES = 'notes'

@dataclass
class SlideElement:
    slide_id: int
    text: str

@dataclass
class TranslationResult:
    original: SlideElement
    translated: str
    error: bool

type TranslatedElement = dict[str, str|SlideElement|bool]

@dataclass
class Config:
    cloudflare_key: str
    cloudflare_id: str
    cloudflare_gateway_name: str
    input_lang: str
    output_lang: str
    input_file: str
    output_file: str

    @staticmethod
    def load_from_file(file_path: str, input_file: str, output_file: str) -> 'Config':
        """
        Load configuration from a specified JSON file and include file paths for input and output.

        Args:
            file_path (str): The path to the JSON configuration file.
            input_file (str): Input JSON file path.
            output_file (str): Output JSON file path.

        Returns:
            Config: An instance of Config initialized with data from the file.
        """
        with open(file_path, 'r') as config_file:
            data = json.load(config_file)
        return Config(
            cloudflare_key=data['cloudflarekey'],
            cloudflare_id=data['cloudflareid'],
            cloudflare_gateway_name=data['cloudflaregatewayname'],
            input_lang=data['inputlang'],
            output_lang=data['outputlang'],
            input_file=input_file,
            output_file=output_file
        )