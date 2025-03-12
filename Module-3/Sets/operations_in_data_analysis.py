# Task 1: Duplicate Entries Cleanup You are given a list of customer IDs, some of which are duplicated. Write a Python script to remove duplicates and display the unique customer IDs.

# Example Code:

customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]
customer_ids.sort()
print(f"Current customer id's: {customer_ids}")
new_set = sorted(set(customer_ids))
print(f"Fixed customer id's: {new_set}")