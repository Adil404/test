string = 'saveChangesInTheEditor'


index = 0
count = 0
if string[index].islower() == True:
    count += 1
for i in range(len(string)):
    if string[index].isupper() == True:
        count += 1
        index += 1
print(count)
print(len(string))    