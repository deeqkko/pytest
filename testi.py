#-*-coding: utf-8-*-

while True:
    print('\n(1) Lue muistikirjaa\n(2) Lisää merkintä\n(3) Tyhjennä muistikirja\n(4) Lopeta\n')
    choice = int(input("Mitä haluat tehdä?: "))
    if choice == 4:
        print("Lopetetaan.\n")
        break
    elif choice == 3:
        memo = open('muistio.txt','w')
        memo.close()
        print("Muistio tyhjennetty.")
    elif choice == 2:
        entry = input("Kirjoita uusi merkintä: ")
        entry = entry+'\n'
        memo = open('muistio.txt','a')
        memo.write(entry)
        memo.close()
    else:
        memo = open('muistio.txt','r')
        content = memo.readlines()
        for line in content:
            print(line)
