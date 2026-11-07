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

#Exercise 5: Lookup table
print("\nExercise 5")

tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.10,
    "platinum": 0.15
}

purchase_amount = 200.00
discount_rate = tier_discounts.get(customer["tier"], 0)
discount_amount = purchase_amount * discount_rate
final_price = purchase_amount - discount_amount

print(f"Tier: {customer['tier']}")
print(f"Discount: {discount_rate:.0%}")
print(f"Final price: ${final_price:.2f}")

#Exercise 6: List of dictionaries
print("\nExercise 6")

customers = [
    {"name": "Alice", "tier": "platinum"},
    {"name": "Bob", "tier": "silver"},
    {"name": "Carol", "tier": "gold"}
]

for person in customers:
    rate = tier_discounts.get(person["tier"], 0)
    discount = 300.00 * rate
    print(f"{person['name']} | {person['tier']} | Discount: ${discount:.2f}")
    