
def jogar_forca():
    print("*********************************")
    print("Bem vindo ao Jogo da Forca!")
    print("*********************************")

    palavra_secreta = "maca".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    #enquanto não enforcou E não acertou
    while(not enforcou and not acertou):


        chute = input("Qual letra?")
        chute = chute.strip().upper()


        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

    if(acertou):
        print("Você ganhou!")
    else:
        print("Você perdeu!")

if(__name__ == "__main__"):
    jogar_forca()