menu = """

Bem-vindo ao Aplicativo do Banco!

Digite o número da opção desejada:

    1. Depositar Dinheiro
    2. Sacar Dinheiro
    3. Extrato
    4. Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)

    if opcao == "1":
        valor_deposito = float(input("Quanto você deseja depositar? "))
        
        if valor_deposito > 0:
           saldo += valor_deposito
           extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
        
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "2":
        valor_saque = float(input("Quanto você deseja sacar? "))
        
        excedeu_saldo = valor_saque > saldo

        excedeu_limite = valor_saque > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        
        elif valor_saque > 0:
            saldo -= valor_saque
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
            numero_saques += 1
            print(f"Saque realizado com sucesso! Seu novo saldo é: R$ {saldo:.2f}")

        else:
            print("Operação falhou! O valor informado é inválido.")
        
    elif opcao == "3":
        print("\n================EXTRATO================")
        print("Não realizada movimentações. " if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("=========================================")

    elif opcao == "4":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida, por favor escolha uma opção válida.")