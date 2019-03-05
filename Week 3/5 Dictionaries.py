if __name__ == "__main__":
    d = {'name' : 'parham',
         'age' : 20,
         'number' : [6568568, 9456356]}

    print(d)   
    print(d['number'][0])

    print(list(d.keys()))

    for key, value in d.items():
        print(key, value)

    names = ['javad', 'angha', 'seyed', 'seyed']
    height = [177, 178, 170, 190]
    o = dict(zip(names, height))
    print(o)

    a = 5
    b = 6
    print(a, b)
    a, b = b, a
    print(a, b)