# algorithms/nutriscore_2023.py

def calculate_negative_points_2023(energy, saturated_fat, sugars, salt):
    """Calculate total negative points based on 2023 algorithm."""
    energy_points = 0 if energy <= 335 else 1 if energy <= 670 else 2 if energy <= 1005 else 3 if energy <= 1340 else 4 if energy <= 1675 else 5 if energy <= 2010 else 6 if energy <= 2345 else 7 if energy <= 2680 else 8 if energy <= 3015 else 9 if energy <= 3350 else 10
    sat_fat_points = 0 if saturated_fat <= 1 else 1 if saturated_fat <= 2 else 2 if saturated_fat <= 3 else 3 if saturated_fat <= 4 else 4 if saturated_fat <= 5 else 5 if saturated_fat <= 6 else 6 if saturated_fat <= 7 else 7 if saturated_fat <= 8 else 8 if saturated_fat <= 9 else 9 if saturated_fat <= 10 else 10
    sugar_points = 0 if sugars <= 3.4 else 1 if sugars <= 6.8 else 2 if sugars <= 10 else 3 if sugars <= 14 else 4 if sugars <= 17 else 5 if sugars <= 20 else 6 if sugars <= 24 else 7 if sugars <= 27 else 8 if sugars <= 31 else 9 if sugars <= 34 else 10 if sugars <= 37 else 11 if sugars <= 41 else 12 if sugars <= 44 else 13 if sugars <= 48 else 14 if sugars <= 51 else 15
    salt_points = 0 if salt <= 0.2 else 1 if salt <= 0.4 else 2 if salt <= 0.6 else 3 if salt <= 0.8 else 4 if salt <= 1.0 else 5 if salt <= 1.2 else 6 if salt <= 1.4 else 7 if salt <= 1.6 else 8 if salt <= 1.8 else 9 if salt <= 2.0 else 10 if salt <= 2.2 else 11 if salt <= 2.4 else 12 if salt <= 2.6 else 13 if salt <= 2.8 else 14 if salt <= 3.0 else 15 if salt <= 3.2 else 16 if salt <= 3.4 else 17 if salt <= 3.6 else 18 if salt <= 3.8 else 19 if salt <= 4.0 else 20
    return energy_points + sat_fat_points + sugar_points + salt_points 



def calculate_positive_points_2023(fiber, protein, fruits_veg):
    """Calculate total positive points based on 2023 algorithm."""
    fiber_points = 0 if fiber <= 3.0 else 1 if fiber <= 4.1 else 2 if fiber <= 5.2 else 3 if fiber <= 6.3 else 4 if fiber <= 7.4 else 5
    protein_points = 0 if protein <= 2.4 else 1 if protein <= 4.8 else 2 if protein <= 7.2 else 3 if protein <= 9.6 else 4 if protein <= 12 else 5 if protein <= 14 else 6 if protein <= 17 else 7
    fruits_veg_points = 0 if fruits_veg < 40 else 1 if fruits_veg <= 60 else 2 if fruits_veg <= 80 else 5
    return fiber_points + protein_points + fruits_veg_points


def nutriscore_2023(energy, saturated_fat, sugars, salt, fiber, protein, fruits_veg):
    """Calculate the Nutri-Score for 2023."""
    N = calculate_negative_points_2023(energy, saturated_fat, sugars, salt)
    P = calculate_positive_points_2023(fiber, protein, fruits_veg)
    return N - P


def nutriscore_2023_Master(energy, saturated_fat, sugars, salt, fiber, protein, fruits_veg):
    """Calculate total points including conditions based on 2023 algorithm."""
    N = calculate_negative_points_2023(energy, saturated_fat, sugars, salt)
    P = calculate_positive_points_2023(fiber, protein, fruits_veg)
    Prot = protein_points = 0 if protein <= 2.4 else 1 if protein <= 4.8 else 2 if protein <= 7.2 else 3 if protein <= 9.6 else 4 if protein <= 12 else 5
    if N >= 11: #takes in account the >11N rule
        return N - P + Prot #excludes proteins from calculation
    else:
        return N - P
