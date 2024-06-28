# YODA CHAT

Projetinho de estudo. Coisa bem simples...

- Instale o MemGPT:

```shell
pip install pymemgpt
```

- Execute o MemGPT Server:

```bash
memgpt server
```

- Obtenha no console do server a password para a sessão. Exemplo:

```text
Generated admin server password for this session: dgXyIIWuysdweRZIykhgSg
```

- Adicione o token da sessao no arquivo .ENV em MEMGPT_SESSION_TOKEN
- Crie o primeiro usuario com o script create_user.py. O script vai retornar a API Key para esse usuário. Defina ela no arquivo .env na variavel MEMGPT_CLIENT_TOKEN.

- Crie o primeiro agente com os script create_yoda_agent.py. O script irá retornar o ID do agente criado. Salve o ID no arquivo .env em MEMGPT_AGENT_ID.

- Execute o script do bot yoda.py e faça a primeira pergunta.
