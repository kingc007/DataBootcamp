store_name = "Downtown"
transactions = 118
revenue = 978.00
promotion_active = False

menu_items = ["coffee", "tea", "pastry"]

store = {
    "name": store_name,
    "transactions": transactions,
    "revenue": revenue,
}
print("Store:", store_name)
print("Transactions:", transactions)
print("Revenue:", revenue)
print("Menu items:", menu_items)
print("Store information:", store)

menu_items.append("sandwich")
average_sale = revenue / transactions

print("Updated menu:", menu_items)
print("Average sale:", round(average_sale, 2))