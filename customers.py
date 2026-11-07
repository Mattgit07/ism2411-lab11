# Excercise 1: One customer

customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 12400.00
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)

#Excercise 2: Update and add
print("\nExercise 2")

customer["phone"] = "555-0100"
print(customer)

customer["tier"] = "platinum"
print(customer)

del customer["email"]
print(customer)