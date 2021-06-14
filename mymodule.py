def function(x):
    print('i got', x)
print('this is mymodule file')
print('__name__ is ', __name__)

function(89)
# import tes
# print(tes.myname())
''' okay so basically this is a multiline comment
here you can write unlimited lines '''


def pattern(n):
    for i in range(1, n):
        for j in range(1, i+1):
            print(j, end='')
        print('\r')
pattern(5) 



num = 1
a = 4
b = 2
for i in range(a):
    for j in range(1, b):
        print(num, end=' ')
        num += 1
    print('')
    b += 1
