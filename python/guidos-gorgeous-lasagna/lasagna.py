EXPECTED_BAKE_TIME = 40
PREPARETION_TIME = 2


def bake_time_remaining(elapsed_baking_time, expected_bake_time=EXPECTED_BAKE_TIME):
    '''Return remaining cooking time.
    This function takes a number representing elapsed baking time
    and calculates the remaining minutes cooking the lasagna.
    '''
    return expected_bake_time - elapsed_baking_time


def preparation_time_in_minutes(number_of_layers, preparetion_time=PREPARETION_TIME):
    '''Return preparation cooking time.
    This function takes a number representing the number of layers.
    '''
    return number_of_layers * preparetion_time


def elapsed_time_in_minutes(number_of_layers, elapsed_baking_time, preparetion_time=PREPARETION_TIME):
    '''Return remaining cooking time.
    This function takes two numbers
    representing the number of layers & the time already spent baking
    and calculates the total elapsed minutes spent cooking the lasagna.
    '''
    return number_of_layers * preparetion_time + elapsed_baking_time
