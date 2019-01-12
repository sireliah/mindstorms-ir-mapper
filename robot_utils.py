
def prox_to_cm(proximity: float) -> float:
    # proximity is in percent
    return proximity * 0.7


def robot_degrees_to_rotations(degrees: int) -> float:
    return float(degrees) * 0.013333333
