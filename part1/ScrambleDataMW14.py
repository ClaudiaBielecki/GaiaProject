import numpy as np
from astropy.table import QTable
import astropy.coordinates as coord
import astropy.units as u
from galpy.orbit import Orbit
from galpy.potential.mwpotentials import MWPotential2014
from galpy.util.conversion import get_physical

gaia_rad = QTable.read("DR3withBPRP.csv")

print('test1')
pmra = np.array(gaia_rad['pmra'])
np.random.shuffle(pmra)
pmdec = np.array(gaia_rad['pmdec'])
np.random.shuffle(pmdec)
radvel = np.array(gaia_rad['radial_velocity'])
np.random.shuffle(radvel)

# Making a SkyCoord object to easily transform between coordinates
c = coord.SkyCoord(ra = gaia_rad['ra']*u.deg,
                   dec = gaia_rad['dec']*u.deg,
                   distance = coord.Distance(parallax = (u.Quantity(gaia_rad['parallax'] ) +0.017)*u.mas, allow_negative=True),
                   pm_ra_cosdec = pmra *u.mas/u.year,
                   pm_dec = pmdec *u.mas/u.year,
                   radial_velocity = radvel *u.km/u.s,
                   frame = 'icrs')

orbits = Orbit(c)
orbits.turn_physical_off()
# stars with positive Lz are rotating with the disk
# stars with negative Lz are counter rotating wrt the disk


Lz = orbits.Lz()
indx_counter =  (Lz < 0)
counter_orbits = orbits[indx_counter]
print('test2')
# Integrals of motion
# First get potential
Potential = MWPotential2014

E_counter  = counter_orbits.E(pot = Potential)
# removing unbound orbits
bound_ind =  (E_counter < 0)
counter_orbits = counter_orbits[bound_ind]

print('test3')
E_counter  = counter_orbits.E(pot = Potential)
Lz_counter = counter_orbits.Lz()
e_counter  = counter_orbits.e(pot = Potential, analytic=True, type= 'staeckel')
L_counter  = np.sqrt(np.sum(counter_orbits.L()**2, axis=1))
print('test4')

np.savetxt('E_scrambled.csv', E_counter, delimiter=',')
np.savetxt('L_scrambled.csv', L_counter, delimiter=',')
np.savetxt('Lz_scrambled.csv', Lz_counter, delimiter=',')
np.savetxt('e_scrambled.csv', e_counter, delimiter=',')

