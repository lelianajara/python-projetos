# Entrada do usuário
email = input().strip()

# Verificar se contém espaço
if ' ' in email:
    print("E-mail inválido")

# Verificar se contém exatamente um "@"
elif email.count('@') != 1:
    print("E-mail inválido")

# Verificar se não começa ou termina com "@"
elif email.startswith('@') or email.endswith('@'):
    print("E-mail inválido")

# Verificar se o domínio contém um ponto (ex: .com)
else:
    nome_usuario, dominio = email.split('@')
    if '.' not in dominio:
        print("E-mail inválido")
    else:
        print("E-mail válido")
