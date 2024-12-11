
#this stores each points individually. It makes the calculations in algorithms a bit useless now but I realised too late and I am scared to touch anything when it works finally.


def energy_points(energy):
    return int(0) if energy <= int(335) else int(1) if energy <= int(670) else int(2) if energy <= int(1005) else int(3) if energy <= int(1340) else int(4) if energy <= int(1675) else int(5) if energy <= int(2010) else int(6) if energy <= int(2345) else int(7) if energy <= int(2680) else int(8) if energy <= int(3015) else int(9) if energy <= int(3350) else int(10)


def saturated_fat_points(saturated_fat):
    return 0 if saturated_fat <= 1 else 1 if saturated_fat <= 2 else 2 if saturated_fat <= 3 else 3 if saturated_fat <= 4 else 4 if saturated_fat <= 5 else 5 if saturated_fat <= 6 else 6 if saturated_fat <= 7 else 7 if saturated_fat <= 8 else 8 if saturated_fat <= 9 else 9 if saturated_fat <= 10 else 10

def sugar_points(sugars):
    return 0 if sugars <= 4.5 else 1 if sugars <= 9 else 2 if sugars <= 13.5 else 3 if sugars <= 18 else 4 if sugars <= 22.5 else 5 if sugars <= 27 else 6 if sugars <= 31 else 7 if sugars <= 36 else 8 if sugars <= 40 else 9 if sugars <= 45 else 10

def salt_points(sodium):
    return 0 if sodium <= 90 else 1 if sodium <= 180 else 2 if sodium <= 270 else 3 if sodium <= 360 else 4 if sodium <= 450 else 5 if sodium <= 540 else 6 if sodium <= 630 else 7 if sodium <= 720 else 8 if sodium <= 810 else 9 if sodium <= 900 else 10

def fiber_points(fiber):
    return 0 if fiber <= 0.9 else 1 if fiber <= 1.9 else 2 if fiber <= 2.8 else 3 if fiber <= 3.7 else 4 if fiber <= 4.7 else 5

def protein_points(protein):
    return 0 if protein <= 1.6 else 1 if protein <= 3.2 else 2 if protein <= 4.8 else 3 if protein <= 6.4 else 4 if protein <= 8 else 5

def fruits_veg_points(fruits_veg):
    return 0 if fruits_veg < 40 else 1 if fruits_veg <= 60 else 2 if fruits_veg <= 80 else 5

def calculate_negative_points_2017(energy, saturated_fat, sugars, sodium):
    """Calculate total negative points based on 2017 algorithm."""
    return energy_points(energy) + saturated_fat_points(saturated_fat) + sugar_points(sugars) + salt_points(sodium)

def calculate_positive_points_2017(fiber, protein, fruits_veg):
    """Calculate total positive points based on 2017 algorithm."""
    return fiber_points(fiber) + protein_points(protein) + fruits_veg_points(fruits_veg)


def energy_points_2023(energy):
    return 0 if energy <= 335 else 1 if energy <= 670 else 2 if energy <= 1005 else 3 if energy <= 1340 else 4 if energy <= 1675 else 5 if energy <= 2010 else 6 if energy <= 2345 else 7 if energy <= 2680 else 8 if energy <= 3015 else 9 if energy <= 3350 else 10

def saturated_fat_points_2023(saturated_fat):
    return 0 if saturated_fat <= 1 else 1 if saturated_fat <= 2 else 2 if saturated_fat <= 3 else 3 if saturated_fat <= 4 else 4 if saturated_fat <= 5 else 5 if saturated_fat <= 6 else 6 if saturated_fat <= 7 else 7 if saturated_fat <= 8 else 8 if saturated_fat <= 9 else 9 if saturated_fat <= 10 else 10

def sugar_points_2023(sugars):
   return 0 if sugars <= 3.4 else 1 if sugars <= 6.8 else 2 if sugars <= 10 else 3 if sugars <= 14 else 4 if sugars <= 17 else 5 if sugars <= 20 else 6 if sugars <= 24 else 7 if sugars <= 27 else 8 if sugars <= 31 else 9 if sugars <= 34 else 10 if sugars <= 37 else 11 if sugars <= 41 else 12 if sugars <= 44 else 13 if sugars <= 48 else 14 if sugars <= 51 else 15


def salt_points_2023(salt):
    return 0 if salt <= 0.2 else 1 if salt <= 0.4 else 2 if salt <= 0.6 else 3 if salt <= 0.8 else 4 if salt <= 1.0 else 5 if salt <= 1.2 else 6 if salt <= 1.4 else 7 if salt <= 1.6 else 8 if salt <= 1.8 else 9 if salt <= 2.0 else 10 if salt <= 2.2 else 11 if salt <= 2.4 else 12 if salt <= 2.6 else 13 if salt <= 2.8 else 14 if salt <= 3.0 else 15 if salt <= 3.2 else 16 if salt <= 3.4 else 17 if salt <= 3.6 else 18 if salt <= 3.8 else 19 if salt <= 4.0 else 20


def fiber_points_2023(fiber):
    return 0 if fiber <= 3.0 else 1 if fiber <= 4.1 else 2 if fiber <= 5.2 else 3 if fiber <= 6.3 else 4 if fiber <= 7.4 else 5

def protein_points_2023(protein):
    return 0 if protein <= 2.4 else 1 if protein <= 4.8 else 2 if protein <= 7.2 else 3 if protein <= 9.6 else 4 if protein <= 12 else 5 if protein <= 14 else 6 if protein <= 17 else 7

def fruits_veg_points_2023(fruits_veg):
    return 0 if fruits_veg < 40 else 1 if fruits_veg <= 60 else 2 if fruits_veg <= 80 else 5

def calculate_negative_points_2023(energy, saturated_fat, sugars, salt):
    """Calculate total negative points based on 2023 algorithm."""
    return energy_points_2023(energy) + saturated_fat_points_2023(saturated_fat) + sugar_points_2023(sugars) + salt_points_2023(salt)

def calculate_positive_points_2023(fiber, protein, fruits_veg):
    """Calculate total positive points based on 2023 algorithm."""
    return fiber_points_2023(fiber) + protein_points_2023(protein) + fruits_veg_points_2023(fruits_veg)

def nutriscore_2023(energy, saturated_fat, sugars, salt, fiber, protein, fruits_veg):
    """Calculate the Nutri-Score for 2023."""
    N = calculate_negative_points_2023(energy, saturated_fat, sugars, salt)
    P = calculate_positive_points_2023(fiber, protein, fruits_veg)
    return N - P

def nutriscore_2023_Master(energy, saturated_fat, sugars, salt, fiber, protein, fruits_veg):
    """Calculate total points including conditions based on 2023 algorithm."""
    N = calculate_negative_points_2023(energy, saturated_fat, sugars, salt)
    P = calculate_positive_points_2023(fiber, protein, fruits_veg)
    Prot = protein_points_2023(protein)
    
    if N >= 11: # Takes into account the >11N rule
        return N - P + Prot  # Excludes proteins from calculation if N >= 11
    else:
        return N - P


def nutriscore_2017_Master(energy, saturated_fat, sugars, sodium, fiber, protein, fruits_veg):
    """Calculate total points including conditions based on 2017 algorithm."""
    N = calculate_negative_points_2017(energy, saturated_fat, sugars, sodium)
    P = calculate_positive_points_2017(fiber, protein, fruits_veg)
    fv_points = fruits_veg_points(fruits_veg)
    Prot = protein_points(protein)
    
    if N >= 11: # Takes into account the >11N rule
        if fv_points >= 5:
            return N - P
    return N - P
