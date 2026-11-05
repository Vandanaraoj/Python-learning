inventory = {"sku_01": 50,"sku_02": 150,"sku_03": 75}
# Add a new item using update()
inventory.update({"sku_04": 200})
# Retrieve value using bracket notation
sku_02_stock = inventory["sku_02"]
# Safely retrieve a missing key using get()
sku_05_stock = inventory.get("sku_05", 0)
# Print keys and values
inventory_ids = list(inventory.keys())
stock_counts = list(inventory.values())
# Convert items into a list of tuples
inventory_items = list(inventory.items())
print("Updated Inventory:", inventory)
print("Stock for sku_02:", sku_02_stock)
print("Stock for sku_05:", sku_05_stock)
print("All SKU IDs:", inventory_ids)
print("All Stock Counts:", stock_counts)
print("Inventory as List of Tuples:", inventory_items)