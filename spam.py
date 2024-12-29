from random import shuffle

liste = "amazing gorgeous blazing stunning tremendous greatest best fantastic phenomenal \
delightful ambitious exciting outstanding incredible spectacular super cool \
magical revolutionary intuitive beautiful jaw-dropping".upper().split()

# Die Elemente der Liste werden durchmischt
shuffle(liste)

for strophe in range(5):
    for n in range(2):
        for i in range(4):
            print("SPAM", end=" ")
        print()
    element1= liste.pop()
    element2= liste.pop()
    print(f'{element1} SPAM, {element2} SPAM')
    print()

print(str(len(liste))+" in Liste verbleibend: ", liste)