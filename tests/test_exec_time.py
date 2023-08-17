import timeout_decorator


@timeout_decorator.timeout(5)
def test_cells_gen_5sec_size3():
    cells3 = ['0' * (8 - len(str(i))) + str(i) for i in range(3 ** 2)]


@timeout_decorator.timeout(5)
def test_cells_gen_5sec_size10():
    cells10 = ['0' * (99 - len(str(i))) + str(i) for i in range(10 ** 2)]


@timeout_decorator.timeout(5)
def test_cells_gen_5sec_size100():
    cells100 = ['0' * (999 - len(str(i))) + str(i) for i in range(100 ** 2)]

