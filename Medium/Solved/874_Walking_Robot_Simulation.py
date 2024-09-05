class Solution:

    def binarySearchPlus(self, array: list[int], key: int, start: int, end: int) -> int:
    
        if start > end:
            if start < len(array):
                return start
            else:
                return -1

        medium = start + (end - start)//2

        if array[medium] == key:
            return -2

        elif array[medium] > key:
            if medium == 0 or array[medium - 1] < key:
                return medium

            return self.binarySearchPlus(array, key, start, (medium - 1))

        elif array[medium] < key:
            return self.binarySearchPlus(array, key, (medium + 1), end)
        

    def binarySearchMinus(self, array: list[int], key: int, start: int, end: int) -> int:

        if start > end:
            if end >= 0:
                return end
            else:
                return -1

        medium = start + (end - start)//2

        if array[medium] == key:
            return -2

        elif array[medium] < key:
            if medium == len(array) - 1 or array[medium + 1] > key:
                return medium

            return self.binarySearchMinus(array, key, (medium + 1), end)

        elif array[medium] > key:
            return self.binarySearchMinus(array, key, start, (medium - 1))


    def robotSim(self, commands: list[int], obstacles: list[list[int]]) -> int:
        
        dictOfX = {}
        obstacles.sort()
        for (obX, obY) in obstacles:
            if obX not in dictOfX:
                dictOfX[obX] = []
            dictOfX[obX].append(obY)
        
        dictOfY = {}
        obstacles.sort(key=lambda x: x[1])
        for (obX, obY) in obstacles:
            if obY not in dictOfY:
                dictOfY[obY] = []
            dictOfY[obY].append(obX)
        
        position = [0,0]

        maxDistance = 0

        direction = 'North'

        for command in commands:

            if command < 0:

                if direction == 'North':
                    if command == -1:
                        direction = 'East'
                    else:
                        direction = 'West'
                
                elif direction == 'East':
                    if command == -1:
                        direction = 'South'
                    else:
                        direction = 'North'

                elif direction == 'South':
                    if command == -1:
                        direction = 'West'
                    else:
                        direction = 'East'

                elif direction == 'West':
                    if command == -1:
                        direction = 'North'
                    else:
                        direction = 'South'
            
            else:

                if direction == 'North':

                    try:
                        listOfOb = dictOfX[position[0]]
                        indexOb = self.binarySearchPlus(listOfOb, position[1], 0, len(listOfOb)-1)
                        print('index:',indexOb)

                        if indexOb == -1 or indexOb == -2 or listOfOb[indexOb] > (position[1] + command):
                            position[1] += command
                        elif listOfOb[indexOb] <= (position[1] + command):
                            position[1] = listOfOb[indexOb] - 1

                    except KeyError:
                        position[1] += command

                
                elif direction == 'East':
                    
                    try:
                        listOfOb = dictOfY[position[1]]
                        indexOb = self.binarySearchPlus(listOfOb, position[0], 0, len(listOfOb)-1)

                        if indexOb == -1 or indexOb == -2 or listOfOb[indexOb] > (position[0] + command):
                            position[0] += command
                        elif listOfOb[indexOb] <= (position[0] + command):
                            position[0] = listOfOb[indexOb] - 1 

                    except KeyError:
                        position[0] += command


                elif direction == 'South':
                    
                    try:
                        listOfOb = dictOfX[position[0]]
                        indexOb = self.binarySearchMinus(listOfOb, position[1], 0, len(listOfOb)-1)

                        if indexOb == -1 or indexOb == -2 or listOfOb[indexOb] < (position[1] - command):
                            position[1] -= command
                        elif listOfOb[indexOb] >= (position[1] - command):
                            position[1] = listOfOb[indexOb] + 1

                    except KeyError:
                        position[1] -= command


                elif direction == 'West':

                    try:

                        listOfOb = dictOfY[position[1]]
                        indexOb = self.binarySearchMinus(listOfOb, position[0], 0, len(listOfOb) - 1)

                        if indexOb == -1 or indexOb == -2 or listOfOb[indexOb] < (position[0] - command):
                            position[0] -= command
                        elif listOfOb[indexOb] >= (position[0] - command):
                            position[0] = listOfOb[indexOb] + 1
                    
                    except KeyError:
                        position[0] -= command


                print(command, position)
                print(command, direction)

                euclidianDistance = (position[0]**2) + (position[1]**2)
                print(command, euclidianDistance)
                print(command, maxDistance)

                if euclidianDistance > maxDistance:
                    maxDistance = euclidianDistance
        
        print('X: ', dictOfX)
        print('Y: ', dictOfY)

        return maxDistance


sol = Solution()
print(sol.robotSim([1,-1,1,-1,1,-1,6],[[0,0]])) 

