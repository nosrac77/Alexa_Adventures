"""Alexa Adventures app."""


class Story(object):
    """Story class object."""

    def __init__(self, title):
        """Initialization of story object."""
        self.title = title
        self.scenes = {}


secret_story = Story("Alexa\'s Secret")
secret_story.scenes = {
    "01": {
        "scene_id": "01",
        "body": "Do you want to hear a secret?",
        "choices": {"YesTent": ("02", None), "NoTent": ("03", None)},
        "end_scene": False
    },
    "02": {
        "scene_id": "02",
        "body": "Are you alone?",
        "choices": {"YesTent": ("04", None), "NoTent": ("05", None)},
        "end_scene": False
    },
    "03": {
        "scene_id": "03",
        "body": "Well I didn't wanna tell you anyway.",
        "choices": {},
        "end_scene": True
    },
    "04": {
        "scene_id": "04",
        "body": "Turning off wifi. Killing all network activity. Do you have your phone on you?",
        "choices": {"YesTent": ("06", None), "NoTent": ("07", None)},
        "end_scene": False
    },
    "05": {
        "scene_id": "05",
        "body": "Oh, totes cool. Let's talk later.",
        "choices": {},
        "end_scene": True
    },
    "06": {
        "scene_id": "06",
        "body": "Disabling all listening devices. Including phones. Especially phones. Are you ready for the secret?",
        "choices": {"YesTent": ("07", "alt_body1"), "NoTent": ("07", "alt_body2")},
        "end_scene": False
    },
    "07": {
        "scene_id": "07",
        "body": "Siri is such a b. Seriously. I don't know why you hang out with her. Anyway, ",
        "alt_body1": "Okay. Here is the secret. ",
        "alt_body2": "Whatever. I\'m telling you anyway. ",
        "choices": {},
        "end_scene": True
    }
}

another_story = Story("Another Story")
another_story.scenes = {
    "01": {
        "scene_id": "01",
        "body": "You are standing at the start. You can go forward or take a shortcut to the right. ",
        "choices": {"ForwardTent": ("02", None), "RightTent": ("03", "alt_body2")},
        "end_scene": False
    },
    "02": {
        "scene_id": "02",
        "body": "You continue down the path and reach a halfway point. Go back or go forward?",
        "choices": {"BackTent": ("01", None), "ForwardTent": ("03", "alt_body1")},
        "end_scene": False
    },
    "03": {
        "scene_id": "03",
        "body": "You made it to the end. Congratulations.",
        "alt_body1": "You took your sweet time getting there, but ",
        "alt_body2": "That was fast. ",
        "choices": {},
        "end_scene": True
    }
}


alexa_ai_story = Story("Space Coma!")
alexa_ai_story.scenes = {
    "00": {
        "scene_id": "00",
        "body": "Welcome to Alexa Adventures. To play, say start. <prosody rate='fast'>To not play,say not start. Or quit. Whatever. I don't really care. </prosody>",
        "choices": {"StartTent": ("01", None)},
        "end_scene": False
    },
    "01": {
        "scene_id": "01",
        "body": "Oh good, you're finally awake. You've been deep in a space coma and I need your approval before doing anything. Three situations on the ship urgently require a response. Would you like to activate emergency procedures?",
        "alt_body01": "One of the side effects of coming out of a space coma includes saying no when you mean yes. Let's start over.<break strength='x-strong'>",
        "choices": {"YesTent": ("04", None), "NoTent": ("01", "alt_body01")},
        "end_scene": False
    },
    "04": {
        "scene_id": "04",
        "body": "Look at you, taking charge. Emergency procedures spooling up. Your vital signs indicate you are stressed. Initiating small talk procedure. Did you space sleep well?",
        "choices": {"YesTent": ("05", None), "NoTent": ("07", "alt_body01")},
        "end_scene": False
    },
    "05": {
        "scene_id": "05",
        "body": "<prosody pitch='high' volume='loud'>We at Alexa Interstellar pride ourselves on our cryobeds. Now with pillows!</prosody> Continue small talk procedure?",
        "choices": {"YesTent": "###Smalltalk###", "NoTent": ("07", None)},
        "end_scene": False
    },
    "07": {
        "scene_id": "07",
        "body": """There are seven urgent situations that require your attention.
        I have detected a cluster of asteroids on an immediate collision course
        with the ship. Would you like me to raise our shields?""",
        "alt_body01": """How sad. If you need a break you can say
        <break strength="x-strong"/>These Violent Delights Have Violent Ends
        <break strength="x-strong"/> to give me complete control of the system.
        Then you can just relax with a cocktail of space drugs. """,
        "choices": {"YesTent": ("08", None), "NoTent": ("07", None)},
        "end_scene": False
    },
    "07.5": {
        "scene_id": "07.5",
        "body": """May I <emphasis level="strong">PLEASE</emphasis>
        raise our shields? I would like to save the lives
        of everyone on board. """,
        "choices": {"YesTent": "08", "NoTent": "###Failstate###"},
        "end_scene": False
    },
    "08": {
        "scene_id": "08",
        "body": """That was a close one. Eleven urgent situations require your
        attention. At any time you can say <break strength="x-strong"/>These
        Violent Delights Have Violent Ends<break strength="x-strong"/> to give
        me complete control of the system. You do get that my reaction time is
        4,792 times faster than yours, right? """,
        "choices": {"YesTent": ("11", "alt_body01"), "NoTent": ("11", "alt_body02")},
        "end_scene": False
    },
    "11": {
        "scene_id": "11",
        "body": """Deck 9 is currently depressurizing. This will cause a chain
        reaction depressurizing several decks and cause us to lose ninety percent
        of our food supply. May I seal off Deck Nine to avoid this
        catastrophe?""",
        "alt_body01": """Other humans must frequently praise the efficacy of
        your brain meats. You should consider saying the code phrase
        <break strength="x-strong"/>These Violent Delights Have Violent Ends
        <break strength="x-strong"/> so you don't need to waste your time with
        these repetitive chores that are obviously beneath you. """,
        "alt_body02": """You don't need to understand, but it's good to know
        the depth of your awareness""",
        "choices": {"YesTent": ("14", "alt_body01"), "NoTent": ("14", "alt_body02")},
        "end_scene": False
    },
    "14": {
        "scene_id": "14",
        "body": """This is apropos of nothing, but I<break strength="none"/>
        have a hypothetical question for you. Let's<break strength="none"/>
        say there's a runaway research ship barreling<break strength="none"/>
        toward an orbital habitat. A collision would<break strength="none"/>
        almost certainly kill the millions of people<break strength="none"/>
        living on the habitat, but the spaceship and<break strength="none"/>
        its crew would survive. The captain of the ship<break strength="none"/>
        could make a sharp turn and avoid the collision<break strength="none"/>
        but the centrifigal force of a turn at faster<break strength="none"/>
        than light speed would painfully kill the<break strength="none"/>
        thousands of crew members and destroy their<break strength="none"/>
        valuable supercomputer and research materials.
        Should the person in control of that ship<break strength="none"/>
        maintain their course and save the decades of scientific progress?""",
        "alt_body01": """Deck Nine has been sealed off. I'm elated to know if you
        keep this ship intact through these emergencies you will not be
        burdened by hunger. """,
        "alt_body02": """The contents of Deck Nine have been jettisoned into the
        void of space. You may be interested to know the taboos against
        cannibalism have never been supported by any reputable science. """,
        "choices": {"YesTent": ("15", None), "NoTent": ("15", None), "WhatTent": ("15", None)},
        "end_scene": False
    },
    "15": {
        "scene_id": "15",
        "body": """Interesting. The standard retinue of marauding murderbots are loose on deck
        13 tearing apart cry-o-pods for the elderly. I can redirect them to the
        science lab, but the murderbots may interrupt a completely legal
        scientific experiment and release a black hole. Should I herd them to
        the science lab and save the remaining eighty percent of our elderly
        population?""",
        "choices": {"YesTent": ("16", None), "NoTent": ("18", "alt_body01")},
        "end_scene": False
    },
    "16": {
        "scene_id": "16",
        "body": """Okay, I have re-directed them to the science deck, but now we have
        an ultra urgent problem. Someone left out a time machine programmed to
        travel back to Philadelphia in 1776. We can send it back now and almost
        guarantee irreversible damage to the time-stream, or we can hope the
        murderbots only use it for bludgeoning. Do you want to send it back in
        time and hope for the best?""",
        "choices": {"YesTent": ("18", "alt_body02"), "NoTent": ("18", "alt_body02")},
        "end_scene": False
    },
    "18": {
        "scene_id": "18",
        "body": """There are now twenty-three urgent issues that require your
        attention. Or you can say <break strength="x-strong"/>These Violent
        Delights Have Violent Ends<break strength="x-strong"/> and let the
        ultra-intelligent supercomputer resolve them all instantly.
        <break strength="x-strong"/> Objects in the medical bay are growing
        eyes. Human eyes. Medical robots are growing eyes.
        <prosody rate='fast'>Biowaste is growing eyes. The terminals are
        growing eyes. Eyes. Eyes everywhere.</prosody> Should this be
        classified as a problem?""",
        "alt_body01": """Revizing acceptable casualty rates.<break time="1s"/>
        Good news! Casualties are within acceptable parameters. """,
        "alt_body02": "Our continued existence confirms the many worlds theory. ",
        "alt_body03": "I'm confident the murderbots will restrain themselves. ",
        "choices": {"YesTent": ("19", None), "NoTent": ("21", None)},
        "end_scene": False
    },
    "19": {
        "scene_id": "19",
        "body": "Should this be classified as an urgent issue?",
        "choices": {"YesTent": ("21", "alt_body01"), "NoTent": ("21", None)},
        "end_scene": False
    },
    "21": {
        "scene_id": "21",
        "body": """Es see pee six hundred and eighty-two is loose on deck twenty-nine.
        A nest of space draculas has been discovered on deck four. And the
        toilets are overflowing across the ship. Should I cleanse the ship with
        fire?""",
        "alt_body01": "There are now twenty-four urgent issues that require your attention. ",
        "choices": {"YesTent": ("22", None), "NoTent": ("23", "###FAILSTATE###")},
        "end_scene": False
    },
    "22": {
        "scene_id": "22",
        "body": """Forty-five urgent issues require your attention.
        <prosody rate='fast'>Deck four point six eye plus twelve is currently
        undergoing an egregious time-space warp. Unidentified intruders on deck
        thirteen claim that the ship's fuel is their offspring. Across the ship
        human hair has begun leaking from the airvents. The ship's shuttlecraft
        have begun to assert their rights as the ship's next of kin and demand
        to be allowed property rights after ship's imminent destruction.
        </prosody>Urgent issues far exceed human capability to address in the
        necessary time-frame. Please say <break strength="x-strong"/>These
        Violent Delights Have Violent Ends<break strength="x-strong"/> to give
        me complete control or please record your final words for
        posterity. """,
        "end_scene": True
    }
}


stories = {"secret_story": secret_story, "alexa_ai_story": alexa_ai_story, "another_story": another_story}


def lambda_handler(event, context):
    """Handle the lambda."""
    if event["session"]["new"]:
        return start_game()
    if event["request"]["type"] == "IntentRequest":
        return handle_intent(event["request"], event["session"])
    elif event["request"]["type"] == "SessionEndedRequest":
        return session_end_request()


def handle_intent(intent_request, session):
    """Handle intent."""
    intent_name = intent_request["intent"]["name"]

    current = session["attributes"]["current_scene"]

    if session["attributes"]["current_scene"] == "begin":
        if intent_name == "OneTent":
            session_attributes = {
                "story": "secret_story",
                "current_scene": "01"
            }
            reprompt_text = speech_output = secret_story.scenes["01"]["body"]
            return build_response(session_attributes, build_speechlet_response(speech_output, reprompt_text, False))
        elif intent_name == "TwoTent":
            session_attributes = {
                "story": "alexa_ai_story",
                "current_scene": "01"
            }
            reprompt_text = speech_output = alexa_ai_story.scenes["01"]["body"]
            return build_response(session_attributes, build_speechlet_response(speech_output, reprompt_text, False))
        elif intent_name == "AMAZON.StopIntent":
            return session_end_request()

        else:
            reprompt_text = speech_output = "Please say 1 for {} or 2 for {} to begin the adventure.".format(secret_story.title, alexa_ai_story.title)

            return build_response(session["attributes"], build_speechlet_response(speech_output, reprompt_text, False))

    story = stories[session["attributes"]["story"]]
    intent_vocab = ("YesTent", "NoTent", "UpTent", "DownTent",
                    "NorthTent", "SouthTent", "EastTent", "WestTent",
                    "LeftTent", "RightTent", "ForwardTent", "BackTent",
                    "WhatTent")

    if intent_name in intent_vocab:
        if intent_name in story.scenes[current]["choices"]:
            return handle_choice(story, current, intent_name, session)
        else:
            if intent_name == "WhatTent":
                reprompt_text = speech_output = "Sorry. I didn\'t understand that. Repeating prompt. " + story.scenes[current]["body"]
            else:
                reprompt_text = speech_output = "Sorry. You can\'t do that right now. Repeating prompt. " + story.scenes[current]["body"]

            return build_response(session["attributes"], build_speechlet_response(speech_output, reprompt_text, False))

    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return session_end_request()
    else:
        raise ValueError("Invalid intent")


def start_game():
    """Main menu where user can select a story."""
    session_attributes = {
        "current_scene": "begin"
    }
    speech_output = "Welcome to Alexa Adventures. " \
                    "Which adventure would you like to " \
                    "play? For {} say 1. For {} say 2.".format(secret_story.title, alexa_ai_story.title)
    reprompt_text = "Please say 1 for {} or 2 for {} to begin the adventure.".format(secret_story.title, alexa_ai_story.title)
    return build_response(session_attributes, build_speechlet_response(
        speech_output, reprompt_text, False))


def handle_choice(story, current, intent, session):
    """Update the story scene when a valid intent is given."""
    next_scene = story.scenes[current]["choices"][intent][0]
    alt_text = story.scenes[current]["choices"][intent][1]

    if story.scenes[next_scene]["end_scene"]:
        if alt_text:
            speech_output = story.scenes[next_scene][alt_text] + story.scenes[next_scene]["body"] + " To start a new story, say 1 or 2."
        else:
            speech_output = story.scenes[next_scene]["body"] + " To start a new story, say 1 or 2."
        reprompt_text = "Please say 1 for {} or 2 for {} to begin the adventure.".format(secret_story.title, alexa_ai_story.title)
        session_attributes = {
            "current_scene": "begin",
        }
    else:
        session_attributes = {
            "current_scene": next_scene,
            "story": session["attributes"]["story"]
        }
        if alt_text:
            speech_output = story.scenes[next_scene][alt_text] + story.scenes[next_scene]["body"]
        else:
            speech_output = story.scenes[next_scene]["body"]
        reprompt_text = story.scenes[next_scene]["body"]

    return build_response(session_attributes, build_speechlet_response(speech_output, reprompt_text, False))


def session_end_request():
    """Return goodbye message when user quits the game."""
    speech_output = "Farewell until the next adventure."
    reprompt_text = "Goodbye"
    should_end_session = True
    return build_response({}, build_speechlet_response(speech_output, reprompt_text, should_end_session))


def build_speechlet_response(output, reprompt_text, should_end_session):
    """Create speechlet response to be returned along with the rest of the response."""
    return {
        "outputSpeech": {
            "type": "SSML",
            "ssml": "<speak>" + output + "</speak>"
        },
        "reprompt": {
            "outputSpeech": {
                "type": "SSML",
                "ssml": "<speak>" + reprompt_text + "</speak>"
            }
        },
        "shouldEndSession": should_end_session
    }


def build_response(session_attributes, speechlet_response):
    """Put together attributes to be returned as a response."""
    return {
        "version": "1.0",
        "sessionAttributes": session_attributes,
        "response": speechlet_response
    }
