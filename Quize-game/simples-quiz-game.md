"""
Simple Quiz Game
---------------------------------
This program asks the user a series of multiple-choice questions.
It keeps track of the score and displays the final result at the end.

Concepts used:
- Lists and dictionaries
- Loops
- Conditional logic
- Basic input/output handling
"""

def run_quiz(questions):
    """
    Runs the quiz loop and calculates the user's score.
    
    Parameters:
        questions (list): A list of question dictionaries, each containing:
                          'question', 'options', and 'answer' keys.
    """
    score = 0  # To keep track of correct answers

    print("🧠 Welcome to the Python Quiz Game!")
    print("Try to answer all questions correctly.\n")

    # Loop through each question in the list
    for index, q in enumerate(questions, start=1):
        print(f"Q{index}: {q['question']}")

        # Display all options neatly
        for option in q['options']:
            print(option)

        # Get user's answer
        user_answer = input("Your answer (A/B/C/D): ").strip().upper()

        # Check if the answer is correct
        if user_answer == q['answer']:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was {q['answer']}.\n")

    # After all questions, show the score
    print("📊 Quiz Completed!")
    print(f"Your final score: {score}/{len(questions)}")

    # Optional encouragement based on performance
    if score == len(questions):
        print("🏆 Excellent! You nailed it!")
    elif score >= len(questions) // 2:
        print("👍 Good job! Keep practicing.")
    else:
        print("💪 Don’t worry, you’ll get better next time!")


def main():
    """Main entry point — defines the questions and starts the quiz."""

    # List of question dictionaries
    questions = [
        {
            "question": "What is the output of print(2 ** 3)?",
            "options": ["A) 6", "B) 8", "C) 9", "D) 12"],
            "answer": "B"
        },
        {
            "question": "Which keyword is used to define a function in Python?",
            "options": ["A) func", "B) define", "C) def", "D) function"],
            "answer": "C"
        },
        {
            "question": "What data type is used to store True or False?",
            "options": ["A) int", "B) bool", "C) str", "D) float"],
            "answer": "B"
        },
        {
            "question": "Which of these is a valid variable name?",
            "options": ["A) 1name", "B) first-name", "C) first_name", "D) first name"],
            "answer": "C"
        },
    ]

    # Start the quiz
    run_quiz(questions)


# Run the main function only when executed directly
if __name__ == "__main__":
    main()
