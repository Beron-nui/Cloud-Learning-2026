def run_budget_tracker():
    # 1. Setup initial data
    try:
        balance = float(input("Enter your starting monthly balance: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    expenses = {
        "Rent": 1200.00,
        "Groceries": 350.00,
        "Utilities": 150.00,
        "Entertainment": 100.00
    }

    print("\n--- Current Expenses ---")
    for item, cost in expenses.items():
        print(f"{item}: ${cost}")

    # --- YOUR TASK STARTS HERE ---
    
    # STEP A: Calculate the total sum of all expenses in the 'expenses' dictionary.
    # Hint: You can iterate through expenses.values()
    total_spent = 0 
    # [Add your logic here to sum the values]
    for cost in expenses.values():
        total_spent = total_spent + cost
    # STEP B: Calculate the remaining balance.
    remaining = 0 
    # [Add your logic here]
    remaining = balance - total_spent 
    # --- YOUR TASK ENDS HERE ---

    print("\n--- Financial Summary ---")
    print(f"Total Spent: ${total_spent}")
    print(f"Remaining: ${remaining}")

    # STEP C: Write a simple IF/ELSE statement below:
    # If remaining is less than 0, print "Warning: You are in debt!"
    # Otherwise, print "Great job! You are within budget."
    
    # [Add your if/else logic here]
    if remaining < 0:
        print(f"Warning!: You are in debt! ${remaining}")
    else:
        print(f"Great job! your whithin budget")

run_budget_tracker()