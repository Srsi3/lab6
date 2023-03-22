def encoder(word):
    thing = ''
    for i in word:
        if int(i) < 7:
            thing += str(int(i)+3)
        else:
            if i == '8':
                thing += '1'
            elif i == '7':
                thing += '0'
            elif i == '9':
                thing += '2'
    return thing
    pass
def decoder(word):
    bruh = ''
    return bruh
    pass
if __name__  == '__main__':
    while True:
        print("Menu\n---------\n0. Exit\n1. Encode\n2. Decode")
        choice = int(input("Choose an option: "))
        if choice == 1:
            print(f"The Encoded password is "+encoder(input("Password to Encode:")))

        elif choice == 2:
            print(f"The Decoded password is "+decoder(input("Password to Decode:")))

        elif choice == 0:
            break

