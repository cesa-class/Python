import random
if __name__ == "__main__":
    # A list is a collection which is ordered and changeable. In Python lists are written with square brackets -> []
    l = []
    l1 = [1, 2, 3, 4, 5, 6]
    l2 = ['hey', 'jude', 'dont', 'make', 'it', 'bad']
    print(l, type(l), len(l))
    print(l1, len(l1))
    print(l2)

    for item in l2:
        print(item, end=' ')

    # To add an item to the end of the list, we use the append() method.
    for i in range(20):
        l.append(random.randint(0,100)) 

    print(l)

    # Access list elements.
    print(l[5], l[9])

    # We can appent other types to a list.
    l2.append('sc')
    l2.append([0,0,0])

    # Copy a list.
    p = l[:]

    # List sort method
    l.sort()
    print(l)
    print(p)


    if l:
        print('full')
    else:
        print('empty')

    while l:
        l.pop()

    # Remove an item from a list.
    q = [1,5,5,9]
    q.remove(5)
    print(q)
