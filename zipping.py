from typing import ItemsView


list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
list3 = [1.5, 3.1, 5.7]

# this zips three lists together for the purpose of iterating through them at once
# zips them together into one object
for item in zip(list1, list2, list3):
    l1, l2, l3 = item
    print(l1)
    print(l2)
    print(l3)
# result: first iteration goes through the first value of each lsit then the 2nd then 3rd
