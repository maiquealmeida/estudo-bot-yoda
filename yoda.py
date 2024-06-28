import os
from dotenv import load_dotenv
from memgpt import create_client
from utils import say

load_dotenv()

MEMGPT_BASE_URL=os.environ['MEMGPT_BASE_URL']
MEMGPT_CLIENT_TOKEN=os.environ['MEMGPT_CLIENT_TOKEN']
MEMGPT_AGENT_ID=os.environ['MEMGPT_AGENT_ID']

client = create_client(
    base_url=MEMGPT_BASE_URL, 
    token=MEMGPT_CLIENT_TOKEN
)

while True:
    user_input = input("> ")
    response = client.user_message(
        agent_id=MEMGPT_AGENT_ID,
        message=user_input
    )

    print(response)

    for r in response.messages:
        if "assistant_message" in r:
            print("ASSISTANT: ", r["assistant_message"])
            # say(r["assistant_message"])
        elif "internal_monologue" in r:
            print("THOUGHTS: ",r["internal_monologue"])
            # say(r["internal_monologue"])
    