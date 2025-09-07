import random
import time

# Function to generate a random math question
def generate_question(level):
    if level == "easy":
        num_range = (1, 10)
    elif level == "medium":
        num_range = (1, 20)
    else:  # hard
        num_range = (1, 50)

    num1 = random.randint(*num_range)
    num2 = random.randint(*num_range)
    operator = random.choice(["+", "-", "*"])

    # Ensure subtraction never gives negative results
    if operator == "-" and num2 > num1:
        num1, num2 = num2, num1

    question = f"{num1} {operator} {num2}"
    answer = eval(question)
    return question, answer

# Function to ask a single question
def ask_question(question, answer):
    print(f"\nWhat is {question}?")
    start = time.time()
    try:
        user_answer = int(input("Your answer: "))
    except ValueError:
        print("Invalid input! Marked as incorrect.")
        return 0, None, int(time.time() - start)

    end = time.time()
    time_taken = end - start

    if user_answer == answer:
        if time_taken <= 5:
            points = 2
        else:
            points = 1
        print(f"Correct! (+{points} points, answered in {time_taken:.2f}s)")
    else:
        points = 0
        print(f"Incorrect! The correct answer was {answer}.")
    return points, user_answer, int(time_taken)

# Main game loop
def maths_test():
    print("=== Welcome to the Maths Test ===")
    print("Choose difficulty:")
    print("1) Easy\n2) Medium\n3) Hard")

    while True:
        choice = input("> ")
        if choice == "1":
            difficulty = "easy"
            total_questions = 5
            break
        elif choice == "2":
            difficulty = "medium"
            total_questions = 10
            break
        elif choice == "3":
            difficulty = "hard"
            total_questions = 15
            break
        else:
            print("Invalid input, please enter 1, 2, or 3.")

    print(f"\nYou selected {difficulty.capitalize()} mode! Let's begin...")

    total_score = 0
    results = []

    for q in range(1, total_questions + 1):
        question, answer = generate_question(difficulty)
        print(f"\nQuestion {q}/{total_questions}")
        points, user_answer, time_taken = ask_question(question, answer)
        total_score += points
        results.append((question, answer, user_answer, points, time_taken))

    # Results summary
    print("\n=== Test Completed! ===")
    print(f"Final Score: {total_score}/{total_questions * 2}")
    percentage = round((total_score / (total_questions * 2)) * 100, 2)
    print(f"Percentage: {percentage}%")

    print("\n--- Question Breakdown ---")
    print("Q#   Question   Your Ans   Correct Ans   Points   Time(s)")
    print("----------------------------------------------------------")
    for i, (q, ans, user, pts, t) in enumerate(results, 1):
        print(f"{i:<4} {q:<9} {str(user):<9} {ans:<12} {pts:<7} {t}")

# Correct main guard
if __name__ == "__main__":
    maths_test()
