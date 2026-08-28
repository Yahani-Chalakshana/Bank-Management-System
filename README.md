# ABC Bank Management System

A Python-based **ABC Bank Management System** developed as an individual academic project for the **DOC333 – Introduction to Programming Principles** module at the Informatics Institute of Technology (IIT), Sri Lanka.

The application is a console-based banking system designed to manage customer savings accounts, perform basic banking transactions, and maintain customer information.

---

## Project Overview

The ABC Bank Management System was developed to provide a simple way for a small bank to manage its customer accounts.

The system supports a maximum of **five customers** and allows users to:

* Register new customers
* View individual customer details
* View all registered customers
* Deposit money
* Withdraw money
* Update customer details
* Exit the system

The project focuses on applying fundamental Python programming concepts to solve a practical problem.

---

# Features

### Customer Management

* Add new customers
* Store customer account information
* View individual customer details
* View all registered customers
* Update customer information
* Maximum of five customer accounts

### Banking Transactions

* Deposit money into an account
* Withdraw money from an account
* Check available account balance
* Prevent withdrawals exceeding the available balance

### Input Validation

The application validates important user inputs, including:

* Bank account number
* NIC number
* First name
* Last name
* Birth date
* Address
* Telephone number
* Transaction amounts

Invalid inputs result in appropriate error messages and allow the user to enter the information again.

### Error Handling

The program handles invalid inputs and prevents incorrect operations from causing the application to terminate unexpectedly.

---

# Main Menu

The application provides the following menu:

```text
ABC Bank

1) Add a new customer
2) View details of a customer including his/her bank balance
3) View details of all the customers with their bank balances
4) Deposit money to a given account
5) Withdraw money from a given account
6) Update Customer Details
7) Exit
```

---

# Customer Information

Each customer record contains:

| Field               | Description                   |
| ------------------- | ----------------------------- |
| Bank Account Number | 10-digit account number       |
| NIC                 | National Identity Card number |
| First Name          | Customer's first name         |
| Last Name           | Customer's last name          |
| Birth Date          | Customer's date of birth      |
| Permanent Address   | Customer's permanent address  |
| Phone Number        | Customer's telephone number   |
| Bank Balance        | Current account balance       |

The account number and bank balance are protected from modification through the customer update functionality.

---

# Program Structure

The application is implemented in a single Python file:

```text
ABC_bank.py
```

The program uses functions to separate different operations of the banking system.

### Main Functional Areas

```text
Main Menu
│
├── Add New Customer
├── View Customer Details
├── View All Customer Details
├── Deposit Money
├── Withdraw Money
├── Update Customer Details
└── Exit
```

---

# Technologies Used

* **Python 3.x**
* Lists
* Variables
* Functions
* Conditional statements
* Loops
* String manipulation
* Input validation
* Exception handling
* Console-based user interface

No external Python libraries are required to run the application.

---

# How to Run

## Requirements

Install **Python 3.x** on your computer.

Check whether Python is installed:

```bash
python --version
```

## Run the Application

Clone the repository and navigate to the project directory.

Then run:

```bash
python ABC_bank.py
```

The ABC Bank main menu will appear in the console.

---

# How the System Works

## 1. Add a New Customer

The user selects option `1` from the main menu.

The application requests the customer's:

* Bank account number
* NIC
* First name
* Last name
* Birth date
* Permanent address
* Phone number

The entered information is validated before the customer is added.

The system allows a maximum of five customers.

---

## 2. View Customer Details

The user selects option `2` and enters a bank account number.

If the account exists, the system displays relevant customer information, including the current bank balance.

---

## 3. View All Customers

Option `3` displays the registered customers together with important account information such as:

* NIC
* Account number
* First name
* Last name
* Bank balance

The system also provides the option to update customer details.

---

## 4. Deposit Money

Option `4` allows the user to deposit money into a selected account.

The system:

1. Requests the account number.
2. Requests the deposit amount.
3. Validates the information.
4. Asks the user whether the transaction should be saved.
5. Updates the account balance when confirmed.

---

## 5. Withdraw Money

Option `5` allows money to be withdrawn from a customer's account.

The system checks whether the requested withdrawal amount is within the available balance.

A withdrawal is not accepted when the requested amount exceeds the account balance.

---

## 6. Update Customer Details

Option `6` allows existing customer information to be modified.

The following details can be updated:

* NIC
* First name
* Last name
* Birth date
* Permanent address
* Phone number

The **bank account number and bank balance cannot be changed** through this functionality.

---

## 7. Exit

Option `7` exits the application and displays a thank-you message.

```text
Thank you for choosing ABC Bank
```

---

# Data Structure

The project uses Python **lists** to store customer information.

The list-based approach allows multiple customer records to be stored and accessed during program execution.

Customer information can be searched using the bank account number, allowing the program to identify the correct customer when performing operations such as:

* Viewing details
* Depositing money
* Withdrawing money
* Updating details

---

# Testing

The application was tested using both positive and negative test cases.

Testing covered all major functionality.

### Main Menu

* Add customer
* View customer
* View all customers
* Deposit money
* Withdraw money
* Update customer
* Exit

### Customer Registration

* Valid account numbers
* Invalid account numbers
* Valid and invalid NIC values
* Name validation
* Address validation
* Phone number validation
* Saving and cancelling customer registration
* Maximum customer limit

### Customer Details

* Searching for valid accounts
* Viewing customer information
* Viewing multiple customer accounts
* Handling invalid account numbers

### Transactions

* Valid deposits
* Invalid deposit amounts
* Valid withdrawals
* Withdrawals exceeding the available balance
* Confirming or cancelling transactions

### Customer Updates

* Updating valid customer information
* Invalid input handling
* Saving updated information
* Cancelling updates

### Exit

* Correctly terminating the program
* Displaying the exit message

---

# Example Test Cases

| Test Case | Description                  | Expected Result                  |
| --------- | ---------------------------- | -------------------------------- |
| 1.1       | Select Add Customer          | Add customer screen displayed    |
| 2.1       | Enter invalid account number | Validation error displayed       |
| 2.2       | Add valid customer           | Customer added successfully      |
| 2.3       | Add sixth customer           | Maximum customer limit displayed |
| 3.1       | Search valid account         | Customer details displayed       |
| 5.1       | Deposit valid amount         | Balance updated                  |
| 6.1       | Withdraw valid amount        | Balance updated                  |
| 6.2       | Withdraw more than balance   | Withdrawal rejected              |
| 7.1       | Update customer details      | Details updated successfully     |
| 8.1       | Select Exit                  | Program terminates               |

The coursework report contains detailed test cases and screenshots demonstrating the actual results.

---

# Learning Outcomes

This project provided practical experience with fundamental programming concepts, including:

* Problem solving
* Algorithm design
* Python programming
* Lists and data structures
* Functions
* Variables
* Conditional statements
* Loops
* String operations
* Input validation
* Error handling
* User interaction
* Testing and debugging

The project also provided experience in translating a real-world banking scenario into a working software solution.

---

# Academic Project

**Module:** DOC333 – Introduction to Programming Principles  
**Programme:** Foundation Certificate in Higher Education  
**Institution:** Informatics Institute of Technology (IIT), Sri Lanka  
**Assignment Type:** Individual  
**Programming Language:** Python 3.x

This project was developed as an academic coursework project.

---

# Author

**Yahani Chalakshana Dissanayake**

Foundation Certificate in Higher Education

Informatics Institute of Technology (IIT), Sri Lanka
