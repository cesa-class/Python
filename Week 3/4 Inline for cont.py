import random as rnd
from pprint import pprint

if __name__ == "__main__":
    M = [[i + j for i in range(5)] for j in range(1, 25, 5)]
    pprint(M)
    print([row[0] for row in M])
    print([row[1] ** 2 for row in M])
    print([row[0] for row in M if row[0] % 2 == 0])
    print(sum([M[i][i] for i in range(len(M))]))

    names = ['javad', 'angha', 'seyed', 'seyed']
    height = [177, 178, 170, 190]

    for i in range(len(names)):
        print(names[i], height[i])
    
    print()
    for name, h in zip(names, height):
        print(name, h)