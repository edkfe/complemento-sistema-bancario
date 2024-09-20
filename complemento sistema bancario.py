from datetime import datetime

menu = """
[1] Depósito
[2] Saque
[3] Extrato
[4] Sair
"""

saldo = 0
extrato = ""
limite = 500
numero_saques = 0
LIMITE_SAQUE = 3
transacoes_diarias = []
LIMITE_TRANSACOES = 10

while True:
    opcao = str(input(menu))

    if opcao == "1":
        valor = float(input("Digite o valor que deseja depositar: "))
        if valor > 0:
            saldo += valor
            data_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            extrato += f"Depósito: R${valor:.2f} em {data_hora}\n"
            transacoes_diarias.append(data_hora)
        else:
            print("Valor inválido! Tente novamente")
       
    elif opcao == "2":
        valor_saque = float(input("Digite o valor para saque: "))
       
        excedeu_limite = valor_saque > limite
        excedeu_saldo = valor_saque > saldo
        excedeu_numero_saques = numero_saques >= LIMITE_SAQUE
        excedeu_transacoes = len(transacoes_diarias) >= LIMITE_TRANSACOES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! Excedeu o limite de saque.")
        elif excedeu_numero_saques:
            print("Operação falhou! Excedeu o número de saques.")
        elif excedeu_transacoes:
            print("Operação falhou! Você excedeu o número de transações permitidas para hoje.")
        elif valor_saque > 0:
            saldo -= valor_saque
            data_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            extrato += f"Saque: R${valor_saque:.2f} em {data_hora}\n"
            transacoes_diarias.append(data_hora)
            numero_saques += 1
        else:
            print("Operação falhou! O valor informado é inválido.")
       
    elif opcao == "3":
        print("\n====== EXTRATO =======")
        print("Sem movimentação." if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")
 
    elif opcao == "4":
        print("Obrigado por usar o sistema.")
        break
   
    else:
        print("Tente novamente!")