def zero_fuel(distance_to_pump, mpg, fuel_left):
    if fuel_left * mpg - distance_to_pump >= 0:
        return True
    return False