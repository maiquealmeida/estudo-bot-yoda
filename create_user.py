import os
from dotenv import load_dotenv
from memgpt import Admin
load_dotenv()

MEMGPT_BASE_URL=os.environ['MEMGPT_BASE_URL']
MEMGPT_SESSION_TOKEN=os.environ['MEMGPT_SESSION_TOKEN']
MEMGPT_CLIENT_TOKEN=os.environ['MEMGPT_CLIENT_TOKEN']

admin = Admin(base_url=MEMGPT_BASE_URL, token=MEMGPT_SESSION_TOKEN)

response = admin.create_user()

print(f"User ID: {response.user_id} API Key: {response.api_key}")