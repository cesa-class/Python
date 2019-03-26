if __name__ == "__main__":
    S = 'Hey jude dont make it bad'
    print(S.find('jude'))
    print(S.replace('jude', 'javad'))
    print(S.lower())
    print(S.upper())
    print(S.title())
    l = [1, 2, 3]
    print(l)
    print('*****'.join([str(i) for i in l]))