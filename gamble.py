#biblioteca RANDOM para aleatoriedade
import random

figuras = ["💎","🪙","👑"]

print(figuras,"\n")

def gamble():
    figuras_choice = []

    resposta = input("deseja apostar? vc parece um cara de sorte (s/n) ")

    match(resposta.lower()):
        case "s":
            for _ in figuras:
                figuras_choice.append(random.choice(figuras))

            contagem = set(figuras_choice)
            mensagem = ""

            if len(contagem) == 3:
                mensagem = "nao foi dessa vez! tente novamente! \n"

                print(figuras_choice, "\n" , mensagem)
            elif len(contagem) == 2:
                mensagem = "quase! voce esta com sorte! \n"
            else:
                mensagem = "tirou a sorte grande! \n"
            
            #bloco doq vai pro terminal
            print(figuras_choice, "\n" , mensagem)
            
            resposta = input("deseja jogar novamente?(s/n) ")

            if resposta == "s":
                gamble()
            else:
                print("fim do programa\n")

        case "n":
            print("fim do programa\n")
        case _:
            print("digite uma resposta valida!\n")
            gamble()
gamble()