# import uuid
#
# confirm_key = uuid.uuid4()
# print(confirm_key)


import requests

# GraphQL endpoint URL
url = "http://localhost:8000/api/v1/graphql"

# GraphQL query
query = """
query {
  allCategories {
    edges {
      node {
        id
        name
      }
    }
  }
}
"""

headers = {
    "Content-Type": "application/json",
    # "Authorization": "Bearer YOUR_ACCESS_TOKEN"  # Agar autentifikatsiya kerak bo'lsa
}

# Request uchun ma'lumot
payload = {
    "query": query
}

# GraphQL queryni jo'natish
response = requests.post(url, json=payload, headers=headers)

if response.status_code == 200:
    print("Query muvaffaqiyatli bajarildi!")
    data = response.json()
    print(data)
else:
    print(f"Xato: {response.status_code}, {response.text}")
