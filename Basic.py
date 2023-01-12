def calculator():

    num1 = float(input("Entrez le premier nombre: "))

    num2 = float(input("Entrez le deuxième nombre: "))

    operator = input("Entrez l'opérateur (+, -, *, /): ")

    if operator == "+":

        result = num1 + num2

    elif operator == "-":

        result = num1 - num2

    elif operator == "*":

        result = num1 * num2

    elif operator == "/":

        result = num1 / num2

    else:

        print("Opérateur non valide. Veuillez entrer un opérateur valide.")

        return

    print("Le résultat est: ", result)

calculator()

