import sys

cumulative_credits = 0
cumulative_grade_points = 0

print("Welcome to the Cumulative GPA Calculator!")
user_input = input("Type 'start' to begin or 'exit' to quit: ").lower()

while user_input != "exit":
    term_credits = 0
    term_grade_points = 0
    term_gpa = 0

    print("\nStarting a new term...")
    while True:
        grade = input("Enter your grade (or type 'end' to finish the term): ").lower()
        if grade == "end":
            break

        grade_number = 0
        if grade == "a":
            grade_number = 4.0
        elif grade == "a-":
            grade_number = 3.7
        elif grade == "b+":
            grade_number = 3.3
        elif grade == "b":
            grade_number = 3.0
        elif grade == "b-":
            grade_number = 2.7
        elif grade == "c+":
            grade_number = 2.3
        elif grade == "c":
            grade_number = 2.0
        elif grade == "c-":
            grade_number = 1.7
        elif grade == "d+":
            grade_number = 1.3
        elif grade == "d":
            grade_number = 1.0
        elif grade == "d-":
            grade_number = 0.7
        elif grade == "f":
            grade_number = 0.0
        else:
            print("Invalid grade entered. Please try again.")
            continue

        try:
            credit = int(input("Enter the credit hours for this class: "))
            grade_points = credit * grade_number

            term_credits += credit
            term_grade_points += grade_points
        except ValueError:
            print("Invalid credit hours. Please enter a number.")

    if term_credits > 0:
        term_gpa = term_grade_points / term_credits
        print(f"Your term GPA is {term_gpa:.2f}")

        cumulative_credits += term_credits
        cumulative_grade_points += term_grade_points

        cumulative_gpa = cumulative_grade_points / cumulative_credits
        print(f"Your cumulative GPA is {cumulative_gpa:.2f}")
    else:
        print("No valid grades or credits entered for this term.")

    user_input = input("\nWould you like to start another term? (yes/no): ").lower()
    if user_input == "no":
        print("Thank you for using the Cumulative GPA Calculator! Goodbye!")
        break
