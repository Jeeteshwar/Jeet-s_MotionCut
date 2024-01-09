import random

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def display_question(self, question):
        print(question['question'])
        for i, option in enumerate(question['options'], start=1):
            print(f"{i}. {option}")

    def get_user_input(self):
        while True:
            try:
                choice = int(input("Enter your answer (1-4): "))
                if 1 <= choice <= 4:
                    return choice
                else:
                    print("Invalid choice. Please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def evaluate_answer(self, user_choice, correct_answer):
        if user_choice == correct_answer:
            print("Correct!\n")
            self.score += 1
        else:
            print(f"Wrong! The correct answer is {correct_answer}\n")

    def run_quiz(self):
        for question in self.questions:
            self.display_question(question)
            user_choice = self.get_user_input()
            self.evaluate_answer(user_choice, question['correct_answer'])

        print(f"Quiz completed! Your final score: {self.score}/{len(self.questions)}")


if __name__ == "__main__":
    # Define your quiz questions here
    quiz_questions = [
        {
            'question': 'What is the capital of France?',
            'options': ['Berlin', 'Madrid', 'Paris', 'Rome'],
            'correct_answer': 3
        },
        {
            'question': 'What is the largest mammal?',
            'options': ['Elephant', 'Blue Whale', 'Giraffe', 'Hippopotamus'],
            'correct_answer': 2
        },
        {
            'question': 'What is the currency of Japan?',
            'options': ['Yuan', 'Yen', 'Won', 'Ringgit'],
            'correct_answer': 2
        },
        {
            'question': 'Which planet is known as the Red Planet?',
            'options': ['Mars', 'Venus', 'Jupiter', 'Saturn'],
            'correct_answer': 1
        },
        {
            'question': 'Who wrote "Romeo and Juliet"?',
            'options': ['Charles Dickens', 'Jane Austen', 'William Shakespeare', 'Mark Twain'],
            'correct_answer': 3
        }
        # Add more questions following the same format
    ]

    # Create an instance of the Quiz class
    quiz = Quiz(quiz_questions)

    # Run the quiz
    quiz.run_quiz()
