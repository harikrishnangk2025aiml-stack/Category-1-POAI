def simple_reflex_agent(location, status):
    if status == "Dirty":
        return "Clean the room"
    elif location == "A":
        return "Move to room B"
    elif location == "B":
        return "Move to room A"


location = input("Enter location (A/B): ")
status = input("Enter room status (Clean/Dirty): ")

action = simple_reflex_agent(location, status)

print("Action:", action)