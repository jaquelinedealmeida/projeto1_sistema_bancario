menu = """
Selecione a opção que deseja: 
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opção = input(menu)

    if opção == "d":
        valor = float(input("Informe o valor a ser depositado: "))
        
        if valor > 0: 
            saldo += valor
            extrato += f" \nDepósito: R$ {valor:.2f}\n"
            "======================================"

        else:
            print("Operação falhou! O valor informado é inválido")

    elif opção == "s":
        valor = float(input("Informe o valor para saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Não é possível realizar a operação. Você não tem saldo suficiente.")
            "======================================"
       
        elif excedeu_limite:
            print("Não é possível realizar a operação. Valor de saque maior que o limite.")
            "======================================"
        
        elif excedeu_saques:
            print("Não é possível realizar a operação. O número de limite de saques excedeu.")
            "======================================"

        elif valor > 0:
            saldo -= valor
            extrato +=  f"\nSaque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação não é válida. Informe um número válido")
            
    elif opção == "e":
        print("\n=================== EXTRATO DO DIA ===============")
        print("\n Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo:.2f}")
        print("=====================================================")

    
    elif opção == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")