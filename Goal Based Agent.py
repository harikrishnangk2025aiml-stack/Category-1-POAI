goal = "Clean"

location = input("Location (A/B): ")
status = input("Status (Clean/Dirty): ")

if status == "Dirty" and goal == "Clean":
    print("Action: Clean the room")
elif location == "A":
    print("Action: Move to B")
else:
    print("Action: Move to A")