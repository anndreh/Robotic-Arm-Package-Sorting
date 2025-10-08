from package_sorter import sort

def test_standard_package():
    width, height, length, mass = 10, 20, 30, 5
    excepted_output = "STANDARD"

    actual_output = sort(width, height, length, mass)

    assert actual_output == excepted_output

def test_bulky_by_volume():
    width, height, length, mass = 100, 100, 100, 15
    excepted_output = "SPECIAL"

    actual_output = sort(width, height, length, mass)

    assert actual_output == excepted_output

def test_bulky_by_dimension():
    width, height, length, mass = 150, 10, 10, 15
    excepted_output = "SPECIAL"

    actual_output = sort(width, height, length, mass)

    assert actual_output == excepted_output

def test_heavy_package():
    width, height, length, mass = 10, 20, 30, 20
    expected_output = "SPECIAL"

    actual_output = sort(width, height, length, mass)

    assert actual_output == expected_output

def test_rejected_volume_package():
    width, height, length, mass = 100, 100, 100, 25
    expeted_result = "REJECTED"

    actual_output = sort(width, height, length, mass)

    assert actual_output == expeted_result

def test_rejected_dimension_package():
    width, height, length, mass = 160, 100, 100, 25
    expected_result = "REJECTED"

    actual_output = sort(width, height, length, mass)

    assert actual_output == expected_result

def test_boundary_package():
    width, height, length, mass = 149, 10, 10, 19
    expected_result = "STANDARD"

    actual_output = sort(width, height, length, mass)

    assert actual_output == expected_result