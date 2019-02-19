import math


def bin_search(li, element):
    bottom = 1
    top = len(li)
    index = 0
    while top >= bottom: #option without break: and index == 0
        mid = int(math.floor((top+bottom)/2.0))
        if li[mid] == element:
            index = mid
            break
        elif li[mid] > element:
            top = mid-1
        else:
            bottom = mid+1

    return index

li = [2,5,7,9,11,17,222]
print(bin_search(li, 11))
print(bin_search(li, 2))

