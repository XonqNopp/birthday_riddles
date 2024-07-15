#!/usr/bin/env python3
"""
Compute how many times we can travel to the sun and back
during my age (relative to traveller) with a speed making
the blue of sonova logo appear to be the green of the Roger logo.

https://405nm.com/color-to-wavelength/

2024

My age is the time you would spend to travel the distance
from Earth to the Sun and back 197'341.3 times
with a speed which would make you see
the blue of the Sonova logo appear to be
the green of the Roger logo.
Good luck :)
"""


SPEED_OF_LIGHT = 299792458  # [m/s]
A_UNIT = 149597870700  # [m]

ROGER_GREEN = 543  # [nm]
SONOVA_BLUE = 461  # [nm]

YEAR = 86400 * 365  # [s/year]


def v_redshift(lambda_observed: float, lambda_emitted: float) -> float:
    """Compute speed for the given redshift."""
    ratio_squared = (lambda_observed / lambda_emitted)**2
    return SPEED_OF_LIGHT * (ratio_squared - 1) / (ratio_squared + 1)


SPEED = v_redshift(ROGER_GREEN, SONOVA_BLUE)
LORENTZ_FACTOR_GAMMA = 1 / (1 - (SPEED / SPEED_OF_LIGHT)**2)**0.5


def create():
    """Create the data."""
    age = 39
    traveller_t = age * YEAR
    earth_t = traveller_t / LORENTZ_FACTOR_GAMMA
    distance = SPEED * earth_t
    distance /= (2 * A_UNIT)  # [number of back and forth to the Sun]

    print(f'{distance=:.1f}')


def solve():
    """Solve the problem."""
    n_travel = 197317.3
    distance = n_travel * 2 * A_UNIT
    earth_t = distance / SPEED
    earth_t /= YEAR

    traveller_t = earth_t * LORENTZ_FACTOR_GAMMA

    print(f'{traveller_t=:.2f}')


if __name__ == '__main__':
    create()
    solve()
