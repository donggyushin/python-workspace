def asterisk_test(a, b, *args):
    print("a:", a)
    print("b:", b)
    print("*args:", args)


asterisk_test(1, 2, 3, 4, 5, 6)
