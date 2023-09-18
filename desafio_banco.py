menu = '''
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

==>  '''

saldo = 0.0
limite = 500.0
numero_saques = 0
limite_saques = 3
valores_sacados = []  # Lista vazia para armazenar os valores sacados

while True:
    opcao = input(menu)

    if opcao == 'd':
        valor_deposito = float(input('Valor do deposito: '))
        if valor_deposito < 0:
            print('POR FAVOR CORRIJA O VALOR')
        else:
            saldo += valor_deposito
            print(f'Depósito Realizado com sucesso. Seu saldo é de : R${saldo:.2f}')

    elif opcao == 's':
        if saldo <= 0.0:
            print('Você não tem saldo')
        else:
            valor_saque = float(input('Valor que quer sacar: R$ '))
            if valor_saque > limite:
                print('Saque não permitido. Valor máximo de saque é de R$500')
            elif valor_saque > 0 and valor_saque <= limite:
                if numero_saques < limite_saques:
                    if saldo >= valor_saque:
                        saldo -= valor_saque
                        numero_saques += 1
                        valores_sacados += [valor_saque]
                        print(f'Saque de R${valor_saque:.2f} realizado com sucesso!')
                        print(f'Seu saldo atual é de R${saldo:.2f}')
                    else:
                        print('Saldo insuficiente para realizar o saque.')
                else:
                    print('Você não pode sacar mais hoje')

    elif opcao == 'e':
        print(f'Saldo atual: R${saldo:.2f}')
        print(f'Número de saques hoje: {numero_saques}')
        print('Valores sacados: ', valores_sacados)

    elif opcao == 'q':
        print('Obrigado! Tenha um bom dia!')
        break

    else:
        print('Opção inválida, por favor, selecione novamente a opção desejada.')
