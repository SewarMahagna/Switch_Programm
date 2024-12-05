from QuickSort import QuickSort

def division_sort(arr):

    divided_by_5_3 = [x for x in arr if x%15==0]
    divided_by_5 = [x for x in arr if (x%5==0 and x%3!=0)]
    divided_by_3 = [x for x in arr if (x%3==0 and x%5!=0)]
    rest = [[x for x in arr if not (x%3==0 or x%5==0)]]

    divided_by_5_3= QuickSort(divided_by_5_3)
    divided_by_5= QuickSort(divided_by_5)
    divided_by_3= QuickSort(divided_by_3)
    rest = QuickSort(rest)

    divided_by_5_3.extend(divided_by_5)
    divided_by_5_3.extend(divided_by_3)
    divided_by_5_3.extend(rest)

    return divided_by_5_3

test1 = QuickSort([5,3,16,15,17,25,27,29,15,4,8,6,3,9])
print(test1)


def Sort_by_Num_Of_digits(arr):
    new_arr = [str(element) for element in arr]
    