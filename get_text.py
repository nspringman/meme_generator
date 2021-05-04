import requests

texts = [
    'They are to carry the tabernacle and all its furnishings; they are to take care of it and encamp around it.',
    'The Congress shall have Power To lay and collect Taxes, Duties, Imposts and Excises, to pay the Debts and provide for the common Defence and general Welfare of the United States; but all Duties, Imposts and Excises shall be uniform throughout the United States;',
    'Oh, maternal ditch, half full of muddy water! A factory gutter! As I raised my body, mud-spattered and smelly, I felt the red hot poker of joy deliciously pierce my heart. A crowd of fishermen and gouty naturalists crowded terrified around this marvel.',
    'Washington University in St. Louis is a leader in a variety of fields through our path-breaking research and exceptional academics.',
    'Cortado Script is the retail version of a custom typeface Jesse Ragan and I worked on for MP Creative’s 2013 ‘Give me Aldo’ campaign.',
    """For it's proper for a devoted poet to be moral himself, [but] in no way is it necessary for his poems. In point of fact, these have wit and charm, if they are sensitive and a little shameless, and can arouse an itch,""",
    'All Gaul is divided into three parts, one of which the Belgae inhabit, the Aquitani another, those who in their own language are called Celts, in our Gauls, the third.',
    """According to all known laws of aviation, there is no way a bee should be able to fly. Its wings are too small to ge its fat little body off the ground. The bee, of course, flies anyway because bees don't carewhat humans think is impossible.""",
    """Former Army Ranger Jake Rivers is not your typical Kelton College student. He is not spoiled, coddled, or ultra-lib like his classmates who sneer at the “soldier boy.” Rivers is not “triggered” by “microaggressions.” He is not outraged by “male privilege” and “cisgender bathrooms.” He does not need a “safe space.”""",
    """I'll have you know I graduated top of my class in the Navy Seals, and I've been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I'm the top sniper in the entire US armed forces."""
]

def generate(feeling):
    generatedText = requests.post(
        "https://api.deepai.org/api/text-generator",
        data={
            'text': texts[feeling-1],
        },
        headers={'api-key': 'cba42b1d-0cf8-40f1-b37f-6615ac018163'}
    )
    generatedText = generatedText.json()['output'] + '.'
    return generatedText