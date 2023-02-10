searching_date = 1415
lst = input().split()

def bin_search(lst):
    
    
    left_index = 0
    right_index = len(lst) - 1
    
    while True:
        center_index = int(left_index + (right_index - left_index)/2)
        if int(lst[center_index]) == searching_date:
            return center_index
        elif int(lst[left_index]) == searching_date:
            return left_index
        elif int(lst[right_index]) == searching_date:
            return right_index
        elif int(lst[center_index]) < searching_date:
            left_index = center_index
        elif int(lst[center_index]) > searching_date:
            right_index = center_index
    
print(bin_search(lst)) 