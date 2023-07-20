def fib_efficient(n, d):
    if n in d:            #if n exist in dictionary
        return d[n]       #return answer for key n
    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        d[n] = ans  #key n in dictionary equals ans
        return ans
    
dictionary = {1:1, 2:2}
print(fib_efficient(666, dictionary))

#uncoment for look to all numbers calculated:
#print(dictionary)

#do a lookup first in case already calculated the value
#modify dictionary as progress through function calls