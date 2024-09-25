from datetime import datetime

# Dicionários para armazenar usuários e contas
usuarios = {}
contas_correntes = {}

# Função para criar um usuário
def criar_usuario(cpf, nome, data_nascimento, endereco):
    if cpf in usuarios:
        print("Usuário já cadastrado!")
    else:
        usuarios[cpf] = {
            "nome": nome,
            "data_nascimento": data_nascimento,
            "endereco": endereco
        }
        print("Usuário criado com sucesso!")

# Função para criar uma conta corrente vinculada a um usuário
def criar_conta_corrente(cpf):
    if cpf not in usuarios:
        print("Usuário não encontrado! Cadastre o usuário primeiro.")
    else:
        numero_conta = len(contas_correntes) + 1  # Gerar número da conta
        contas_correntes[numero_conta] = {
            "cpf": cpf,
            "saldo": 0,
            "limite": 500,
            "numero_saques": 0,
            "extrato": "",
            "transacoes_diarias": []
        }
        print(f"Conta corrente {numero_conta} criada com sucesso para {usuarios[cpf]['nome']}!")

# Função para exibir o menu
def exibir_menu():
    menu = """
    [1] Criar usuário
    [2] Criar conta corrente
    [3] Depósito
    [4] Saque
    [5] Extrato
    [6] Sair
    """
    return input(menu)

# Função principal que executa o sistema
def sistema_banco():
    LIMITE_SAQUE = 3
    LIMITE_TRANSACOES = 10
    
    while True:
        opcao = exibir_menu()

        if opcao == "1":
            cpf = input("Informe o CPF (somente números): ")
            nome = input("Informe o nome completo: ")
            data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
            endereco = input("Informe o endereço (logradouro, número - bairro - cidade/UF): ")
            criar_usuario(cpf, nome, data_nascimento, endereco)

        elif opcao == "2":
            cpf = input("Informe o CPF do usuário: ")
            criar_conta_corrente(cpf)

        elif opcao == "3":
            numero_conta = int(input("Informe o número da conta: "))
            if numero_conta not in contas_correntes:
                print("Conta não encontrada!")
            else:
                valor = float(input("Digite o valor que deseja depositar: "))
                if valor > 0:
                    contas_correntes[numero_conta]["saldo"] += valor
                    data_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    contas_correntes[numero_conta]["extrato"] += f"Depósito: R${valor:.2f} em {data_hora}\n"
                    contas_correntes[numero_conta]["transacoes_diarias"].append(data_hora)
                else:
                    print("Valor inválido! Tente novamente")
        
        elif opcao == "4":
            numero_conta = int(input("Informe o número da conta: "))
            if numero_conta not in contas_correntes:
                print("Conta não encontrada!")
            else:
                valor_saque = float(input("Digite o valor para saque: "))
                conta = contas_correntes[numero_conta]
                
                excedeu_limite = valor_saque > conta["limite"]
                excedeu_saldo = valor_saque > conta["saldo"]
                excedeu_numero_saques = conta["numero_saques"] >= LIMITE_SAQUE
                excedeu_transacoes = len(conta["transacoes_diarias"]) >= LIMITE_TRANSACOES

                if excedeu_saldo:
                    print("Operação falhou! Você não tem saldo suficiente.")
                elif excedeu_limite:
                    print("Operação falhou! Excedeu o limite de saque.")
                elif excedeu_numero_saques:
                    print("Operação falhou! Excedeu o número de saques.")
                elif excedeu_transacoes:
                    print("Operação falhou! Você excedeu o número de transações permitidas para hoje.")
                elif valor_saque > 0:
                    conta["saldo"] -= valor_saque
                    data_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    conta["extrato"] += f"Saque: R${valor_saque:.2f} em {data_hora}\n"
                    conta["transacoes_diarias"].append(data_hora)
                    conta["numero_saques"] += 1
                else:
                    print("Operação falhou! O valor informado é inválido.")
        
        elif opcao == "5":
            numero_conta = int(input("Informe o número da conta: "))
            if numero_conta not in contas_correntes:
                print("Conta não encontrada!")
            else:
                conta = contas_correntes[numero_conta]
                print("\n====== EXTRATO =======")
                print("Sem movimentação." if not conta["extrato"] else conta["extrato"])
                print(f"\nSaldo: R${conta['saldo']:.2f}")

        elif opcao == "6":
            print("Obrigado por usar o sistema.")
            break

        else:
            print("Opção inválida! Tente novamente.")

# Iniciar o sistema
sistema_banco()
