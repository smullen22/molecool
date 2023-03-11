"""
Testing for molecule module
"""

import molecool
import pytest
import sys

import numpy as np
import os

def test_move_methane(methane_molecule):
    symbols, coordinates = methane_molecule

    coordinates[0] += 5

@pytest.fixture(scope="module")
def methane_molecule():
    symbols = np.array(['C', 'H', 'H', 'H', 'H'])
    coordinates = np.array([
        [1, 1, 1],
        [2.4, 1, 1],
        [-0.4, 1, 1],
        [1, 1, 2.4],
        [1, 1, -0.4],
    ])
    
    return symbols, coordinates

def test_build_bond_list(methane_molecule):
    symbols, coordinates = methane_molecule

    bonds = molecool.build_bond_list(coordinates)

    assert len(bonds) == 4

    for atoms, bonds in bonds.items():
        assert bonds == 1.4

def test_molecular_mass(methane_molecule):
    symbols, coordinates = methane_molecule
    
    calculated_mass = molecool.calculate_molecular_mass(symbols)

    actual_mass = 16.04

    assert pytest.approx(actual_mass, abs=1e-2) == calculated_mass

def test_build_bond_list_failure(methane_molecule):
    symbols, coordinates = methane_molecule
    
    with pytest.raises(ValueError):
        molecool.build_bond_list(coordinates, min_bond=-1)

def test_center_of_mass(methane_molecule):
    symbols, coordinates = methane_molecule

    center_of_mass = molecool.calculate_center_of_mass(symbols, coordinates)

    expected_center = np.array([1,1,1])
    
    assert np.array_equal(center_of_mass, expected_center)