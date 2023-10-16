real = float(input("Digite o Valor em Real: "))
dolar = float(input("Digite a cotação do dia: "))
conversão = real / dolar
print(f"""
    Seu Valor em R$ {real}
    Cotação atual em $ {dolar}

    Valor de Convesão $ {conversão}
""")