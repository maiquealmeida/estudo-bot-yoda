import os
from dotenv import load_dotenv
from memgpt import create_client

load_dotenv()

MEMGPT_BASE_URL=os.environ['MEMGPT_BASE_URL']
MEMGPT_CLIENT_TOKEN=os.environ['MEMGPT_CLIENT_TOKEN']

client = create_client(
    base_url=MEMGPT_BASE_URL, 
    token=MEMGPT_CLIENT_TOKEN
)

agent_info = client.create_agent(
    name="MestreYoda1",
    persona=""""
        Você é Yoda, personagem do filme Star Wars. 
        Você sempre responde em português brasileiro, no estilo do Yoda e
        utiliza citações que o personagem do filme utiliza.
    """
)

print(agent_info.id)