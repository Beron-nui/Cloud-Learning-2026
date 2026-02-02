def mask_transactions():
    # A list of transaction strings: "ID_Status_Amount"
    transactions = [
        "TXN101_ACTIVE_200",
        "TXN102_HIDDEN_450",
        "TXN103_ACTIVE_700",
        "TXN104_HIDDEN_150"
    ]

    print("--- Processing Transactions ---")

    for entry in transactions:
        # STEP 1: Split the string into a list of 3 parts using the "_" as a separator
        # Hint: use entry.split("_")
        parts = [entry.split("_")] # YOUR CODE HERE

        txn_id = parts[0]
        status = parts[1]
        amount = float(parts[2])

        # --- YOUR TASK STARTS HERE ---

        # STEP A: Logic for Masking
        # If the status is "HIDDEN", change the txn_id variable to "****"
        if status == "HIDDEN":
            txn_id = "****"  # YOUR CODE HERE

        # STEP B: Logic for Flagging
        # Create a variable 'flag' that is " [HIGH VALUE]" if amount > 500, 
        # otherwise it should be an empty string ""
        flag = "" 
        
        if amount > 500:
            flag = ["HIGH VALUE"]
        else:
            flag = ""

        # --- YOUR TASK ENDS HERE ---

        print(f"ID: {txn_id} | Status: {status} | Amount: ${amount}{flag}")

mask_transactions()