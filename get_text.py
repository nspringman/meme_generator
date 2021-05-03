import requests

def generate(text):
    generatedText = requests.post(
        "https://api.deepai.org/api/text-generator",
        data={
            'text': text,
        },
        headers={'api-key': 'cba42b1d-0cf8-40f1-b37f-6615ac018163'}
    )
    generatedText = generatedText.json()['output'] + '.'
    return generatedText