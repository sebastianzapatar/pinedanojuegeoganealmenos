import pytest

from calc.ops import add

@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1,2,3),
        (-6,6,0),
        (0,0,1),
        (10,-3,7)
    ],
)
def test_add(a,b,expected):
    assert add(a,b)==expected