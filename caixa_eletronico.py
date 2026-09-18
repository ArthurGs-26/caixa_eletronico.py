# caixa_eletronico.py
senha_correta = '1234'
tentativas = 3

while tentativas > 0:
    digitar_senha = input('Digite sua senha: ')

    if digitar_senha == senha_correta:
        print('Acesso permitido! Bem vindo.')
        break
    else:
        tentativas -= 1
        print(f'Senha incorreta. Você ainda tem {tentativas} tentativas(s).')

if tentativas == 0:
    print('Conta bloqueada por excesso de tentativas')

opcao = ''
saldo = 5000.00
extrato = []

while opcao != '5':
    print('Menu Principal')
    print('1. Consultar Saldo')
    print('2. Depositar dinheiro')
    print('3. Sacar dinheiro')
    print('4. Mostrar extrato')
    print('5. Sair')

    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        print(f'O seu saldo atual é de R$ {saldo:.2f}')
    elif opcao == '2':
        valor_depositar = float(input('Digite o valor que quer depositar: '))
        if valor_depositar > 0:
            saldo += valor_depositar
            print(f'Depósito realizado com sucesso! Novo saldo: R$ {saldo:.2f}')
            extrato.append(f'Depósito: R$ {valor_depositar:.2f}')
        else: 
            print('Depósito inválido!')
    elif opcao == '3':
        valor_sacar = float(input('Digite o valor que quer sacar: '))
        if valor_sacar > 0 and valor_sacar <= saldo:
            saldo -= valor_sacar
            print(f'Saque realizado com sucesso! Novo saldo: R$ {saldo:.2f}')
            extrato.append(f'Saque: R$ {valor_sacar:.2f}')
        else:
            print('Saque inválido!')
    elif opcao == '4':
        print('---Extrato Bancário---')
        if not extrato:
            print('Não foram realizadas movimentações.')
        else:
            for operacao in extrato:
                print(operacao)
        print(f'Saldo atual: R$ {saldo:.2f}')
        print('----------------------')
    elif opcao == '5':
        print('Obrigado por utilizar o nosso caixa eletrônico!')
    else:
        print('Opção inválida')
