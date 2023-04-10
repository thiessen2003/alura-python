
def jogar_forca():
    print("*********************************")
    print("Bem vindo ao Jogo da Forca!")
    print("*********************************")

    palavra_secreta = "banana"

    enforcou = False
    acertou = False

    #enquanto não enforcou E não acertou
    while(not enforcou and not acertou):

        index = 0
        chute = input("Qual letra?")

        chute = chute.strip()

        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
              print(f"Encontrei a letra {chute} na posição {index}")
            index += 1

        print("jogando.........")

if(__name__ == "__main__"):
    jogar_forca()