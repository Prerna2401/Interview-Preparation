def intersect(self, arr1, arr2):
        intersection = []
        i, j = 0, 0  # Pointers for both arrays
    
        while i < len(arr1) and j < len(arr2):
            if arr1[i] == arr2[j]:
                intersection.append(arr1[i])
                i += 1
                j += 1
            elif arr1[i] < arr2[j]:
                i += 1
            else:
                j += 1
    
        return intersection