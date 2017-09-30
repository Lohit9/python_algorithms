class LRUCache(object):

    def __init__(self, capacity=0):
        """
        :type capacity: int
        """
        #lets use an hash map/dictionary
        self.capacity = capacity
        self.LRUDict = dict()

    def getKey(self): #{4a7:2}
        inputDict = self.LRUDict
        keys = inputDict.keys()
        keysList = []
        res = ''
        for each in keys:
            while(each != 'a'):
                res += each
            if (each == 'a'):
                keysList.append(res)
        return keysList

    def getValues(self):
        inputDict = self.LRUDict
        keys = inputDict.keys()
        valuesList = []
        res = ''
        for index,each in enumerate(keys):
            if(each == 'a'):
                res = valuesList[index+1:]
                valuesList.append(res)
        return valuesList

    def get(self, key):
        """
        :rtype: int
        """
        keys = getKey(self)
        values = getValues(self)
        for index,num in keys:
            if key == keys :
                return values[index]
        return -1

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        keys = getKey(self)
        if key not in keys:
            self.LRUDict[str(key)+'a'+value] = 0
            self.capacity += 1
        else:
             popularElems = self.LRUDict.values()
            #  print popularElems
             popularElems.sort()
             del popularElems[-1]
             self.LRUDict[str(key)+'a'+value] = 0
