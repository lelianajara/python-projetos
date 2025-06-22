# Entrada do usuário
preco = float(input())
cupom = input().strip()

# Aplicando o desconto com base no cupom
if cupom == "DESCONTO10":
    preco_final = preco * 0.90
elif cupom == "DESCONTO20":
    preco_final = preco * 0.80
else:
    preco_final = preco

# Saída com duas casas decimais
print(f"{preco_final:.2f}")
