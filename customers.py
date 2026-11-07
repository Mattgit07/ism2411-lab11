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

#excercise 3: Safe lookup
print("\nExercise 3")
print(customer.get("email", "no email on file"))
try:
    print(customer["email"])
except KeyError:
    print("KeyError: 'email' is missing")

#Exercise 4: Iterate
print("\nExercise 4")

for key, value in customer.items():
    print(f"{key}: {value}")

print("Keys only")

#Without .items(), the loop gives only keys, not their values
for key in customer:
    print(key)