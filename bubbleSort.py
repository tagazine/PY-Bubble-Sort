def bubble_sort(lst):
    
    for i in range(len(lst)-1):
        swapped = False
        print(f"interation {i}")
        for j in range(len(lst)-1):
            print(f"compare {lst[j]} with {lst[j+1]}")
            if lst[j] > lst[j+1]:
                swapped = True
                lst[j], lst[j+1] = lst[j+1], lst[j]
        if swapped == False:
            return
    return lst

sample_list = [10, 100, 35, 567, 2, 99]
print(f"Unsorted list: {sample_list}")
bubble_sort(sample_list)
print(f"Sorted list: {sample_list}")
