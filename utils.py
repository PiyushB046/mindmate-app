import json
import os

# Load trivia questions
def load_questions():
    try:
        with open(os.path.join("data", "trivia_questions.json"), "r") as f:
            return json.load(f)
    except:
        return []

# Load This or That game questions
def load_this_or_that_questions():
    try:
        with open(os.path.join("data", "this_or_that.json"), "r") as f:
            return json.load(f)
    except:
        return []
