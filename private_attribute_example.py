#!/usr/bin/python3
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number #Protected attribute
        self.__balance = balance #Private attribute

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")


