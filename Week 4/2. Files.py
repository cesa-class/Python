if __name__ == "__main__":
    # myfile = open('./test.txt', 'w')
    # myfile.write('hey jude dont make it bad.')
    # myfile.close()

    # f = open('./test.txt')
    # # for line in f:
    # #     print(line)
    # print(f.read())
    # f.close()

    with open('./test.txt') as f:
       print(f.read())