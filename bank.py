import datetime

class account():
    def __init__(self, name):
        self.name = name
        self.balance = 0.0
        self.transactions = []
        self.plan = None

    def deposit(self, amount, source = "OTHERS"):
        # Get the current time
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            # Check if amount is a number
            amount = float(amount)
        except ValueError:
            raise ValueError("Deposit amount must be a number.")
        # Check if amount is positive
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        # Check if source is valid
        if source not in ["WAGE", "GIFT", "LOAN", "FAMILY", "ALLOWANCE", "CAPITAL", "OTHERS"]:
            raise ValueError("Invalid source for deposit. Valid sources are: WAGE, GIFT, LOAN, FAMILY, ALLOWANCE, CAPITAL, OTHERS.")
        self.balance += amount
        # Record the transaction
        self.transactions.append(["DEPOSIT", amount, source, self.balance, now])
        return f"Deposited successfully. New balance: {self.balance:.2f}"
    

    def withdraw(self, amount, source = "OTHERS"):
        # Get the current time
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  
        try:
            # Check if amount is a number
            amount = float(amount)
        except ValueError:
            raise ValueError("Withdrawal amount must be a number.")
        # Check if amount is positive and sufficient funds are available
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds for withdrawal.")
        # Check if source is valid
        if source not in ["FOOD", "ENTERTAINMENT", "FAMILY", "HOUSE", "SHOPPING", "TRAFFIC", "HEALTH", "FINANCE", "OTHERS"]:
            raise ValueError("Invalid source for withdrawal. Valid sources are: FOOD, ENTERTAINMENT, FAMILY, HOUSE, SHOPPING, TRAFFIC, HEALTH, FINANCE, OTHERS.")
        self.balance -= amount
        # Record the transaction
        self.transactions.append(["WITHDRAW", amount, source, self.balance, now])
        return f"Withdrew successfully. New balance: {self.balance:.2f}"
    
    def statement(self, date = None):
       # Set default date to current date if not provided
        if date is None:
            date = datetime.datetime.now()

        print(f"--- Bank Statement ---")
        print(f"Account Name: {self.name}")
        print(f"Statement Date: {date.strftime('%Y-%m-%d')}")
        print("-" * 30)
       
        # Initialize variables
        balance_at_date = 0.0
        transactions_in_period = []

        rev_wage = rev_gift = rev_loan = rev_family = rev_allowance = rev_capital = rev_others = 0.0
        exp_food = exp_entertainment = exp_family = exp_house = exp_shopping = exp_traffic = exp_health = exp_finance = exp_others = 0.0
        
        # Iterate through transactions and filter by date
        for transaction in self.transactions:
            transaction_date = datetime.datetime.strptime(transaction[4], "%Y-%m-%d %H:%M:%S")
            if transaction_date <= date:
                transactions_in_period.append(transaction)
                balance_at_date = transaction[3] 

                tx_type = transaction[0]
                tx_amount = transaction[1]
                tx_source = transaction[2]
               
                # Update revenue and expense categories based on transaction type and source
                if tx_type == "DEPOSIT":
                    if tx_source == "WAGE": rev_wage += tx_amount
                    elif tx_source == "GIFT": rev_gift += tx_amount
                    elif tx_source == "LOAN": rev_loan += tx_amount
                    elif tx_source == "FAMILY": rev_family += tx_amount
                    elif tx_source == "ALLOWANCE": rev_allowance += tx_amount
                    elif tx_source == "CAPITAL": rev_capital += tx_amount
                    elif tx_source == "OTHERS": rev_others += tx_amount
                elif tx_type == "WITHDRAW":
                    if tx_source == "FOOD": exp_food += tx_amount
                    elif tx_source == "ENTERTAINMENT": exp_entertainment += tx_amount
                    elif tx_source == "FAMILY": exp_family += tx_amount 
                    elif tx_source == "HOUSE": exp_house += tx_amount
                    elif tx_source == "SHOPPING": exp_shopping += tx_amount
                    elif tx_source == "TRAFFIC": exp_traffic += tx_amount
                    elif tx_source == "HEALTH": exp_health += tx_amount
                    elif tx_source == "FINANCE": exp_finance += tx_amount
                    elif tx_source == "OTHERS": exp_others += tx_amount 

        # Print the balance and transactions
        print(f"Balance as of {date.strftime('%Y-%m-%d')}: {balance_at_date:.2f}")
        print("-" * 30)
        print("Transactions:")
        if not transactions_in_period:
            print("No transactions in this period.")
        else:
            for tx in transactions_in_period:
                # tx: [Type, Amount, Source, Balance, Timestamp]
                print(f"  {tx[4]} - {tx[0]:<8} - {tx[1]:>10.2f} - {tx[2]:10} - Bal: {tx[3]:>5.2f}")
        
        print("\n" + "-" * 30)
        print("Summary:")
        print("-" * 30)

        # Calculate total revenue and expenses
        total_revenue = rev_wage + rev_gift + rev_loan + rev_family + rev_allowance + rev_capital + rev_others
        total_expense = exp_food + exp_entertainment + exp_family + exp_house + exp_shopping + exp_traffic + exp_health + exp_finance + exp_others

        # Print total revenue and expenses with breakdown
        if total_revenue == 0:
            print("No revenue recorded.")
        else:
            print(f"Total Revenue: {total_revenue:.2f}")
            print("Revenue Breakdown:")
            print(f"  WAGE:      {rev_wage:.2f} ({rev_wage/total_revenue:.2%})")
            print(f"  GIFT:      {rev_gift:.2f} ({rev_gift/total_revenue:.2%})")
            print(f"  LOAN:      {rev_loan:.2f} ({rev_loan/total_revenue:.2%})")
            print(f"  FAMILY:    {rev_family:.2f} ({rev_family/total_revenue:.2%})")
            print(f"  ALLOWANCE: {rev_allowance:.2f} ({rev_allowance/total_revenue:.2%})")
            print(f"  CAPITAL:   {rev_capital:.2f} ({rev_capital/total_revenue:.2%})")
            print(f"  OTHERS:    {rev_others:.2f} ({rev_others/total_revenue:.2%})")
            
        print("-" * 30)
        
        # Print total expenses with breakdown
        if total_expense == 0:
            print("No expense recorded.")
        else:
            print(f"Total Expense: {total_expense:.2f}")
            print("Expense Breakdown:")
            print(f"  FOOD:          {exp_food:.2f} ({exp_food/total_expense:.2%})")
            print(f"  ENTERTAINMENT: {exp_entertainment:.2f} ({exp_entertainment/total_expense:.2%})")
            print(f"  FAMILY:        {exp_family:.2f} ({exp_family/total_expense:.2%})")
            print(f"  HOUSE:         {exp_house:.2f} ({exp_house/total_expense:.2%})")
            print(f"  SHOPPING:      {exp_shopping:.2f} ({exp_shopping/total_expense:.2%})")
            print(f"  TRAFFIC:       {exp_traffic:.2f} ({exp_traffic/total_expense:.2%})")
            print(f"  HEALTH:        {exp_health:.2f} ({exp_health/total_expense:.2%})")
            print(f"  FINANCE:       {exp_finance:.2f} ({exp_finance/total_expense:.2%})")
            print(f"  OTHERS:        {exp_others:.2f} ({exp_others/total_expense:.2%})")
                
        print("-" * 30)


            