import math

def printHead():
    print(" - Pokedex - ")

def createCategories():
    global starter
    starter = [1,2,3,4,5,6,7,8,9,
    152,153,154,155,156,157,158,159,160,
    252,253,254,255,256,257,258,259,260,
    387,388,389,390,391,392,393,394,395,
    495,496,497,498,499,500,501,502,503,
    650,651,652,653,654,655,656,657,658,
    722,723,724,725,726,727,728,729,730,
    810,811,812,813,814,815,816,817,818,
    906,907,908,910,911,912,913,914,915]

    global pseudo
    pseudo = [147,148,149,
    246,247,248,
    371,372,373,374,375,376,
    443,444,445,
    633,634,635,
    704,705,706,
    782,783,784,
    885,886,887,
    996,997,998]

    global legendary
    legendary = [144,145,146,150,
    243,245,246,249,250,
    377,378,379,380,381,382,383,384,
    480,481,482,483,484,485,486,487,488,
    638,639,640,641,642,643,644,645,646,
    716,717,718,
    772,773,785,786,787,788,789,790,791,792,800,
    888,889,890,891,892,894,895,896,897,898,
    1007,1008,1014,1015,1016,1017,1024]

    global mythical
    mythical = [151,
    251,
    385,386,
    489,490,491,492,493,
    494,647,648,649,
    719,720,721,
    801,802,807,808,809,
    893,
    1025]

    global ultrabeast
    ultrabeast = [793,794,795,796,797,798,799,803,804,805,806]

    global paradox
    paradox = [984,985,986,987,988,989,990,991,992,993,994,995,1005,1006,1009,1010,1020,1021,1022,1023]

def createDex():
    global dex
    dex = {}
    temp = 1
    while temp < 1026:
        dex[temp] = 0
        temp = temp + 1

    save_path = r"dex\save.txt"

    with open(save_path, 'w') as f:
        for key, value in dex.items():
            f.write(f"{key}: {value}\n")

def loadDex():
    global dex
    dex = {}

    global save_path
    save_path = r"dex\save.txt"

    try:
        with open(save_path, 'r') as f:
            for line in f:
                key, value = map(int, line.strip().split(': '))
                dex[key] = value
    except FileNotFoundError:
        print("No save file found. Creating a new Pokedex...")
        createDex()

def loadPokemonList():
    save_path_list = r"dex\pokemon_list.txt"
    with open(save_path_list, "r") as f:
        return [line.strip() for line in f.readlines()]

def modifyEntry(entry):
    if dex.get(entry) == 0:
        dex[entry] = 1
        print(f"Pokedex entry {entry} is now marked completed!")
    else:
        dex[entry] = 0
        print(f"Pokedex entry {entry} is no longer marked completed!")

    with open(save_path, 'w') as f:
        for key, value in dex.items():
            f.write(f"{key}: {value}\n")

    main()

def viewEntry(entry):
    print(f"Viewing Pokedex Entry {entry}")
    print(f"Entry contains {pokemon_list[entry]}")
    
    if entry in starter:
        print("This Pokemon is classidied as a 'Starter'")
    elif entry in pseudo:
        print("This Pokemon is classidied as a 'Pseudo-Legendary'")
    elif entry in legendary:
        print("This Pokemon is classidied as a 'Legendary'")
    elif entry in mythical:
        print("This Pokemon is classidied as a 'Mythical'")
    elif entry in ultrabeast:
        print("This Pokemon is classidied as a 'Ultra Beast'")
    elif entry in paradox:
        print("This Pokemon is classidied as a 'Paradox Pokemon'")
    else:
        print("This Pokemon doesnt have any special classifications")

    if dex.get(entry) == 0:
        print(f"This Pokedex Entry is marked as incompleted")
    else:
        print(f"This Pokedex Entry is marked as complete")
    
    main()

def viewCompletion():
    temp = 1
    complete = 0
    incomplete = 0
    completion = 0
    while temp < 1026:
        if dex.get(temp) == 0:
            incomplete = incomplete + 1
        else:
            complete = complete + 1
        temp = temp + 1
    completion = complete / 1025
    completion = completion * 100
    print(f"{complete}/1025 entries are marked as complete")
    print(f"{incomplete}/1025 entries are marked as incomplete")
    print(f"Your Pokedex is {math.floor(completion)}% complete")
    main()
    

def main():
    loadDex()
    first = 0
    if first == 0:
        global pokemon_list
        pokemon_list = loadPokemonList()
        printHead()
        createCategories()
        first = 1
    print("What Action do you want to take?")
    print("[M]odify an entry")
    print("[V]iew entry")
    print("[C]heck completion")
    print("[R]eset dex")
    i = input("Choose")
    if i == "M" or i == "m":
        e = int(input("Which entry do you want to modify? [1-1025]"))
        modifyEntry(e)
    elif i == "V" or i == "v":
        e = int(input("Which entry do you want to view? [1-1025]"))
        viewEntry(e)
    elif i == "C" or i == "c":
        viewCompletion()
    elif i == "R" or i == "r":
        print("This is a permanent Action!")
        j = input("Are you sure you want to clear your Progress? [Y]es/[N]o")
        if j == "Y" or j == "y":
            createDex()
        elif j == "N" or j == "n":
            main()

main()