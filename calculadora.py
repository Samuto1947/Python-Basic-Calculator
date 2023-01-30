while True:    
    pergunta = input("Bem vindo a calculadora, escolha qual operação deseja fazer!\n1. Soma\n2. Subtração\n3. Multiplicação\n4. Divisão\n5. Saída\nSua escolha: ")
    print('==============================================')
    if pergunta == '1':
        n1 = float(input("Escolha um número: "))
        n2 = float(input("Escolha um segundo número: "))
        s = n1 + n2
        print('==============================================')
        print(f'A soma entre {n1} e {n2} resulta em: {s}\nFim do uso!')
        print('==============================================')

    elif pergunta == '2':
        n1 = float(input("Escolha um número: "))
        n2 = float(input("Escolha um segundo número: "))
        s = n1 - n2
        print('==============================================')
        print(f'A subtração entre {n1} e {n2} resulta em: {s}\nFim do uso!')
        print('==============================================')
    
    elif pergunta == '3':
        n1 = float(input("Escolha um número: "))
        n2 = float(input("Escolha um segundo número: "))
        s = n1 * n2
        print('==============================================')
        print(f'A multiplicação entre {n1} e {n2} resulta em: {s}\nFim do uso!')
        print('==============================================')
    
    elif pergunta == '4':
        n1 = float(input("Escolha um número: "))
        n2 = float(input("Escolha um segundo número: "))
        s = n1 / n2
        print('==============================================')
        print(f'A divisão entre {n1} e {n2} resulta em: {s}\nFim do uso!')
        print('==============================================')
    
    elif pergunta == '5':
        print('Você optou por sair.\nObrigado por utilizar a calculadora!')
        break
    
    else:
        print("Escolha uma opção válida.")
        print('==============================================')


    pergunta2 = input('Deseja fazer outro calculo?\n1. Usar novamente\n2. Sair da calculadora\nSua escolha: ')
   
    if pergunta2 == '1':
        print('==============================================')
        print('Ok, use novamente!')
        print('==============================================')
    elif pergunta2 == '2':
        print('==============================================')
        print('Você optou por sair.\nObrigado por utilizar a calculadora!')
        break
