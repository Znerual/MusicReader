class Test:
    def findJumps(self, rawData, maxDist):
        for i in range(0, len(rawData)-1):
            delta = map(lambda x,y: x-y, rawData[i], rawData[i+1])
            for entry in delta:
                if (entry > maxDist):
                    print("Found jump at index " + str(i))
                    return False
        return True
