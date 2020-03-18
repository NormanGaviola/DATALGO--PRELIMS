def __mul__(other1, other2):

    result = 0  # start with vector of zeros
    for a in range(len(other1)):
        result += other1[a] * other2[a]
    return result