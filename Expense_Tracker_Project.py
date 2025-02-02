# Expense Tracker and Financial Health Checker

def get_numeric_input(prompt):
    """Helper function to get valid numerical input from the user."""
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a positive number.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

# 1. User Profile Setup
name = input("Enter your name: ").strip().lower().title()  # Formatting name properly
profession = input("Enter your profession: ").strip()

print(f"\nWelcome, {name}! Let's analyze your financial health as a {profession}.\n")

# 2. Income and Expense Management
monthly_income = get_numeric_input("Enter your Monthly Income: ")
monthly_expenses = get_numeric_input("Enter your Monthly Expenses: ")

savings = monthly_income - monthly_expenses
savings_percentage = (savings / monthly_income) * 100

print(f"\nTotal Savings: {savings}")
print(f"Savings Percentage: {savings_percentage:.2f}%")

# 3. Financial Health Check
if savings_percentage >= 20:
    print(f"Great job, {name}! You have a strong savings habit.\n")
elif 10 <= savings_percentage < 20:
    print(f"Good, {name}, but you could save a bit more.\n")
else:
    print(f"Warning, {name}: Your savings are too low. Consider cutting expenses!\n")

# 4. Categorize Expenses
essentials = get_numeric_input("How much do you spend on Essentials? ")
wants = get_numeric_input("How much do you spend on Wants? ")
investments = get_numeric_input("How much do you save or invest? ")

total_allocation = essentials + wants + investments

# Initialize percentages to avoid NameError
essentials_pct = wants_pct = investments_pct = 0.0

# Ensure the total doesn't exceed income
if total_allocation > monthly_income:
    print("\nError: Your total expenses and savings exceed your income. Please re-evaluate your budget.")
else:
    essentials_pct = (essentials / monthly_income) * 100
    wants_pct = (wants / monthly_income) * 100
    investments_pct = (investments / monthly_income) * 100

    print("\nExpense Breakdown:")
    print(f"Essentials: {essentials_pct:.2f}%")
    print(f"Wants: {wants_pct:.2f}%")
    print(f"Savings/Investments: {investments_pct:.2f}%\n")

# 5. Custom Goals
savings_goal = get_numeric_input("What is your savings goal (in %)? ")

# ✅ Define `difference` before the condition to avoid NameError
difference = max(0, savings_goal - savings_percentage)

if savings_percentage >= savings_goal:
    print(f"Congratulations, {name}! You’ve achieved your savings goal.")
else:
    print(f"Keep working on your savings, {name}. You're {difference:.2f}% away from your goal.")

# 6. Export Summary (Bonus Feature)
summary = f"""
Financial Health Summary for {name}:
--------------------------------------
Profession: {profession}
Income: {monthly_income}
Expenses: {monthly_expenses}
Savings: {savings} ({savings_percentage:.2f}%)

Expense Breakdown:
Essentials: {essentials_pct:.2f}%
Wants: {wants_pct:.2f}%
Savings/Investments: {investments_pct:.2f}%

Savings Goal: {savings_goal}%
Status: {difference:.2f}% away from your goal.
"""

print("\nGenerating Financial Summary...\n")
print(summary)

# Saving to a text file
with open(f"{name}_Financial_Summary.txt", "w") as file:
    file.write(summary)

print(f"Summary saved as '{name}_Financial_Summary.txt'.")
print("\nThank you for using the Expense Tracker!")
