import textwrap
#Funções
def menu():
    menu = """\n
    ===============MENU===============
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNovo Usuário
    [q]\tSair
    ==>"""
    return input(textwrap.dedent(menu))
    



def adicionar_cliente(nome, data_nascimento, cpf, endereco):
    novo_cliente = {
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco
    }
    clientes.append(novo_cliente)
    print(f"Cliente {novo_cliente['nome']} adicionado com sucesso!")


def sacar(saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):
    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou, você não tem saldo sufuciente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número maximo de saques excedido.")
    
    elif valor < saldo:
       saldo -= valor
       numero_saques += 1
       extrato += f"Saque: R$ {valor:.2f}\n"
       print(f"Saque de R${valor:.2f} realizado com sucesso! Saldo atual: R${saldo:.2f}")    
    
    else:
        print("Operação falhou! O valor informado é invalido.")
    
    return saldo, extrato


def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é invalido.")

    return saldo, extrato


def extratos(saldo, /, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

    
def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    clientes = []


    while True:

        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)


        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato =  sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES)

        elif opcao == "e":
            extratos(saldo, extrato=extrato)

        elif opcao == "a":
            nome = input("Digite o nome do cliente: ")
            data_nascimento = input("Digite a data de nascimento: [XX/XX/XXXX]")
            cpf = input("Digite o cpf do cliente: ")
            endereco = input("Digite o endereço do Cliente: ")
            adicionar_cliente(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)


        elif opcao == "q":
            break

        else:
            print("Operação invalida, por favor selecione novamente a operação desejada.")


main()




