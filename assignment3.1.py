try:
    score = float(input("Enter the score (0-100): "))

    if 0 <= score <= 100:
        if score >= 90:
            grade = 'A'
        elif score >= 80:
            grade = 'B'
        elif score >= 70:
            grade = 'C'
        elif score >= 60:
            grade = 'D'
        else:
            grade = 'F'

        print(f"Grade: {grade}")

    else:
        print("Error: The entered score is out of the valid range (0-100).")

except ValueError as E:
    print("Error:", E)
except Exception as E:
    print("Error:", E)
