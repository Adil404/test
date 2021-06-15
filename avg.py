'''n = 20
# formula to calculate sum
res = n * (n + 1) / 2
print('sum of first', n, 'numbers is:', res)
# Output sum of first 20 numbers is: 210.0

# formula to calculate average
average = (n * (n + 1) / 2) / n
print('Average of first', n, 'numbers is:', average)
# Output Average of 20 numbers is: 10.5'''

## Plus minus program
# test = int(input())
# m1 = list(map(int, input().split()))


# if len(m1) == test:
#     print(m1)
# else:
#     print('write correct number of values')
# count = 0
# count1 = 0
# count2 = 0
# for i in m1:
    

#     if i > 0:
#         count += 1
#     elif i < 0:
#         count1 += 1
#     elif i == 0:
#         count2 += 1
# print('%.6f' % (count/ len(m1)))
# print('%.6f' % (count1/ len(m1)))
# print('%.6f' % (count2/ len(m1)))

def plusMinus(arr):
    # Write your code here
    # test = int(input())
    # m1 = list(map(int, input().split()))


    if len(arr) == n:
        # print(m1)
        count = 0
        count1 = 0
        count2 = 0
        for i in arr:            
            if i > 0:
                count += 1
            elif i < 0:
                count1 += 1
            elif i == 0:
                count2 += 1
    print('%.6f' % (count/ len(arr)))
    print('%.6f' % (count1/ len(arr)))
    print('%.6f' % (count2/ len(arr)))
            

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)


print('hello this is Adil')
