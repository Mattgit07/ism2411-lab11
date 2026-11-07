# Reflection 1:
# I would use .get() for optional fields, such as an email address,
# so missing information returns a default instead of stopping the program.
# I would use bracket notation for required fields, such as a customer's
# name, so a missing key is noticed and can be fixed.

# Reflection 2:
# This pattern reminds me of an Excel PivotTable or SUMIF because
# it adds sales amounts for each region.
# Python can automate repeated summaries across many files without
# manually updating spreadsheet ranges, which is useful for large datasets.


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

# Exercise 7: Nested catalog
print("\nExercise 7")

catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8}
}

for product_name, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {product_name} has {details['stock']} units remaining")

# Exercise 8: Sales by region
        print("\nExercise 8")

transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200}
]

sales_by_region = {}

for transaction in transactions:
    region = transaction["region"]
    amount = transaction["amount"]
    sales_by_region[region] = sales_by_region.get(region, 0) + amount

for region in sorted(sales_by_region):
    print(f"{region}: ${sales_by_region[region]:.2f}")