import requests

texts = [
    'They are to carry the tabernacle and all its furnishings; they are to take care of it and encamp around it.',
    'The Congress shall have Power To lay and collect Taxes, Duties, Imposts and Excises, to pay the Debts and provide for the common Defence and general Welfare of the United States; but all Duties, Imposts and Excises shall be uniform throughout the United States;',
    'Oh, maternal ditch, half full of muddy water! A factory gutter! As I raised my body, mud-spattered and smelly, I felt the red hot poker of joy deliciously pierce my heart. A crowd of fishermen and gouty naturalists crowded terrified around this marvel. '
]

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

print(generate(texts[2]))