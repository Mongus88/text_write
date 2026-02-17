def szoveg_kiiras(szo, ABC):
    for sorok in range(0, len(ABC[szo[0]])):
        for karakterek in szo:
            for oszlopok in range(0, len(ABC[karakterek][sorok])):
                print(ABC[karakterek][sorok][oszlopok], end= " ")
            print("  ", end="")
        print()

hatter = input("Miből legyen a háttér? ")
tinta = input("Miből legyen a tinta? ")
szo = input("Mi legyen a szó? ")

ABC = {
    "a":[[hatter, hatter, hatter, tinta, tinta, hatter, hatter, hatter],
         [hatter, hatter, tinta, tinta, tinta, tinta, hatter, hatter],
         [hatter, tinta, tinta, hatter, hatter, tinta, tinta, hatter],
         [tinta, tinta, hatter, hatter, hatter, hatter, tinta, tinta],
         [tinta, tinta, tinta, tinta, tinta, tinta, tinta, tinta],
         [tinta, tinta, tinta, tinta, tinta, tinta, tinta, tinta],
         [tinta, tinta, hatter, hatter, hatter, hatter, tinta, tinta],
         [tinta, tinta, hatter, hatter, hatter, hatter, tinta, tinta]],

    "z":[[tinta, tinta, tinta, tinta, tinta, tinta, tinta, tinta],
         [tinta, tinta, tinta, tinta, tinta, tinta, tinta, tinta],
         [hatter, hatter, hatter, hatter, hatter, tinta, tinta, tinta],
         [hatter, hatter, hatter, hatter, tinta, tinta, tinta, hatter],
         [hatter, hatter, tinta, tinta, tinta, hatter, hatter, hatter],
         [tinta, tinta, tinta, hatter, hatter, hatter, hatter, hatter],
         [tinta, tinta, tinta, tinta, tinta, tinta, tinta, tinta],
         [tinta, tinta, tinta, tinta, tinta, tinta, tinta, tinta]]
}

szoveg_kiiras(szo, ABC)
