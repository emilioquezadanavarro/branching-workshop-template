from time_converter import seconds_to_minutes


def test_basic_conversion():
    # ARRANGE: Set up the input
    seconds = 120
    minutes = seconds_to_minutes(seconds)
    assert minutes == 2.0


def test_zero_conversion():
    # Test case for zero seconds
    assert seconds_to_minutes(0) == 0.0


def test_fractional_conversion():
    # Test case for a number that results in a fraction
    assert seconds_to_minutes(30) == 0.5
