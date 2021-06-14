### Sequential search is a a method for finding an element within a list


def search(lst, item):
    pos = 0
    found = False



    while pos < len(lst) and not found:
        if lst[pos] == item:
            found = True
            break

        else:
            pos += 1
    return found


print(search([1,3,4,3], 4))   # True 
print(search([1,3,2,3,5,6], 9)) # False





