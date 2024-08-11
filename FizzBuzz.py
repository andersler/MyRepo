'''
loop 100 times (i)

    if i div 3 & 5: print "FizzBuzz"
    if i div 3: print "Fizz"
    if i div 5: print "Buzz"
'''

NUMBER_OF_ITERATIONS = 100
FIZZBUZZ = "FizzBuzz"
FIZZ = "Fizz"
BUZZ = "Buzz"

for i in range(NUMBER_OF_ITERATIONS):
    if (i % 3 == 0 and i % 5 == 0):
        print(f"{i+1}: {FIZZBUZZ}")
    elif i % 3 == 0:
        print(f"{i+1}: {FIZZ}")
    elif i % 5 == 0:
        print(f"{i+1}: {BUZZ}")
