texto = input("Digite um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

print()  # Para garantir que o cursor vá para a próxima linha após imprimir as vogais
# O código acima lê um texto do usuário e imprime apenas as vogais presentes nele.