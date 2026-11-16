from dataclasses import dataclass
import random
from time import time  
@dataclass
class Challenge:
    title: str
    description: str
    type: str
    restrictions: str   # Optional restrictions for the challenge
#where challenges will be stored
#instrumental_challenges = [Challenge("Tubarific", "Write a Sip for Tuba", "instrumental"), Challenge("Sax Attack", "Write a Sip for Saxophone", "instrumental")]
emotional_challenges = [Challenge("Sound of Jealousy", "Write a Sip that sounds jealous", "emotional", "none"), Challenge("Music of Love", "Write a Sip that sounds like its in love", "emotional", "none")]
rhythmic_challenges = [Challenge("Not Half Bad", "Write a Sip using only half notes", "rhythmic", "half notes only"), Challenge("Quartermaster", "Write a Sip using only quarter notes", "rhythmic", "quarter notes only")]
#all_challenges = []

current_emotional_challenge = random.choice(emotional_challenges)
current_rhythmic_challenge = random.choice(rhythmic_challenges)
def get_daily_challenge(emotions: list[Challenge], rhythms: list[Challenge], type: str) -> Challenge:
    '''
    gets a daily challenge from the list of the specificied challenge type
        instruments(list[Challenge]): list of potential instrument challenges
        emotions(list[Challenge]): list of potential emotional challenges
        rhymths(list[Challenge]): list of potential rhythmic challenges
        type(str): the actual selected challenge type
    '''
    challenge = "none"
    if type == "emotional":
        challenge = random.choice(emotional_challenges)
    elif type == "rhythmic":
       challenge = random.choice(rhythmic_challenges)
    return challenge
#get_daily_challenge is random, so it can't really be unit tested
get_daily_challenge(emotional_challenges, rhythmic_challenges, "emotional")  # Call the function to initialize the challenges