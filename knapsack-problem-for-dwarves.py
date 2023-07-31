#class for data to compute
class Ore(object):
    def __init__(self, name, value, weight):
        self.ore = name
        self.val = value
        self.wei = weight
    def getName(self):
        return self.ore
    def getValue(self):
        return self.val
    def getWeight(self):
        return self.wei
    def getDensity(self):
        return (self.val/self.wei)
    def __str__(self):
        return 'Ore: '+str(self.ore)+', Value: '+str(self.val)+', Weight: '+str(self.wei)

#create dataset for algorithm from provided tables
def db_create(ore, val, kg):
    db = []
    for i in range(len(ore)):
        db.append(Ore(ore[i], val[i], kg[i]))
    return db
#example tables
ores = ['gold', 'iron', 'silver', 'platinum', 'bronze', 'copper', 'nickel', 'aluminium']
value = [ 100, 20, 70, 90, 5, 35, 25, 30]
weight = [ 19.3, 7.8, 10.5, 21.4, 8.3, 8.9, 8.9, 2.7]
#function for adding more of existing item
def add_amount(i, orginal_position):
    while i > 0:
        ores.append(ores[orginal_position])
        value.append(value[orginal_position])
        weight.append(weight[orginal_position])
        i -= 1
'''
add_amount(10, 0) #add gold
add_amount(10, 1) #add iron
add_amount(10, 2) #add silver
add_amount(10, 3) #add platinum
add_amount(10, 4) #add bronze
add_amount(10, 5) #add copper
add_amount(10, 6) #add nickel
add_amount(10, 7) #add aluminum
'''
minerals = db_create(ores, value, weight)

#uncomment to see dataset
'''
for i in range(len(minerals)):
    print(minerals[i])
'''
#Algorithm:
#takes prepared set of data and maximal weight of items, creates dictionary for computed items
def maxProfit(items, max_weight, memory={}):
    #if result exist in dictionary return answer instead od computing it again
    if (len(items), max_weight) in memory:
        result = memory[(len(items), max_weight)]
    #if given data is empty or weight is 0 return 0 and empty tuple
    elif items == [] or max_weight == 0:
        result = (0, ())
    #if first item is heavier than given maximum jump to next item
    elif items[0].getWeight() > max_weight:
        result = maxProfit(items[1:], max_weight, memory)
    else:
        #save first item to buffor
        nextItem = items[0]
        #repeat function without first item and lower max_weight by weight of first item
        withVal, withToTake = maxProfit(items[1:], max_weight - nextItem.getWeight(), memory)
        #adds up total value for case when item is taken
        withVal += nextItem.getValue()
        #compute for case of not taking an item
        withoutVal, withoutToTake = maxProfit(items[1:], max_weight, memory)
        #return case with higher value
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    #set data in resoult as data in current cell in dictionary
    memory[(len(items), max_weight)] = result
    return result
#show result in user-friendly way
def showResult(data, max_weight, printItems = True):
    print('Generating most profitable load list for '+str(max_weight)+'kg ...')
    val, taken = maxProfit(data, max_weight)
    
    print('Total value of items to take:', val)
    if printItems:
        for item in taken:
            print('  ', item)
            
showResult(minerals, 100)
