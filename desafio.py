def depositar(saldo,valor,extrato):
    saldo+=valor
    extrato+=f"Depósito: {saldo:.2f}\n"
    print("Depósito realizado com sucesso!")
    return saldo,extrato

def saque(valor,saldo,extrato,numero_saques):
    if saldo<valor: print("Operação falhou! Saldo insuficiente para reaizar saque!")
    elif numero_saques>=3: print("Operação falhou! Número máximo de saques excedido!")#3 é o numero maximo de saques
    elif valor>500: print("Operação falhou! Limite de valor de saque excedidido!") #500 é o número limite
    elif saldo>valor:
        saldo-=valor
        extrato+=f"Saque: {valor:.2f}\n"
        numero_saques+=1
        print("Saque realizado com sucesso!")
    else:  print("Operação falhou! O valor informado é inválido.")
    return saldo,extrato,numero_saques

def mostra_extrato(saldo,extrato):
    print("====Extrato====")
    print('Não foram realizadas movimentações.' if not extrato else extrato)#se extrato estiver vazio
    #ou falso a mensagem sera impressa, se tiver algo ou for vdd sera impresso o que esta na variavel
    print(f'Saldo: R$: {saldo:.2f}')
    #print(f'\nSaldo: \t\ R$ {saldo:.2f}')
    print('===================')

def novo_usuario(usuarios):
    cpf=input('Digite o cpf: ')
    usuario=filtro_novo_usuario(cpf,usuarios)

    if usuario:
        print('Usuário já existente.')
        return
    nome=input('Informe o nome completo: ')
    data_nasc=input('Informe a data de nascimento (dd-mm-aaaa):')
    endereco=input('Informe o endereço: ')

    usuarios.append({'nome':nome,'data_nasc':data_nasc,'cpf':cpf,'endereço':endereco})

    print('Usuário criado com sucesso! ')
    
def filtro_novo_usuario(cpf,usuarios):
        for usuario in usuarios:
            if usuario['cpf'] == cpf:
                return True
        return False

def criar_conta(agencia,numero_conta,usuarios,contas):
    cpf = input("Digite o cpf: ")
    usuario = filtro_conta(cpf,usuarios)

    if usuario:
        conta_existente=False
        if len(contas)>0:
            for conta in contas:
                if conta['usuario']['cpf']==cpf: 
                    print("Conta já existente!")
                    conta_existente=True
                    break
                
        if not conta_existente:
            print("Conta criada com sucesso!")
            return {'agencia':agencia,'numero_conta':numero_conta,'usuario':usuario}
    else:
        print('\nUsuário não encontrado, fluxo de criação de conta encerrado!')
        return None

def filtro_conta(cpf,usuarios):
   for usuario in usuarios:
       if usuario['cpf']==cpf:
           return usuario
    
def listar_contas(contas):
    for conta in contas:
        linha=f'''\
            agencia:\t{conta['agencia']}
            C\C:\t\t{conta['numero_conta']}
            titular:\t{conta['usuario']['nome']}
        '''
        print('='*100)
        print(linha)

def menu():
    print('[d] Depositar')
    print('[s] Sacar')
    print('[e] Extrato')
    print('[q] Sair')
    print('[nc] Nova conta')
    print('[lc] Listar contas')
    print('[nu] Novo usuário')
    print('[q] Sair')
    return str(input('Opção: '))

AGENCIA='0001'

saldo = 0
extrato = ""
usuarios=[]
numero_saques = 0
contas=[]

while True:
    opc=menu()
    if opc=="d":
        valor = float(input("Informe o valor do depósito: "))
        saldo,extrato=depositar(saldo,valor,extrato)
    
    elif opc=="s":
        valor=float(input('Informe o valor do saque: '))
        saldo,extrato,numero_saques=saque(valor,saldo,extrato,numero_saques)
    
    elif opc=='e':
        mostra_extrato(saldo,extrato)

    elif opc=='nu':
        novo_usuario(usuarios)

    elif opc=="nc":
        numero_conta=len(contas)+1
        conta=criar_conta(AGENCIA,numero_conta,usuarios,contas)

        if conta:
            contas.append(conta)

    elif opc=="lc":
        listar_contas(contas)
    
    elif opc == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")