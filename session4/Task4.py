csv_data = "Apple,iPhone,1200,Silver"
# Convert CSV string into a list
product_details = csv_data.split(",")

# Change price at index 2
product_details[2] = "1300"

# Join list using semicolon
reconstructed_data = ";".join(product_details)

# Create header
header = "BRAND;MODEL;PRICE;COLOR"

# Combine header and data with a newline
final_csv_output = header + "\n" + reconstructed_data
print("Product Details List:", product_details)
print("Reconstructed Data:", reconstructed_data)
print("Final CSV Output:")
print(final_csv_output)