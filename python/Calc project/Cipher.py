def cipher():

    r = float(input('Enter r\n'))
    x = int(input('Enter initial value for x\n'))

    x = r*x*(1-x)
    print(x)

    word = str(input('Enter message to be encrypted\n'))

    for letter in word:
        letter = ord(letter)
        letter = letter + int(x)
        print(letter)
        encrypted = ''.join(letter if c.isalpha() else c for c in word)

    print("Encrypted word is :", encrypted)

cipher()

