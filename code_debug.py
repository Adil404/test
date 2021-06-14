testcase = int(input(range(1, 10 ** 5)))
tem,tem1,tem2= 1,1,1
x = list(map(float, input().split()))
print(":\n ", x)
x1 = list(map(float, input().split()))
print(":\n ", x1)
x2 = list(map(float, input().split()))
print(":\n ", x2)

for i in x:
    tem = tem * i
var2 = round(100/tem, 2)
if var2 < 9.58:
    print("yes")
else:
    print("no")
for j in x1:
    tem1 = tem1 * j
var = round(100/tem1, 2)
if var < 9.58:
    print("yes")
else:
    print("no")
for k in x2:
    tem2 = tem2 * k
var1 = round(100/tem2, 2)
if var1 < 9.58:
    print("yes")
else:
    print("no")
while testcase == testcase:
    testcase -= 1
    if testcase == 0:
        break
