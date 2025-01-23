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
    



def criar_usuario(usuarios):
    cpf = input("Informe o cpf (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Já existe usuário com este CPF!!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento: [dd-mm-aaaa]")
    endereco = input("Informe o endereço: [logradouro, nro - bairro - cidade/sigla estado]")

    usuarios.append({"nome": nome, "data_nasciemnto": data_nascimento, "endereco": endereco, "cpf": cpf})

    print("Usuário criado com sucesso!!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Conta criada com sucesso!!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("Usuário não encontrado, fluxo de criação de conta encerrado!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta["agencia"]}
            C/C:\t\t{conta["numero_conta"]}
            Titular:\t{conta["usuario"]["nome"]}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def sacar(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):
    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("\nOperação falhou, você não tem saldo sufuciente.")

    elif excedeu_limite:
        print("\nOperação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("\nOperação falhou! Número maximo de saques excedido.")
    
    elif valor < saldo:
       saldo -= valor
       numero_saques += 1
       extrato += f"Saque: R$ {valor:.2f}\n"
       print(f"Saque de R${valor:.2f} realizado com sucesso! Saldo atual: R${saldo:.2f}")    
    
    else:
        print("Operação falhou! O valor informado é invalido.")
    
    return saldo, extrato, numero_saques


def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("\n++Depósito realizado com sucesso!! ++")
    else:
        print("Operação falhou! O valor informado é invalido.")

    return saldo, extrato


def extratos(saldo, /, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

    
def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    contas = []
    usuarios = []


    while True:

        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)


        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques =  sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES)

        elif opcao == "e":
            extratos(saldo, extrato=extrato)

        elif opcao == "a":
            nome = input("Digite o nome do cliente: ")
            data_nascimento = input("Digite a data de nascimento: [XX/XX/XXXX]")
            cpf = input("Digite o cpf do cliente: ")
            endereco = input("Digite o endereço do Cliente: ")
            adicionar_cliente(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação invalida, por favor selecione novamente a operação desejada.")


main()




