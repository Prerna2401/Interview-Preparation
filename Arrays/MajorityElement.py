def majorityElement(a):
        n = len(a)
        frequency_dict = {}
    
        for i, element in enumerate(a):
            if element in frequency_dict:
                frequency_dict[element] += 1
            else:
                frequency_dict[element] = 1

            if frequency_dict[element] > n // 2:
                return element
        return None