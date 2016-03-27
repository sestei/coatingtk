coatingtk
=========

Python-package for simulation of dielectric mirror coatings.

*This package used to come with a graphical user interface, this is now in a separate package: [CoatingGUI](https://github.com/sestei/CoatingGUI).*

The goal of this project is to provide an easy interface for coating
simulations, tailored to the needs of the gravitational wave community.
Especially, this means that this project is focussed on rather simple (design-
wise) single-wavelength coatings rather than e.g. dispersion-optimised
coatings. However, it aims to include coating thermal noise calculations.

Please see COPYRIGHT.md for copyright information and attributions.

Status
------

- Calculates reflectivity of arbitrary coating stacks for arbitrary angles of incidence. This part is well tested and works reliably.
- Calculates room-temperature coating brownian noise, as long as the required material data is available. Brownian noise at other (e.g. cryogenic) temperatures is on the wish list, but not yet implemented.
- Calculates phase of reflected light. Seems to work fine, but not tested against other models.
- Calculates electric field inside the coating. This works well for normal incidence. Oblique angles are also implemented, but the results are untested.
- Coating designs can be loaded from / saved to YAML based configuration files. These can e.g. be read in by CoatingGUI.

---
-- Sean Leavey, Sebastian Steinlechner 2015
