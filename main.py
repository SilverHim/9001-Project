import bank
import datetime
import pickle

DATA_FILE = "piggy_bank_data.pkl" 
accounts = {} 

def load_data():
    # Load existing accounts from the data file
    global accounts
    try:
        with open(DATA_FILE, "rb") as f:
            accounts = pickle.load(f)
    except (FileNotFoundError, EOFError):
        accounts = {}

def save_data():
    # Save the current accounts to the data file
    with open(DATA_FILE, "wb") as f:
        pickle.dump(accounts, f)


def main():
    # Load existing accounts from the data file
    load_data()

    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{'-' * 26}\n"
        f"Welcome to the piggy bank!\n"
        f"{'-' * 26}\n"
        f"Current time: {now}\n"
        f"Please input 'HELP' to get insturction:\n")

    print("please select your account, if account not exist, will automatically create a new one.")
    account_name = []
    while True:
        account_name = input(">>> ").strip().split()
        # Check if the input is empty
        if not account_name:
            print("Please enter a command.")
            continue
        account_name[0] = account_name[0].upper()

        if account_name[0] == "HELP" and len(account_name) == 1:
            print("1. <HELP> - Show this help message\n"
            "2. <SHOW> - Show all accounts\n"
            "3. <DELETE> <name> - Delete an account\n"
            "4. <SELECT> <name> - Select an account\n    name expect full letters and no more than 10 characters, recommend to use your name as your account name.\n"
            "    if account not exist, it will automatically create a new one.\n"
            "5. <EXIT> - Exit the program\n")

        elif account_name[0] == "SHOW" and len(account_name) == 1:
            if not accounts:
                print("No accounts available.")
            else:
                print("Available accounts:")
                for name in accounts.keys():
                    print(f"- {name}")

        elif account_name[0] == "DELETE" and len(account_name) == 2:
            if account_name[1] in accounts:
                del accounts[account_name[1]]
                print(f"Account '{account_name[1]}' deleted successfully.")
                save_data()
            else:
                print(f"Account '{account_name[1]}' does not exist.")

        elif account_name[0] == "SELECT" and len(account_name) == 2: 
            if len(account_name[1]) > 10 or not account_name[1].isalpha():
                print("Invalid account name. Please use only letters and no more than 10 characters.")

            elif account_name[1] not in accounts:
                # Create a new account if it does not exist and store it in the accounts dictionary
                accounts[account_name[1]] = bank.account(account_name[1])
                print(f"Account '{account_name[1]}' created successfully.")
                current_account = accounts[account_name[1]]
                save_data()
                break

            else:
                current_account = accounts[account_name[1]]
                break
       
        elif account_name[0] == "EXIT" and len(account_name) == 1:
            print("Goodbye!")
            exit()

        else:
            print("Invalid command. Please try again or type 'HELP' for instructions.")
        
    print(f"\nCurrent select account: {current_account.name}\n")
    print(f"Welcome {current_account.name}, your current balance is: {current_account.balance:.2f}\n\n"
        f"Please input your command")
    while True:
        command = input(">>> ").strip().upper().split()
        # Check if the input is empty
        if not command:
            print("Please enter a command.")
            continue

        if command[0] == "HELP":
            print("Available commands:\n"
                "1. STATEMENT <yyyy-mm-dd> - show the bank statement up to yyyy-mm-dd\n\n"
                "2. DEPOSIT <amount> <source>- deposite money into the account and note the source\n"
                "   Valid source: WAGE, GIFT, LOAN, FAMILY, ALLOWANCE, CAPITAL, OTHERS (if you not input source, it will be defualted to OTHERS)\n\n"
                "3. WITHDRAW <amount> <source>- withdraw money from the account and note the source\n"
                "   Valid source: FOOD, ENTERTAINMENT, FAMILY, HOUSE, SHOPPING, TRAFFIC, HEALTH, FINANCE, OTHERS (if you not input source, it will be defualted to OTHERS)\n\n"
                "4. EXIT - Exit the program\n")
    
        elif command[0] == "STATEMENT":
            try:
                # Check if a date is provided
                date_str = command[1]
                date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
                current_account.statement(date_obj)
            except ValueError:
                print("Invalid date format. Please use yyyy-mm-dd.")
            except IndexError:
                current_account.statement(None)

        elif command[0] == "DEPOSIT":
            # Check if the command has at least 2 arguments
            if len(command) < 2:
                print("Error: DEPOSIT: DEPOSIT <amount> <source>")
                continue
            try:
                # Check if a valid amount is provided
                amount = float(command[1])
                if len(command) >= 3:
                    source = command[2]
                    print(current_account.deposit(amount, source))
                else:
                    print(current_account.deposit(amount))
                save_data()
            except ValueError as e:
                print(e)


        elif command[0] == "WITHDRAW":
            # Check if the command has at least two arguments
            if len(command) < 2:
                print("Error: WITHDRAW: WITHDRAW <amount> <source>")
                continue
            try:
                # Check if a valid amount is provided
                amount = float(command[1])
                if len(command) >= 3:
                    source = command[2]
                    print(current_account.withdraw(amount, source))
                else:
                    print(current_account.withdraw(amount))
                save_data()
            except ValueError as e:
                print(e)

        elif command[0] == "EXIT":
            print("Goodbye!")
            exit()
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__": 
    main()