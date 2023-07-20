#block for testing errors
try:
    a=int(input("Give me number: "))
    b=int(input("Give me second number: "))
    print("a/b = ", a/b)
    print("a+b = ", a+b)
#prints this output when program fails becouse of input value being incorret
except ValueError:
    print("Could not convert to a number.")
#prints this output when provided divisor equals 0
except ZeroDivisionError:
    print("Can't divide by zero")
#prints this output when program fails from diffrent error
except:
    print("Something went wrong")
#prints this output alwyas at the end of try
finally:
    print("Good bye!")