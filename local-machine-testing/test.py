"""
This file executes the database functions for testing functionality on local machine
"""

import databaseFunctions as db

print("-------------------------------------------\nStart of operations:\n")

db.createTable()
db.initializeTable()
db.scanTable()