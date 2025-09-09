import math
import pytest
from math_basic import square, factorial, is_prime, gcd, lcm


# ---------- square ----------
def test_square_happy_int():
    assert square(3) == 9


def test_square_happy_negative():
    assert square(-4) == 16


def test_square_type_error():
    with pytest.raises(TypeError):
        square("3")


# ---------- factorial ----------
def test_factorial_zero():
    assert factorial(0) == 1


def test_factorial_basic():
    assert factorial(5) == 120


def test_factorial_negative_raises():
    with pytest.raises(ValueError):
        factorial(-1)


def test_factorial_type_error_on_float():
    with pytest.raises(TypeError):
        factorial(3.2)


# ---------- is_prime ----------
def test_is_prime_true():
    assert is_prime(17) is True


def test_is_prime_false_composite():
    assert is_prime(18) is False


def test_is_prime_less_than_two_is_false():
    assert is_prime(1) is False


def test_is_prime_type_error():
    with pytest.raises(TypeError):
        is_prime(10.0)


# ---------- gcd ----------
def test_gcd_basic():
    assert gcd(54, 24) == 6


def test_gcd_with_negatives():
    assert gcd(-8, 12) == 4


def test_gcd_both_zero_is_zero():
    assert gcd(0, 0) == 0


def test_gcd_type_error():
    with pytest.raises(TypeError):
        gcd(3.5, 2)


# ---------- lcm ----------
def test_lcm_basic():
    assert lcm(4, 6) == 12


def test_lcm_with_negatives():
    assert lcm(-4, 6) == 12


def test_lcm_any_zero_is_zero():
    assert lcm(0, 5) == 0


def test_lcm_type_error():
    with pytest.raises(TypeError):
        lcm("4", 6)
