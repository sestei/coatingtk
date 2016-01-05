#!/usr/bin/env python
# This work is licensed under the Creative Commons Attribution-NonCommercial-
# ShareAlike 4.0 International License. To view a copy of this license, visit
# http://creativecommons.org/licenses/by-nc-sa/4.0/ or send a letter to Creative
# Commons, PO Box 1866, Mountain View, CA 94042, USA.

from __future__ import division

import sys
import os

import unittest

from coatingtk.coating import Coating
from coatingtk.materials import Material, MaterialLibrary
import numpy as np

class TestCoating(unittest.TestCase):
    def test_d(self):
        lambda0 = 1064e-9

        materials = MaterialLibrary.Instance()

        # substrate and superstrate materials
        Material(name="Silica Substrate", n=1.45, Y=7.27e10, sigma=0.167, phi=5e-9)
        Material(name="Vacuum", n=1)

        # coatings
        Material(name="Silica Coating", n=1.45, Y=7.2e10, sigma=0.17, phi=4e-5)
        Material(name="Titanium Tantala Coating", n=2.06539, Y=1.4e11, sigma=0.23, phi=2.3e-4)

        coating_a = materials.get_material("Silica Coating")
        coating_b = materials.get_material("Titanium Tantala Coating")

        # layers
        layers = [["Silica Coating", 0.5 * lambda0 / coating_a.n(lambda0)]]
        layers.extend([
            ["Silica Coating", 0.27 * lambda0 / coating_a.n(lambda0)],
            ["Titanium Tantala Coating", 0.23 * lambda0 / coating_b.n(lambda0)]
        ] * 17)
        layers.append(["Silica Coating", 0.163870186147445 * lambda0 / coating_a.n(lambda0)])

        etm = Coating("Vacuum", "Silica Substrate", layers, lambda0)

        # compare class calculation to manual calculation
        self.assertAlmostEqual(etm.thickness, sum([layer[1] for layer in layers]), delta=1e-20)

if __name__ == '__main__':
    unittest.main()
