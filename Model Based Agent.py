state = {}

location = input("Location (A/B): ")
status = input("Status (Clean/Dirty): ")

state[location] = status

if status == "Dirty":
    print("Action: Clean")
elif location == "A":
    print("Action: Move to B")
else:
    print("Action: Move to A")

print("Memory:", state)