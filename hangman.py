import random

nome = str(input('INFORME SEU NOME: ')).upper().strip()

def menu():
    print('>' * 20, 'UNIESP'.center(20), '<' * 20)
    print('#'.ljust(15), 'INTRODUÇÃO À PROGRAMAÇÃO'.center(30), '#'.rjust(15))
    print('#'.ljust(15), ' '.center(30), '#'.rjust(15))
    print('#'.ljust(15), 'BEM-VINDO(A) AO JOGO DA FORCA,'.center(30), '#'.rjust(15))
    print('#'.ljust(15), '{}'.format(nome).center(30), '#'.rjust(15))
    print('#'.ljust(15), ' '.center(30), '#'.rjust(15))
    print('#'.ljust(15), 'MENU DE CATEGORIAS'.center(30), '#'.rjust(15))
    print('#'.ljust(15), ' '.center(30), '#'.rjust(15))
    print('#'.ljust(15), '[1] Frutas'.center(15), '#'.rjust(23))
    print('#'.ljust(15), '[2] Países da Europa'.center(15), '#'.rjust(25))
    print('#'.ljust(15), '[3] Línguas Neolatinas'.center(15), '#'.rjust(24))
    print('#'.ljust(15), '[0] SAIR DO JOGO'.center(5), '#'.rjust(29))
    print('#'.ljust(15), ' '.center(30), '#'.rjust(15))
    print('#'.ljust(3), 'Grupo:', '#'.rjust(51))
    print('#'.ljust(3), 'Brunno Medeiros - 2022111510029@iesp.edu.br', '#'.rjust(14))
    print('#'.ljust(3), 'Camylla Neves - 2022111510089@iesp.edu.br', '#'.rjust(16))
    print('#'.ljust(3), 'Eduardo Urbieta - 2022111510044@iesp.edu.br', '#'.rjust(14))
    print('#'.ljust(3), 'Gabriel Santana - 2022111510010@iesp.edu.br', '#'.rjust(14))
    print('#'.ljust(3), 'Ianny Mamedes - 2022111510025@iesp.edu.br', '#'.rjust(16))
    print('#'.ljust(15), ' '.center(30), '#'.rjust(15))
    print('#' * 62)
menu()
print()

tema = int(input("Vamos agora selecionar o tema que deseja jogar!: "))

if tema == 1:
    from frutas import frutasList
    listaSelecionada = frutasList
    print("Você selecionou a categoria FRUTAS!")
elif tema == 2:
    from paises import paisesList
    listaSelecionada = paisesList
    print("Você selecionou a categoria PAÍSES DA EUROPA!")
elif tema == 3:
    from linguas import linguasLista
    listaSelecionada = linguasLista
    print("Você selecionou a categoria LÍNGUAS NEOLATINAS!")
elif tema == '0':
    print('Opção Escolhida: SAIR DO JOGO')
    print('Jogo encerrando...')
    print('Jogo encerrado!')  # colocar temporizador
else:
    print('Opção Inválida. Tente outra vez!')
    print('''
                [1] FRUTAS
                [2] PAÍSES DA EUROPA
                [3] LÍNGUAS NEOLATINAS
                [0] SAIR DO JOGO''')

def obterpalavra():
    palavra = random.choice(listaSelecionada)
    return palavra.upper()

def jogar(palavra):
    compleicao_palavra = "_" * len(palavra)
    adivinhado = False
    letras_adivinhadas = []
    palavras_adivinhadas = []
    tentativas = 6
    print("Vamos jogar o Jogo da Forca!")
    print(forca_display(tentativas))
    print(compleicao_palavra)
    print("\n")
    while not adivinhado and tentativas > 0:
        adivinhar = input("Tente adivinhar uma letra ou a palavra! ").upper()
        if len(adivinhar) == 1 and adivinhar.isalpha():
            if adivinhar in letras_adivinhadas:
                print("Você já adivinhou esta letra! ", adivinhar)
            elif adivinhar not in letras_adivinhadas:
                print(adivinhar, "não está na palavra!")
                tentativas -= 1
                letras_adivinhadas.append(adivinhar)
            else:
                print("Boa!", adivinhar, "está na palavra!")
                letras_adivinhadas.append(adivinhar)
                palavra_como_lista = list(compleicao_palavra)
                indices = [i for i, letra in enumerate(palavra) if letra == adivinhar]
                for index in indices:
                    palavra_como_lista[index] = adivinhar
                compleicao_palavra = "".join(palavra_como_lista)
                if "_" not in compleicao_palavra:
                    adivinhado = True
        elif len(adivinhar) == len(palavra) and adivinhar.isalpha():
            if adivinhar in palavras_adivinhadas:
                print("Você já adivinhou a palavra!", adivinhar)
            elif adivinhar != palavra:
                print(adivinhar, "não é a palavra!")
                tentativas -= 1
                palavras_adivinhadas.append(adivinhar)
            else:
                adivinhado = True
                compleicao_palavra = palavra
        else:
            print("Erroooou!")
        print(forca_display(tentativas))
        print(compleicao_palavra)
        print("\n")
    if adivinhado:
        print("Parabéns mlk! Cê conseguiu em!")
    else:
        print("Parece que não deu não em... Complicado parça... Te contar que a palavra era: " + palavra)

def forca_display(tentativas):
    estagios = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return estagios[tentativas]

def main():
    palavra = obterpalavra()
    jogar(palavra)
    while input("Quer jogar de novo? (S/N) ").upper() == "S":
        palavra = obterpalavra()
        jogar(palavra)

if __name__ == "__main__":
    main()
