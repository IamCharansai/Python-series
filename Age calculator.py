from datetime import datetime

def calculate_age(birthdate_str):
    try:
        birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
        today = datetime.today()
        age_days = (today - birthdate).days
        years = age_days // 365
        months = (age_days % 365) // 30
        days = (age_days % 365) % 30

        print(f"\n You are {years} years, {months} months, and {days} days old.")
    except ValueError:
        print(" Please enter the date in YYYY-MM-DD format.")

print(" Age Calculator")
birth_input = input("Enter your birthdate (YYYY-MM-DD): ")
calculate_age(birth_input)
