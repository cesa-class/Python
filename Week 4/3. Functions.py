def powerX(a: int, x: int) -> int:
    b = a ** x
    return b

def www(a, b=5):
    return a + b

def m(N):
    def h(X):
        return X**N
    return h

if __name__ == "__main__":
    print(powerX(2, 2))

    def a():
        print("in a")
    
    a()

    w = powerX
    print(w(3,3))

    print(www(1))

    e = m(3)
    print(e(5))