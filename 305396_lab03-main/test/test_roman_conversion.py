import pytest
from utility.roman import int_to_roman  


def test_int_to_roman():
    assert int_to_roman(1) == 'I'
    assert int_to_roman(4) == 'IV'
    assert int_to_roman(9) == 'IX'
    assert int_to_roman(58) == 'LVIII'
    assert int_to_roman(1994) == 'MCMXCIV'

    with pytest.raises(ValueError, match="Input must be an integer between 1 and 3999"):
        int_to_roman(0)

    with pytest.raises(ValueError, match="Input must be an integer between 1 and 3999"):
        int_to_roman(4000)





