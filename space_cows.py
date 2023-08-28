#reading data from file
cows, weights = [], []
file = open('ps1_cow_data.txt')
for i in file:
    x, y = i.split(',')
    cows.append(x)
    weights.append(int(y))
file.close()


#cow
class Cow(object):
    def __init__(self, n, w):
        self.name = n
        self.weight = w
    def get_name(self):
        return self.name
    def get_weight(self):
        return self.weight
    def __str__(self):
        return ('Name: '+self.name+', Weight: '+str(self.weight))
#creating list of Objects for futher algorithm  
cow_list = []
for i in range(len(cows)):
    cow_list.append(Cow(cows[i], weights[i]))

#greedy algorithm for this case
def greedy_alien(list, max_load, key_func):
    #sort list based on key descending
    cows_s = sorted(list, key=key_func, reverse=True)
    total_load = 0.0
    taken, not_taken = [], []
    for i in range(len(cows_s)):
        #if there is space for biggest cow put her in
        if(total_load + cows_s[i].get_weight()) <= max_load:
            total_load += cows_s[i].get_weight()
            taken.append(cows_s[i])
        #if she dosen't fit put her in waiting room
        else:
            not_taken.append(cows_s[i])
    #return taken cows, total weight of taken cows, cows in waiting room
    return (taken, total_load, not_taken)

        
def efficient_aliens(list, max_load):
    if list == [] or max_load == 0:
        moved_cows = (0, ())
    elif list[0].get_weight() > max_load:
        moved_cows = efficient_aliens(list[1:], max_load)

    else:
        next_cow = list[0]
        taken_weight, taken_cows = efficient_aliens(list[1:], max_load - next_cow.get_weight())
        taken_weight += next_cow.get_weight()
        
        left_weight, left_cow = efficient_aliens(list[1:], max_load) #, memory
        if taken_weight > left_weight:
            moved_cows = (taken_weight, taken_cows + (next_cow,))
        else:
            moved_cows = (left_weight, left_cow)
    return moved_cows

  
def test_greedy(list, load, key_func, to_print = True):
    print('---Greedy aliens---')
    trip = 0
    while(list !=[]):
        taken, value, list = greedy_alien(list, load, key_func)
        trip += 1
        if to_print:
            print(' Trip no.', trip)
            print('  Toral load:', value)
            for i in taken:
                print('    ', i)
    return trip
                
def test_efficient(list, load, to_print = True):
    print("---Efficient aliens---")
    trip = 0
    while(list !=[]):
        value, taken = efficient_aliens(list, load)
        trip += 1
        left_cows = []
        for i in list:
            if i not in taken:
                left_cows.append(i)
        if to_print:
            print(' Trip no.', trip)
            print('  Total load:', value)
            for cow in list:
                print('    ', cow)
        list = left_cows
    return trip

def conclusion(t1, t2, time1, time2):
    print('---Execution time---')
    print(' Greedy:', time1, 'Efficient:', time2)
    if time1 < time2:
        print('  Fastest: Greedy by', time2-time1, 's')
    elif time1 > time2:
        print('  Fastest: Efficient by', time1-time2, 's')
    else:
        print(' Tie')
    
    print('---Number of trips---')
    print(' Greedy:', t1, 'Efficient:', t2)
    if t1 < t2:
        print('  Least trips: Greedy by', t2-t1, 'trip(s)')
    if t1 > t2:
        print('  Least trips: Efficient by', t1-t2, 'trip(s)')
    else:
        print('  Tie')   

import time    

start = time.time()
t1 = test_greedy(cow_list, 10, Cow.get_weight)
stop = time.time()

start1 = time.time()
t2 = test_efficient(cow_list, 10)
stop1 = time.time()

conclusion(t1, t2, stop-start, stop1-start1)