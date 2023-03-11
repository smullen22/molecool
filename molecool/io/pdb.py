"""
Functions for manipulating pdb files.
"""

import numpy as np


def open_pdb(f_loc):
  """Open and read coordinates and atom symbols from a pdb file.
    The pdb file must specify the atom elements in the last column, and follow
    the conventions outlined in the PDB format specification.
    Parameters
    ----------
    file_location : str
        The location of the pdb file to read in.
    Returns
    -------
    coords : np.ndarray
        The coordinates of the pdb file.
    symbols : list
        The atomic symbols of the pdb file.
    """
    with open(f_loc) as f:
        data = f.readlines()

    c = []
    sym = []
    for l in data:
        if "ATOM" in l[0:6] or "HETATM" in l[0:6]:
            sym.append(l[76:79].strip())
            c2 = [float(x) for x in l[30:55].split()]
            c.append(c2)

    coords = np.array(c)

    return sym, coords