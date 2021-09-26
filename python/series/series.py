def slices(series, length):

    if length > len(series) or length <= 0:
        raise ValueError("Error!")

    return [series[n-length:n] for n in range(length, len(series)+1)]
