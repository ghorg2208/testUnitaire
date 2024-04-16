def test_average():
    input1 = [11, -11, 10, 20]
    expected_result = 7.5

    from lib import average
    actual_result = average(input1)

    assert expected_result == actual_result

def test_get_minimum():
    # Test case 1: Liste non vide
    input1 = [11, -11, 10, 20]
    expected_result = -11

    from lib import get_minimum
    actual_result = get_minimum(input1)

    assert expected_result == actual_result

    # Test case 2: Liste vide
    input2 = []
    expected_result = None

    actual_result = get_minimum(input2)

    assert expected_result == actual_result