def test_print():
    print("Я принт во внешней функциии")

    def inner_test():
        print("Я принт из вложенной области видимости test_print")

    inner_test()

test_print()
inner_test()