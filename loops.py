
# 1.Basic: Print all integer from 0 to 150
for i in range(0,151,1):
    print(i)

print("***********End of Exercise 1 *************")

# 2.Multiples of Five: Print all the multiplies of 5 from 5 to 1000

for i in range(0, 1001, 5):
    print(i)

print("***********End of Exercise 2 *************")

# 3.Counting, the Dojo Way: Print integers 1 to 100. If divisible by 5,
# print "Coding" instead. If divisible by 10, print "Coding Dojo"

for i in range(1,101,1):
    if i%10==0:
        print("Coding Dojo")
    elif i%5==0:
        print("Coding")
    else:
        print(i)

print("***********End of Exercise 3 *************")

# 4.Whoa. That Suchker's Huge: Add odd integers from 0 to 500000 and print the final sum

total =0

for i in range (1, 500000, 1):
    if i%2!=0:
        total+=i

print(total)

print("***********End of Exercise 4 *************")
#5. Countdown by Fours - Print positive numbers starting at 2018, counting down by fours

i=2018

while i>0:
    print(i)
    i-=4

print("***********End of Exercise 5 *************")

#6. Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum,
#  print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, 
# the loop should print 3, 6, 9 (on successive lines)

lowNum=3
highNum=9
mult=3

for i in range (0, highNum, 1):
    if mult*i>=lowNum and mult*i<=highNum:  #3*0=0
        print(mult*i)

print("***********End of Exercise 6*************")
