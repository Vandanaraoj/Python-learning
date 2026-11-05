raw_log = " ERROR_CODE: 404 | STATUS: NOT_FOUND | SOURCE: SERVER_01 "
# Remove leading and trailing whitespace
stripped_log = raw_log.strip()

# Replace underscores with spaces
replaced_log = stripped_log.replace("_", " ")

# Find the index of the first vertical bar
vertical_bar_index = replaced_log.find("|")

# Convert to lowercase
cleaned_log = replaced_log.lower()

# Verification
print("Original Log:", raw_log)
print("Stripped Log:", stripped_log)
print("Underscores Replaced:", replaced_log)
print("Index of '|':", vertical_bar_index)
print("Cleaned Log:", cleaned_log)