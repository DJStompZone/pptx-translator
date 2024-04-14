const fs = require('fs');
const axios = require('axios');

const { cloudflarekey, cloudflareid, cloudflaregatewayname, inputlang, outputlang } = require('../config.json');

async function translateText(element, sourceLang, targetLang, retries = 3) {
    try {
        const response = await axios.post(`https://gateway.ai.cloudflare.com/v1/${cloudflareid}/${cloudflaregatewayname}/workers-ai/@cf/meta/m2m100-1.2b`, {
            text: element[1],
            source_lang: sourceLang,
            target_lang: targetLang
        }, {
            headers: {
                Authorization: `Bearer ${cloudflarekey}`
            }
        });
        return {
            "original": element,
            "translated": response.data.result.translated_text
        };
    } catch (error) {
        if (retries > 0) {
            console.log(`Retrying translation for element: ${element[0]}, attempts left: ${retries - 1}`);
            return await translateText(element, sourceLang, targetLang, retries - 1);
        } else {
            console.error(`Failed translation for element: ${element[0]}, error: ${error.message}`);
            return {
                "original": element,
                "translated": "Translation failed",
                "error": true
            };
        }
    }
}

async function main() {
    const data = fs.readFileSync('output.json');
    const output = JSON.parse(data);

    let translated = [];
    const batchSize = 5;

    for (let i = 0; i < output.length; i += batchSize) {
        const batch = output.slice(i, i + batchSize).map((element, index) => {
            return translateText(element, inputlang, outputlang);
        });

        const batchResults = await Promise.all(batch);
        translated.push(...batchResults);

        batchResults.forEach((item, index) => {
            if (!item.error) {
                console.log(`Translated: ${i + index + 1}/${output.length}`);
            }
        });
    }

    fs.writeFileSync('translated.json', JSON.stringify(translated, null, 2));
}

main();
