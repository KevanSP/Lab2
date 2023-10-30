import Exercies6.Lab2 as LabCode


def test_find_min_max():
    test_arr = [5, 67, 32]
    pass_arr = [5, 67]

    result = LabCode.find_min_max(test_arr)
    assert (result == pass_arr)


def test_calc_average():
    test_arr = [5, 67, 32]
    result = LabCode.calc_average(test_arr)
    assert (int(result) == 34)


def test_calc_median_temperature():
    test_arr = [5, 67, 32]
    result = LabCode.calc_median_temperature(test_arr)
    assert (result == 32)
