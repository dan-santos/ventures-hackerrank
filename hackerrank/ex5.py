# https://www.geeksforgeeks.org/count-items-common-lists-different-prices/

# O(1+n) = O(n) de complexidade de tempo
# O(1) para complexidade de espaço

if __name__=='__main__':
    list1 = [("apple", 60), ("bread", 20), ("wheat", 50), ("oil", 30)]
    list2 = [("milk", 20), ("bread", 15), ("wheat", 40), ("apple", 60)]

    # O(2n) = O(n)
    list1 = dict(list1)
    list2 = dict(list2)
    count = 0

    # O(n)
    for key in list1.keys():
        # O(1)
        if key in list2 and list1[key] != list2[key]:
            count += 1

    print(count)

