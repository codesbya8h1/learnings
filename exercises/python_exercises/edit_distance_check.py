def are_equal_or_close(s1, s2):
    s1, s2 = s1.lower(), s2.lower()
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    distances = range(len(s1) + 1)
    print("initial distances :", distances)
    for i2, c2 in enumerate(s2):
        distances_ = [i2+1]
        print("distances_ :", distances_)
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                distances_.append(distances[i1])
            else:
                distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
            print("distances_ updated:",distances_)
        distances = distances_
        print("distances :",distances)
    
    return distances[-1] <= 1

print(are_equal_or_close('abc', 'ac'))