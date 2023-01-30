#Inicia o laço de repetição.
while True:
    #Pergunta inicial para saber qual operação irá fazer    
    pergunta = input("Bem vindo a calculadora, escolha qual operação deseja fazer!\n1. Soma\n2. Subtração\n3. Multiplicação\n4. Divisão\n5. Saída\nSua escolha: ")
    print('==============================================') # Daqui em diante usado no código por estética
    
    #Caso escolher a operação de soma +
    if pergunta == '1':
        n1 = float(input("Escolha um número: "))
        n2 = float(input("Escolha um segundo número: "))
        s = n1 + n2
        print('==============================================')
        print(f'A soma entre {n1} e {n2} resulta em: {s}\nFim do uso!')
        print('==============================================')

    #Caso escolher a operação de subtração -
    elif pergunta == '2':
        n1 = float(input("Escolha um número: "))
        n2 = float(input("Escolha um segundo número: "))
        s = n1 - n2
        print('==============================================')
        print(f'A subtração entre {n1} e {n2} resulta em: {s}\nFim do uso!')
        print('==============================================')
    
    #Caso escolher a operação de multiplicação *
    elif pergunta == '3':
        n1 = float(input("Escolha um número: "))
        n2 = float(input("Escolha um segundo número: "))
        s = n1 * n2
        print('==============================================')
        print(f'A multiplicação entre {n1} e {n2} resulta em: {s}\nFim do uso!')
        print('==============================================')

    #Caso escolher a operação de divisão /
    elif pergunta == '4':
        n1 = float(input("Escolha um número: "))
        n2 = float(input("Escolha um segundo número: "))
        s = n1 / n2
        print('==============================================')
        print(f'A divisão entre {n1} e {n2} resulta em: {s}\nFim do uso!')
        print('==============================================')
    
    #Caso optar por sair logo no início
    elif pergunta == '5':
        print('Você optou por sair.\nObrigado por utilizar a calculadora!')
        break
    
    #Caso escrever uma opção inválida como "6" ou "SNFOA"
    else:
        print("Escolha uma opção válida.")
        print('==============================================')

    #Pergunta caso quiser fazer outra operação após finalizar a sua operação atual.
    pergunta2 = input('Deseja fazer outro calculo?\n1. Usar novamente\n2. Sair da calculadora\nSua escolha: ')
   
    #Caso escolher fazer outra operação
    if pergunta2 == '1':
        print('==============================================')
        print('Ok, use novamente!')
        print('==============================================')

    #Caso escolher encerrar a calculadora após operação    
    elif pergunta2 == '2':
        print('==============================================')
        print('Você optou por sair.\nObrigado por utilizar a calculadora!')
        break
