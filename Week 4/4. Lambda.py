if __name__ == "__main__":
    M = [['parham', 20], ['javad', 5], ['angha', 30]]
    M.sort(key=lambda x : x[1])
    print(M)
    a = lambda x, y:x + y
    print(a(1,2))
