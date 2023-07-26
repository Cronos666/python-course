class Food(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.calories = w
    def getValue(self):
        return self.value
    def getCost(self):
        return self.calories
    def density(self):
        return self.getValue()/self.getCost()
    def __str__(self):
        return self.name+': <'+str(self.value)+',  '+str(self.calories)+'>'

#create menu from lists we provide adapting it to class Food
def buildMenu(names, values, calories):
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i], calories[i]))
    return menu
#the greedy algorithm takes best itmes ( best defined by keyFunction )
#until it runs out of "space", then it take next most valuable item that it can "fit"
def greedy(items, maxCost, keyFunction):
    #create sorted (descending) copy of given list
    itemsCopy = sorted(items, key = keyFunction, reverse=True)
    result = []
    totalValue, totalCost = 0.0, 0.0
    
    for i in range(len(itemsCopy)):
        #if item value is less than provided it's added to list
        if (totalCost+itemsCopy[i].getCost()) <= maxCost:
            result.append(itemsCopy[i])
            totalCost += itemsCopy[i].getCost()
            totalValue += itemsCopy[i].getValue()
    #returns pointer to records in resoult and total value
    return (result, totalValue)

def testGreedy(items, constrait, keyFunction):
    taken, val = greedy(items, constrait, keyFunction)
    print('Total value of itmes taken =', val)
    #prints all items one by one instead of pointers like "print taken" would do
    for item in taken:
        print(' ', item)
#test for different cases of key
def testGreedys(foods, maxUnits):
    print('Use greedy by value to allocate', maxUnits, 'calories')
    testGreedy(foods, maxUnits, Food.getValue)
    
    print('\nUse greedy by cost to allocate', maxUnits, 'calories')
    #lambda create "anonymus" function
    testGreedy(foods, maxUnits, lambda x: 1/Food.getCost(x))
    
    print('Use greedy by density to allocate', maxUnits, 'calories')
    testGreedy(foods, maxUnits, Food.density)
       
names = ['wine', 'beer', 'pizza', 'burger', 'fries', 'cola', 'apple', 'donut', 'cake']
val = [89,100,95,98,90,79,50,10]
kcal = [123,154,258,353,365,150,95,195]
foods = buildMenu(names, val, kcal)

testGreedys(foods, 500)


#lt = greedy(foods, 500, Food.getValue)
#print(lt[0][0])
