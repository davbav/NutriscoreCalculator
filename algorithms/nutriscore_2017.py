# algorithms/nutriscore_2017.py


def calculate_negative_points_2017(energy, saturated_fat, sugars, sodium):
    """Calculate total negative points based on 2017 algorithm."""
    energy_points = 0 if energy <= 335 else 1 if energy <= 670 else 2 if energy <= 1005 else 3 if energy <= 1340 else 4 if energy <= 1675 else 5 if energy <= 2010 else 6 if energy <= 2345 else 7 if energy <= 2680 else 8 if energy <= 3015 else 9 if energy <= 3350 else 10
    sat_fat_points = 0 if saturated_fat <= 1 else 1 if saturated_fat <= 2 else 2 if saturated_fat <= 3 else 3 if saturated_fat <= 4 else 4 if saturated_fat <= 5 else 5 if saturated_fat <= 6 else 6 if saturated_fat <= 7 else 7 if saturated_fat <= 8 else 8 if saturated_fat <= 9 else 9 if saturated_fat <= 10 else 10
    sugar_points = 0 if sugars <= 4.5 else 1 if sugars <= 9 else 2 if sugars <= 13.5 else 3 if sugars <= 18 else 4 if sugars <= 22.5 else 5 if sugars <= 27 else 6 if sugars <= 31 else 7 if sugars <= 36 else 8 if sugars <= 40 else 9 if sugars <= 45 else 10
    salt_points = 0 if sodium <= 90 else 1 if sodium <= 180 else 2 if sodium <= 270 else 3 if sodium <= 360 else 4 if sodium <= 450 else 5 if sodium <= 540 else 6 if sodium <= 630 else 7 if sodium <= 720 else 8 if sodium <= 810 else 9 if sodium <= 900 else 10
    return energy_points + sat_fat_points + sugar_points + salt_points



def calculate_positive_points_2017(fiber, protein, fruits_veg):
    """Calculate total positive points based on 2017 algorithm."""
    fiber_points = 0 if fiber <= 0.9 else 1 if fiber <= 1.9 else 2 if fiber <= 2.8 else 3 if fiber <= 3.7 else 4 if fiber <= 4.7 else 5
    protein_points = 0 if protein <= 1.6 else 1 if protein <= 3.2 else 2 if protein <= 4.8 else 3 if protein <= 6.4 else 4 if protein <= 8 else 5
    fruits_veg_points = 0 if fruits_veg < 40 else 1 if fruits_veg <= 60 else 2 if fruits_veg <= 80 else 5
    return fiber_points + protein_points + fruits_veg_points




def nutriscore_2017_Master(energy, saturated_fat, sugars, sodium, fiber, protein, fruits_veg):
    """Calculate total points including conditions based on 2017 algorithm."""
    N = calculate_negative_points_2017(energy, saturated_fat, sugars, sodium)
    P = calculate_positive_points_2017(fiber, protein, fruits_veg)
    fruits_veg_points = 0 if fruits_veg < 40 else 1 if fruits_veg <= 60 else 2 if fruits_veg <= 80 else 5
    Prot = protein_points = 0 if protein <= 1.6 else 1 if protein <= 3.2 else 2 if protein <= 4.8 else 3 if protein <= 6.4 else 4 if protein <= 8 else 5
    if N >= 11: #takes in account the >11N rule
        if fruits_veg_points >= 5:
            return N - P
        else:
            return N - P + Prot #Excludes protein from positive points when there is <5 fruits and veg.
    else:
        return N - P
    

