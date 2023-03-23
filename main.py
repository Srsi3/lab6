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
def decoder():
    bruh = ''
    return bruh
    pass
if __name__  == '__main__':
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        choice = int(input("Please enter an option: "))
        if choice == 1:
            origi = encoder(input("Please enter your password to encode: "))
            print("Your password has been encoded and stored!")
        elif choice == 2:
            print(f"The encoded password is {origi}, and the original password is {decoder(origi)}.")
        elif choice == 3:
            break
