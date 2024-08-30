# Account.py
from Account import Account
# Class Account:
def __init__(self, balance, interest_rate):
        self.balance = balance
        self.interest_rate = interest_rate
        self.interest_earned = 0

    # This method sets the balance of the account.
def set_balance(self, balance):
        """Sets the balance for the for the account"""
        self.balance = balance

    # The method sets the interest gained for the account.
def set_interest(self, interest):
        """Sets the interest gained for the the account"""
        self.interest_earned = interest

def get_balance(self):
    return self.balance

def get_interest(self):
      return self.interest_earned


# Define a function for the Savings Account
def create_savings_account(balance, interest, months):
    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

        
    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    savings_account = Account(balance, 0)
    # Calculate interest earned
    interest_earned = balance * (interest / 100) * (months / 12)

    # Update the savings account balance by adding the interest earned
    updated_balance = balance + interest

    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    savings_account.set_balance(updated_balance)
    savings_account.set_interest(interest)

    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    savings_account.set_interest(interest_earned)

    # Return the updated balance and interest earned.
    return  updated_balance, interest
