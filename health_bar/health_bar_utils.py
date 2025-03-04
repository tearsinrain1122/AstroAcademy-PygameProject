
class ZeroOrNegativeRatio(Exception):
    # Test for 0 or negative ratio
    pass


class NonNumericRatio(Exception):
    # Test non numeric ratio
    pass


class NonIntHealth(Exception):
    # Test for non integer health
    pass


# Calculating width of health bar in game window
def calculate_health_bar_width(health, ratio):
    if type(ratio) is not int and type(ratio) is not float:
        raise NonNumericRatio("Check initial health stats - health_ratio must be numeric.")

    if ratio <= 0:
        raise ZeroOrNegativeRatio("Check initial health stats - health_ratio must be > 0.")

    if type(health) is not int:
        raise NonIntHealth("Check health stats - health and health reduction must be integers.")

    return health / ratio
