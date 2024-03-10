contatos = {
   "oi@silvaneimartins.com": {"nome": "Silvanei Martins", "telefone": "3333-2221"},
    "suporte@silvaneimartins.com": {"nome": "Suporte", "telefone": "3443-2121"},
    "vendas@silvaneimartins.com": {"nome": "Vendas", "telefone": "3344-9871"},
    "comercial@silvaneimartins.com": {"nome": "Comercial", "telefone": "3333-7766"},
}

for chave in contatos:
    print(chave, contatos[chave])

print("=" * 100)

for chave, valor in contatos.items():
    print(chave, valor)
