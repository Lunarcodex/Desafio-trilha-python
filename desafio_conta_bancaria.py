menu = """

[c] Criar Usuário
[cc] Criar Conta
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """



def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}"
        print("\n Operação concluída com sucesso!\n")
    elif valor <0:
        print("Operação falhou! O valor informado é inválido.")
    return saldo,extrato

def sacar(*,saldo,valor,extrato,limite ,numero_saques,LIMITE_SAQUES):
    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
       saldo -= valor
       extrato += f"Saque: R$ {valor:.2f}"
       numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo,extrato

def exibir_extrato(saldo,/,*, extrato):
    print("EXTRATO".center(42,"="))
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("="*42)
    return saldo,extrato

def filtrar_usuario(cpf,usuario):
   for usuario in usuario:
       if usuario["cpf"] ==cpf:
        return usuario
   return None

def criar_conta(agencia,numero_da_conta,usuario):
    cpf = input("Por favor, informe o CPF cadastrado\n")

    if filtrar_usuario(cpf, usuario):
        print("Conta criada com sucesso")
        return {"agencia": agencia, "numero_da_conta": numero_da_conta, "usuario": usuario }
    
    print("Usuário não encontrado, por favor tente novmente")


def criar_usuario(usuarios):
    cpf = input("Por favor, informe somente os números de seu CPF\n")
    

    if filtrar_usuario(cpf, usuarios):
        print("Esse CPF já está cadastrado")
        return 
    
    nome = input("Por favor, isira seu nome completo\n")
    data_de_nascimento = input("Por favor, insira a sua data de nascimento no formato dd-mm-aa\n")
    endereco = input("Por favor, informe seu endereço da seguinte maneira, logradouro, n°, bairro, cidade/sigla do estado\n")
    usuarios.append({'nome': nome, 'data_de_nascimento':data_de_nascimento, 'cpf': cpf, 'endereco': endereco})
    print('Usuário cadastrado com sucesso')


saldo = 0
limite = 500
extrato = ""
numero_saques = 0
usuario = []
contas = []
numero_da_conta = 0
LIMITE_SAQUES = 3
AGENCIA = "0001"

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = depositar(valor,saldo,extrato)
        deposito = depositar(saldo,valor,extrato)
        print(deposito)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saque = sacar(saldo=saldo,
                      valor=valor,
                      extrato=extrato,
                      limite=limite,
                      numero_saques=numero_saques,
                      LIMITE_SAQUES=LIMITE_SAQUES)
        print(saque)

    elif opcao == "e":
        exibir_extrato(saldo, extrato=extrato)
        extrato = exibir_extrato(saldo, extrato=extrato)
        print(extrato)

    elif opcao == "c":
        criar_usuario(usuario)
        print(criar_usuario)

    elif opcao == "cc":
        numero_da_conta = numero_da_conta + 1
        conta = criar_conta(AGENCIA, numero_da_conta, usuario)
        if conta:
            contas.append(conta)
   
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")