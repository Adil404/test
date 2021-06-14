""" Binary search is an efficient algorithm for finding an iterm from a sorted list of item.
It works by repeatedly dividing in half the portion of the list that could contain the iterm, until you've narrowed down the possible locations to just one."""


def binary_search(lst, item):
    first = 0
    last = len(lst)-1
    found = False


    while(first<=last and not found):
        mid = (first + last)//2
        if lst[mid] == item:
            found = True
        else:
            if item < lst[mid]:
                lst = mid - 1
            else:
                first = mid + 1
    return found


print(binary_search([1,4,3,7,5,6], 3))  # True
print(binary_search([1,2,3,4,5,6], 8))  # False                