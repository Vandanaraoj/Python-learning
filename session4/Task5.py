print("\n" + "-" * 10 + " Task 5: Atomic Dictionary Merging & Popping " + "-" * 10)
# Create dictionaries
personal_info = {"name": "John","age": 30}
job_info = {"salary": 5000,"role": "Analyst"}

# Merge dictionaries using Dictionary Union Operator
full_profile = personal_info | job_info

# Remove age and store its value
removed_age = full_profile.pop("age")

# Clear personal_info
personal_info.clear()

# Print results
print("Full Profile:", full_profile)
print("Removed Age:", removed_age)
print("Personal Info After Clear:", personal_info)
print("Length of Personal Info:", len(personal_info))