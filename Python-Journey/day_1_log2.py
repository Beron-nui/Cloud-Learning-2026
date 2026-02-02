def run_expense_auditor():
    expenses = {
        "Rent": 1200.00,
        "Groceries": 350.00,
        "Utilities": 150.00,
    }

    # 1. Let the user add one more expense
    new_name = input("Enter a new expense name: ")
    try:
        new_price = float(input(f"How much was the {new_name}? "))
        expenses[new_name] = new_price # This adds it to the dictionary
    except ValueError:
        print("Invalid price, skipping add.")

    print("\n--- Auditing Your Expenses ---")

    # --- YOUR TASK STARTS HERE ---

    # STEP A: Loop through the 'expenses' dictionary using .items()
    # STEP B: Inside the loop, check IF the price is greater than 200.
    # STEP C: If it is, print: "[NAME] is expensive! ($[PRICE])"
    # STEP D: Otherwise, print: "[NAME] is within a reasonable range."

    # [Write your loop and if/else logic here]
    for item, cost in expenses.items():
        print(f"{item}: ${cost}")

        if cost >= 200:
            print(f"{[item]} is expensive!")
        else:
            print(f"{[item]} is within reasonanble renage")         
    # --- YOUR TASK ENDS HERE ---

run_expense_auditor()