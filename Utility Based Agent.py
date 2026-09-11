location = input("Location (A/B): ")
status = input("Status (Clean/Dirty): ")

if status == "Dirty":
    utility_clean = 10
    utility_move = 2
else:
    utility_clean = 3
    utility_move = 8

if utility_clean > utility_move:
    print("Action: Clean")
else:
    print("Action: Move")

print("Best Utility:", max(utility_clean, utility_move))