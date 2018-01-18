import itertools

if __name__ == '__main__':

    coins = [2, 3, 5, 7, 9] # corresponds to [red, corroded, shiny, concave, blue]
    configurations = itertools.permutations(coins)

    for configuration in configurations:
        a = configuration[0]
        b = configuration[1]
        c = configuration[2]
        d = configuration[3]
        e = configuration[4]

        if a + b*c**2 + d**3 - e == 399:
            print(configuration)
