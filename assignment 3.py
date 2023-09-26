try:
    hours = input("Enter the number of hours worked: ")
    rate = input("Enter the hourly rate: ")

    hours = int(hours)
    rate = float(rate)

    if hours > 40:
        salary = 40 * rate + (hours - 40) * 1.5 * rate
    else:
        salary = hours * rate

    print(f"Salary: ${salary:.2f}")

except ValueError as e:
    print("Error:", e)
except Exception as e:
    print("Error:", e)
