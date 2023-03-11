"""
Tests for the measure module.
"""

# imports
import pytest

import molecool
import numpy as np

def test_calculate_distance():

    r1 = np.array([0, 0, 0])
    r2 = np.array([0, 1, 0])

    expected_distance = 1

    calculate_distance = molecool.calculate_distance(r1,r2)

    assert expected_distance == calculate_distance

def test_calculate_angle():

    r1 = np.array([0, 0, -1])
    r2 = np.array([0, 0, 0])
    r3 = np.array([1, 0, 0])

    expected_angle = 90

    calculated_angle = molecool.calculate_angle(r1,r2,r3, degrees = True)

    assert pytest.approx(expected_angle, abs=1e-2)  == calculated_angle

@pytest.mark.parametrize("p1, p2, p3, expected_angle", [
    (np.array([np.sqrt(2)/2, np.sqrt(2)/2, 0]), np.array([0, 0, 0]),np.array([1, 0, 0]),45),
    (np.array([0, 0, -1]), np.array([0, 1, 0]), np.array([1, 0, 0]), 60),
])
def test_calculate_angle_many(p1, p2, p3, expected_angle):
    calculated_angle = molecool.calculate_angle(p1, p2, p3, degrees = True)

    assert pytest.approx(expected_angle, abs=1e-2)  == calculated_angle