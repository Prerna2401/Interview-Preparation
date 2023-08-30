def getRow(self, k):
        if k == 0:
            return [1]
        row = [1]
        for i in range(1,k+1):
            for j in range(i,0,-1):
                if j == i:
                    row.append(1)
                else:
                    row[j] = row[j] + row[j-1]
        return row