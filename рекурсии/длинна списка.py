def find_farthest_orbit(list_of_orbits):
    orb_planet = []
    pi = 3.14
    for i in list_of_orbits:
        if (i[0] != i[1]):
            S = pi * i[0] * i[1]
            orb_planet.append(S)
            a = max(orb_planet)
    for i in list_of_orbits:
        if (pi * i[0] * i[1] == a) and (i[0] != i[1]):
            return i


orbits = [(1.0, 4.0), (5.0, 1.0)]
print(*find_farthest_orbit(orbits))
