def szoveg_kiiras(szoveg, betu_keszlet):
    matrixok = [betu_keszlet[betu] for betu in szoveg]
    for sorok in zip(*matrixok):
        for betu, karakterlista in zip(szoveg, sorok):
            for pixel in karakterlista:
                if pixel == 0:
                    print(hatter, end=" ")
                else:
                    print(betu, end=" ")
            print(end="  ")
        print()

hatter = input("Miből legyen a háttér? ")
szo = input("Mi legyen a szó? ")

abc = {
    "a":[[0, 0, 0, 1, 1, 0, 0, 0],
         [0, 0, 1, 1, 1, 1, 0, 0],
         [0, 1, 1, 0, 0, 1, 1, 0],
         [1, 1, 0, 0, 0, 0, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 0, 0, 0, 0, 1, 1],
         [1, 1, 0, 0, 0, 0, 1, 1]],

    "z":[[1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1],
         [0, 0, 0, 0, 0, 1, 1, 1],
         [0, 0, 0, 0, 1, 1, 1, 0],
         [0, 0, 1, 1, 1, 0, 0, 0],
         [1, 1, 1, 0, 0, 0, 0, 0],
         [1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1]],

    "i":[[0, 0, 1, 1, 0, 0],
         [0, 0, 1, 1, 0, 0],
         [0, 0, 1, 1, 0, 0],
         [0, 0, 1, 1, 0, 0],
         [0, 0, 1, 1, 0, 0],
         [0, 0, 1, 1, 0, 0],
         [0, 0, 1, 1, 0, 0],
         [0, 0, 1, 1, 0, 0]]
}

szoveg_kiiras(szo, abc)
