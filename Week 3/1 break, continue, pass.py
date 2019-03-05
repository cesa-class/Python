if __name__ == "__main__":
    for i in range(10):
        print(i, end=' ')
    
    print()
    for i in range(10):
        if i == 7:
            break
        print(i, end=' ')
    
    print()
    for i in range(10):
        if i == 7:
            continue
        print(i, end=' ')

    print()
    for i in range(10):
        if i == 7:
            pass
        print(i, end=' ')