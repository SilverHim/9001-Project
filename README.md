## Piggy Bank - Quick Start Guide

Piggy Bank is a command-line accounting tool designed to help you manage your income and expenses and view your financial status.

### 1. Startup & Account Selection

After starting the program, you first need to select or create an account.

* **`HELP`**
    * Displays help information for this stage.
* **`SHOW`**
    * Lists all existing accounts.
* **`DELETE <name>`**
    * Deletes the account with the specified name (`<name>`).
* **`SELECT <name>`**
    * Selects or creates an account.
    * **Requirement**: The account name (`<name>`) must contain **only letters** and be **no longer than 10 characters**.
    * Upon successful selection, you will enter the account operations interface for that account.

### 2. Account Operations

After entering a specific account, you can use the following commands for accounting and queries:

* **`HELP`**
    * Displays help information for this stage.
* **`STATEMENT`** or **`STATEMENT <yyyy-mm-dd>`**
    * Displays the financial statement.
    * Without a date, it shows the report up to the current date. With a date (in `yyyy-mm-dd` format), it shows the report up to that specific date.
    * **The statement includes**:
        * Ending balance.
        * A detailed list of transactions (Time, Type, Amount, Source/Purpose, Balance).
        * A summary of income and expenses by category, including percentages.
* **`DEPOSIT <amount> [<source>]`**
    * Records a deposit.
    * `<amount>`: The amount to deposit.
    * `<source>` (Optional): The source of the income. Defaults to `OTHERS`.
    * **Valid sources**: `WAGE`, `GIFT`, `LOAN`, `FAMILY`, `ALLOWANCE`, `CAPITAL`, `OTHERS`.
* **`WITHDRAW <amount> [<source>]`**
    * Records a withdrawal.
    * `<amount>`: The amount to withdraw.
    * `<source>` (Optional): The purpose of the expense. Defaults to `OTHERS`.
    * **Valid sources**: `FOOD`, `ENTERTAINMENT`, `FAMILY`, `HOUSE`, `SHOPPING`, `TRAFFIC`, `HEALTH`, `FINANCE`, `OTHERS`.
* **`EXIT`**
    * Exits the program.

### 3. Notes

* Commands are **case-insensitive** (e.g., `deposit` is the same as `DEPOSIT`).
* Use **spaces** to separate commands and their arguments.
* All data is **saved automatically**.

