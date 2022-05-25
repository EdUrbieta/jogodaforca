import random
from frutas import frutasList
from paises import paisesList
from linguas import linguasLista

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
    print('#'.ljust(15), '[F] Frutas'.center(15), '#'.rjust(23))
    print('#'.ljust(15), '[P] Países da Europa'.center(15), '#'.rjust(25))
    print('#'.ljust(15), '[L] Línguas Neolatinas'.center(15), '#'.rjust(24))
    print('#'.ljust(15), '[S] SAIR DO JOGO'.center(5), '#'.rjust(29))
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


def obter_palavra():
    global listaSelecionada
    categoria = str(input("Vamos selecionar uma categoria!" '''
                    [F] FRUTAS
                    [P] PAÍSES DA EUROPA
                    [L] LÍNGUAS NEOLATINAS
                    [S] SAIR DO JOGO:\n'''))

    if categoria.upper() == 'F':
        listaSelecionada = frutasList
    elif categoria.upper() == 'P':
        listaSelecionada = paisesList
    elif categoria.upper() == 'L':
        listaSelecionada = linguasLista
    elif categoria.upper() == 'S':
        print("Opção Escolhida: SAIR DO JOGO")
        exit()
    else:
        categoria = input("Vamos selecionar uma categoria!" '''
                    [F] FRUTAS
                    [P] PAÍSES DA EUROPA
                    [L] LÍNGUAS NEOLATINAS
                    [S] SAIR DO JOGO:\n''')

    palavra = random.choice(listaSelecionada)
    return palavra.upper()


def jogar(palavra):
    para_completar = "_" * len(palavra)
    adivinhado = False
    letras_adv = []
    palavras_adv = []
    tentativas = 6
    print("Vamos jogar!")
    print(forca_display(tentativas))
    print(para_completar)
    print("\n")

    while not adivinhado and tentativas > 0:
        adv = input("Por favor tente adivinhar!: ").upper()
        if len(adv) == 1 and adv.isalpha():
            if adv in letras_adv:
                print("Você já adivinhou essa letra!", adv)
            elif adv not in palavra:
                print(adv, "Não está na palavra!")
                tentativas -= 1
                letras_adv.append(adv)
            else:
                print("Bom trabalho!", adv, "é a palavra!")
                letras_adv.append(adv)
                plv_lista = list(para_completar)
                indices = [i for i, letra in enumerate(palavra) if letra == adv]
                for index in indices:
                    plv_lista[index] = adv
                para_completar = ''.join(plv_lista)
                if "_" not in para_completar:
                    adivinhado = True
        elif len(adv) == len(palavra) and adv.isalpha():
            if adv in palavras_adv:
                print("Você já adivinhou esta palavra!", adv)
            elif adv != palavra:
                print(adv, "não é a palavra!")
                tentativas -= 1
                palavras_adv.append(adv)
            else:
                adivinhado = True
                para_completar = palavra
        else:
            print("Por favor insira um valor válido!")
        print(forca_display(tentativas))
        print(para_completar)
        print("\n")
    if adivinhado:
        print("Você é bom mesmo em menino! Adivinhou a palavra!", palavra)
    else:
        print("Iih... Foi bom não em, a palavra era: ", palavra)


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
    palavra = obter_palavra()
    jogar(palavra)
    while input("Quer jogar de novo? (S/N): ").upper() == 'S':
        palavra = obter_palavra()
        jogar(palavra)


if __name__ == "__main__":
    main()
