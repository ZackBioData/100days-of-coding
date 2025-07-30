counts = [16419, 17757, 17409, 18294, 17135, 16551]
weights = [1.0, 1.0, 1.0, 0.75, 0.5, 0.0]

expected_dominant_offspring = sum(2 * count * prob for count, prob in zip(counts, weights))
print(expected_dominant_offspring)