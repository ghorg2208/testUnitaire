def average(values):
    return sum(values) / len(values)

def get_minimum(values):
    if not values:
        return None
    minimum = values[0]
    for value in values:
        if value < minimum:
            minimum = value
    return minimum