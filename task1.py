def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp):
    return ((given_mass1/molar_mass1 + given_mass2/molar_mass2) * 0.082 * (temp + 273.15)) / volume