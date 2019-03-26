def temp(*args, **kargs):
    print(args)
    print(kargs)

import sys
def kiaprint(*args, **kargs):
    sep = kargs.pop('sep', '\t')
    end = kargs.pop('end', '\n')
    f = kargs.pop('file', sys.stdout)

    if kargs:
        raise TypeError('extra : {}'.format(kargs))
    output = sep.join(map(str, args))

    f.write(output + end)

if __name__ == "__main__":
    a, *b, c = [1,2,3,4,5]
    print(a, b, c)
    temp(1,2,3, t=5, j =9)

    kiaprint(1,2,3, end='\n\n', sep='--')