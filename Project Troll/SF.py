def swapFileData():
    file1 = input("Enter first file name:-")
    file2 = input("Enter second file name:-")

    with open(file1, 'r') as a:
        dataA = a.read()

    with open(file2, 'r') as b:
        dataB = b.read()

    with open(file1, 'w') as a:
        a.write(dataA)

    with open(file2, 'w') as b:
        b.write(dataB)

swapFileData()