#Write a program that asks the user to input their salary and then calculates their tax based on the following conditions: if salary is less than or equal to 5000, tax is 10%; if salary is between 5001 and 10000, tax is 20%; otherwise, tax is 30% using if, elif, and else.
def calculate_tax():
    salary = float(input("Enter your salary: "))
    if salary <= 5000:
        tax = salary * 0.10 
    elif salary <= 10000:
        tax = salary * 0.20
    else:
        tax = salary * 0.30 
    print(f"Your tax based on a salary of {salary:.2f} is {tax:.2f}")
calculate_tax()
