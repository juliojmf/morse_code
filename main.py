letter_to_morse = {'A': '._', 'B': '_...', 'C': '_._.', 'D': '_..', 'E': '.', 'F': '.._.', 'G': '__.', 'H': '....', 'I': '..',
       'J': '.___', 'K': '_._', 'L': '._..', 'M': '__', 'N': '_.', 'O': '___', 'P': '.__.', 'Q': '__._', 'R': '._.',
       'S': '...', 'T': '_', 'U': '.._', 'V': '..._', 'W': '.__', 'X': '_.._', 'Z': '__..', ' ': '   '}

on = True
morse_to_letter = {code: letter for letter, code in letter_to_morse.items()}
morse_to_letter.update({"/": " "})
choice = input("Digite:\n"
               "1, para traduzir para código morse\n"
               "2, para taduzir a partir de código morse\n"
               "quit para sair\n")
while on:
    if choice == "1":
        word = input("\nO que deseja traduzir para código morse?\n").upper()
        if word == "QUIT":
            break
        output = [letter_to_morse[letter] for letter in word]
        for code in output:
            print(f"{code} ", end="")
    elif choice == "2":
        morse = input("\nDigite o código usando espaço simples para separar cada letra de código e / para separar palavras:\n").split()
        if "quit" in morse:
            break
        output = [morse_to_letter[code] for code in morse]
        for letter in output:
            print(f"{letter}", end="")
    elif choice == "quit":
        break
    else:
        print("Entrada inválida")
        break