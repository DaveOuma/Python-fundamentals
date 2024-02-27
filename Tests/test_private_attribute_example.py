#!/usr/bin/python3

import unittest
from private_attribute_example import BankAccount

class TestBankAccount(unittest.TestCase):
    def test_deposit(self):
        account = BankAccount(123456, 100)
        account.deposit(50)
        self.assertEqual(account.get_balance(), 150)

    def test_withdraw_sufficient_balance(self):
        account = BankAccount(123456, 100)
        account.withdraw(50)
        self.assertEqual(account.get_balance(), 50)

    def test_withdraw_insufficient_balance(self):
        account = BankAccount(123456, 100)
        account.withdraw(150)
        self.assertEqual(account.get_balance(), 100)

if __name__ == '__main__':
    unittest.main()
