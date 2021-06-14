#Reverse a Number Mathematically


number = 865
revs_num = 0


while (number > 0):
    remainder = number % 10
    revs_num = (revs_num * 10) + remainder
    number = number // 10

var_rimrzesx = 'reversed num of given num is'

print(var_rimrzesx,revs_num,) #reversed Number