class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        if length == 1:
            if flowerbed[0] == 0:
                return True

        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            n -= 1
            #print(flowerbed)
            #print(n)

        for i in range(1,length-1):
            if flowerbed[i] == 0:
                if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    n -= 1
                #print(flowerbed)
        
        if flowerbed[length-1] == 0 and flowerbed[length-2] == 0:
            flowerbed[length-1] = 1
            n -= 1
            #print(flowerbed)
            #print(n)

        if n <= 0:
            return True
        return False