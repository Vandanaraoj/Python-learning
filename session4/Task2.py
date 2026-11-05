# Data Setup
api_response = {"status": "success",
    "data": [
        {"id": 1,"info": {"email": "user1@work.com","tags": ["admin", "dev"]}},
        {"id": 2,"info": {"email": "user2@work.com","tags": ["guest"]}}]}
# Access first user's email
user_1_email = api_response["data"][0]["info"]["email"]
# Access second tag of first user
user_1_secondary_tag = api_response["data"][0]["info"]["tags"][1]
# Access last user's ID using negative indexing
last_user_id = api_response["data"][-1]["id"]
# Print results
print("First User Email:", user_1_email)
print("First User Secondary Tag:", user_1_secondary_tag)
print("Last User ID:", last_user_id)
# Print data types
print("Type of api_response['data']:", type(api_response["data"]))
print("Type of first user's info:", type(api_response["data"][0]["info"]))