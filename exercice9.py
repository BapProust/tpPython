# Ecrire un script permettant de faire une calculatrice console

def exercice9():
    while True:
        operation = input("Entrez une opération: ")
        operandes = ["+", "-", "/", "*"]

        if operation == "q":
            break

        for s in operandes:
            if operation.split(s):
                var = operation.split(s)
                if len(var) > 1:
                    try:
                        if s == "+":
                            result = float(var[0]) + float(var[1])
                            print(result)
                        elif s == "-":
                            result = float(var[0]) - float(var[1])
                            print(result)
                        elif s == "/":
                            result = float(var[0]) / float(var[1])
                            print(result)
                        elif s == "*":
                            result = float(var[0]) * float(var[1])
                            print(result)
                    except:
                        continue


exercice9()
