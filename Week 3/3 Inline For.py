from pprint import pprint

if __name__ == "__main__":
    l = [0] * 20
    l2 = [[0] * 5] * 5
    pprint(l2)
    l2[0][0] = 1
    pprint(l2)

    # Somehow inline for.
    l = [0 for i in range(5)]
    print(l)

    l2 = [[0] * 5 for i in range(5)]
    pprint(l2)
    l2[0][0] = 1
    pprint(l2)