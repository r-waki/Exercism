def transform(legacy_data):
    new_data = {}
    for point, words in legacy_data.items():
        for word in words:
            new_data[word.lower()] = point
    return new_data
