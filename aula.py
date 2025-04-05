
import random

def jogar_partida():
    separador = ('-' * 80)

    def escolhas_possiveis():
        print('\n 1 - Pedra\n 2 - Papel\n 3 - Tesoura')

    escolhas_possiveis()

    escolha = input('Faça sua escolha: ').upper()
    print('-' * 80)
    
    def escolha_jogador(escolha):
        while True:
            escolhas = ['PEDRA', 'PAPEL', 'TESOURA']
            if escolha in escolhas:     
                return escolha
            elif escolha not in escolhas:
                escolha = input('Escolha Invalida\nEscolha de novo: ').upper()
                continue
            else:
                break
            
    escolha = escolha_jogador(escolha)
    print ('Boa Sorte!!!')
    print('-' * 80)
    

    opcao = ['Pedra', 'Papel', 'Tesoura']
    escolha_maquina = random.choice(opcao).upper()

    print(f'Sua escolha foi -{escolha}-')
    print('-' * 80)
    print(f'Minha escolha foi -{escolha_maquina}-')
    print('-' * 80)

    empate = 'Empate'
    vitoria_sua = 'Vitória Sua'
    vitoria_minha = 'Vitória minha'
    
    resultado = ""
    if escolha == escolha_maquina:
        resultado = empate
    elif escolha != escolha_maquina:
        if escolha == 'PEDRA' and escolha_maquina == 'TESOURA':
            resultado = vitoria_sua
        elif escolha == 'TESOURA' and escolha_maquina == 'PAPEL':
            resultado = vitoria_sua
        elif escolha == 'PAPEL' and escolha_maquina == 'PEDRA':
            resultado = vitoria_sua
        else:
            resultado = vitoria_minha
    
    print(resultado)
    print('-' * 80)
    
    return resultado

def reiniciar_programa():
    resposta = input("Deseja jogar Jokenpo? (S/N): ").strip().upper()
    print('-' * 80)
    if resposta == "S":
        jogar_partida()
    elif resposta == 'N':
        print("Encerrando. Até logo!")
    else:
        print('Escolha Inválida')
        reiniciar_programa()


def criar_placar():
    return {"Jogador": 0, "Computador": 0}

def atualizar_placar(placar, resultado):
    if resultado == "Vitória Sua":
        placar["Jogador"] += 1
    elif resultado == "Vitória minha":
        placar["Computador"] += 1
    return placar

def exibir_placar(placar):
    print('-' * 80)
    print(f"PLACAR ATUAL:")
    print(f"Jogador: {placar['Jogador']} | Computador: {placar['Computador']}")
    print('-' * 80)

def melhor_de_tres():
    print("MODO MELHOR DE TRÊS")
    print('-' * 80)
    
    placar = criar_placar()
    partidas_jogadas = 0
    
    while partidas_jogadas < 3 and placar["Jogador"] < 2 and placar["Computador"] < 2:
        print(f"Partida {partidas_jogadas + 1}")
        resultado = jogar_partida()
        placar = atualizar_placar(placar, resultado)
        exibir_placar(placar)
        
        partidas_jogadas += 1
    
    if placar["Jogador"] > placar["Computador"]:
        print("Você venceu o melhor de três!")
    elif placar["Computador"] > placar["Jogador"]:
        print("Eu venci o melhor de três!")
    else:
        print("O melhor de três terminou em empate!")
    
    print('-' * 80)
    reiniciar_programa()

    


def tipo_de_jogo():
    escolha = input('Escolha o tipo de jogo:\n digite (1) para partidas isoladas\n digite (2) para melhor de três\n')
    print('-' * 80)
    if escolha == '1':
        placar = criar_placar()
        while True:
            resultado = jogar_partida()
            placar = atualizar_placar(placar, resultado)
            exibir_placar(placar)
            
            continuar = input("Deseja jogar novamente? (S/N): ").strip().upper()
            if continuar != "S":
                break
    else: 
        melhor_de_tres()


tipo_de_jogo()
