def SayHello(name):
    if name:
        print("Hello " + name)
    else:
        name = raw_input("Vous n'avez pas saisi le nom, merci d'en saisir un: ")
        SayHello(name)

SayHello("")
