#!/usr/bin/python3
from Finance import Budget

transactions = [512 , 42.08 , -12]
wallet = Budget()
wallet.add_transactions(transactions)
wallet.show_transactions()