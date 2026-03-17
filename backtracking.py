def raju(a):
    if a == 1:
        return
    print(a + 10, end=" ")
    raju(a - 1)
    print(a)


raju(4)
