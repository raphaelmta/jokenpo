import random

def jogo():

    def menu():
        print('Bem Vindo ao JOKENPO!!!')
        print('Regras do jogo: ')
        print('- Pedra ganha de tesoura, mas perde para papel.\n- Pedra ganha de tesoura, mas perde para papel.\n- Tesoura ganha de papel, mas perde para pedra.\n- Papel ganha de pedra, mas perde para tesoura.\n- Caso o jogador e o computador façam a mesma escolha, declare um empate. ') 

    menu()

    def escolhas_possiveis():
        print('\n 1 - Pedra\n 2 - Papel\n 3 - Tesoura')

    escolhas_possiveis()

    escolha = input('Faça sua escolha: ')
    def escolha_jogador(escolha):
        escolhas = ['Pedra', 'Papel', 'Tesoura']
        if escolha in escolhas:     
            return escolha 
        else:
            print('Escolha Invalida\nEscolha de novo')

    escolha_jogador(escolha)
    print(f'sua escolha foi {escolha}')

    opcao = ['Pedra', 'Papel', 'Tesoura']
    escolha_maquina = random.choice(opcao)

    print(f'sua escolha foi{escolha}')
    print(f'Minha escolha foi {escolha_maquina}')

    if escolha == escolha_maquina:
        print('Empate')
    elif escolha != escolha_maquina:
        if escolha == 'Pedra' and escolha_maquina == 'Tesoura':
            print('Vitória sua!')
        elif escolha == 'Tesoura' and escolha_maquina == 'Papel':
            print('Vitória Sua!')
        elif escolha == 'Papel' and escolha_maquina == 'Pedra':
            print('Vitória sua!')
        else:
            print('Vitória Minha!')
    reiniciar_programa()

def reiniciar_programa():
    resposta = input("Deseja jogar Jokenpo? (S/N): ").strip().upper()
    if resposta == "S":
        jogo()
    elif resposta == 'N':
        print("Encerrando. Até logo!")
    else:
        print('Escolha Inválida')
        reiniciar_programa()

reiniciar_programa()
    