"""This file contains the implementation of the Question class."""

class Question:

    def __init__(self, data):
        self.category = data["category"]
        self.type = data["type"]
        self.difficulty = data['difficulty']
        self.question = data["question"]
        self.correct_answer = data["correct_answer"]
        self.incorrect_answers = data["incorrect_answers"]

    def __repr__(self) -> str:
        return f"Question: {self.question}"

    def submit_answer(self, answer: str) -> bool:
        if answer.lower() == self.correct_answer.lower():
            return True
        else:
            return False
