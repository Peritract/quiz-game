"""Python file that launches the quiz game."""

import requests as req

from exceptions import APIError
from question import Question

API_URL = "https://opentdb.com/api.php"


def get_quiz_questions(num_questions: int=10) -> dict:
    """Retrieves quiz questions from the API."""

    res = req.get(f"{API_URL}?amount={num_questions}")

    if res.status_code != 200:
        raise APIError(res.text, res.status_code)

    questions = res.json()["results"]

    return questions


if __name__ == "__main__":
    try:
        data = get_quiz_questions(5)
        quiz = [Question(q) for q in data]
        print(quiz)
    except APIError as err:
        print("Unable to access the API; please try again later.")