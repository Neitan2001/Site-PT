from time import sleep
sleep(0)
from os import system
system('clear')
c= 0
o= 5



while o !=4  :
    
    print('Gasparzinho Lanches- Carpazinha, RS')
    print('''
    [1]Comida
    [2]Bebidas
    [3]Valor da Conta
    [4]Fechar Pedido''')
    o= int(input('Qual a sua opção?:'))
    sleep(1)
    system('clear')
    
    

    if o==1 :
        o1=0
        while o1 !=4:
            print('''  
            [1]Cacetinho do Letício- 5 reais
            [2]Doce de maracujá- 2 reais
            [3]Doce de leite- 2 reais
            [4]Voltar''')
            o1= int(input('Qual a sua opção?:'))
            if o1== 1:
                c+=5
                print('Adicionado um Cacetinho ao carrinho')
                sleep(1)
                system('clear')
            elif o1== 2:
                c+=2
                print('Adicionando um Doce de maracujá ao carrinho')
                sleep(1)
                system('clear')
            elif o1==3:
                c+=2
                print('Adicionado um Doce de leite ao carrinho')
                sleep(1)
                system('clear')
            elif o1== 4:
                print('Volando...')
                sleep(1)
                system('clear')
            else:
                print('Opção inválida, tente novamente')
                sleep(1)
                system('clear')
    if o==2 :
        o2=0
        while o2 != 4:
            print('''
            [1]Suco de Bergamota- 10 reais
            [2]Suco de Laranja- 10 reais
            [3]Suco de Abacaxi- 10 reais
            [4]Voltar''')
            o2=int(input('Qual a sua opção?:'))
            if o2== 1:
                c+=10
                print('Adicionado um Suco de Bergamota ao carrinho')
                sleep(1)
                system('clear')
            elif o2== 2:
                c+=10
                print('Adicionando um Suco de Laranja ao carrinho')
                sleep(1)
                system('clear')
            elif o2==3:
                c+=10
                print('Adicionado um Suco de Abacaxi ao carrinho')
                sleep(1)
                system('clear')
            elif o2== 4:
                print('Volando...')
                sleep(1)
                system('clear')
            else:
                print('Opção inválida, tente novamente')
                sleep(2)
                system('clear')
    if o==3:
        print('O valor da conta é:{} reais'.format(c))
        sleep(2)
        system('clear')
print("Pedido Fechado, Volte sempre")
        

        


