
def prox_to_cm(proximity: float) -> float:
    # Proximity is in percent values, but we want cm.
    return proximity * 0.7


def robot_degrees_to_rotations(degrees: int) -> float:
    # This constant was of course accquired experimentally.
    return float(degrees) * 0.013333333
