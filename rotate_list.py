# Add your clarifying questions here

# is "shift-by" number always positive?
# is "shift-by" number always shift to the right? Yes
# can "shift-by" number be zero? 
# can "shift-by" number be bigger than the list length?
# Empty or 1-element list?

# list = [1,2,3] , 4
# list = [3,1,2]
# index + shiftby //length
# 0+4=4 
# res 4,3 = 1

def rotate_list(list, shift_by):
    if shift_by < 0:
        return f"Shift_by number should be positive integer!"

    length = len(list)
    result_list = [None] * length

    # iterate over list items and move each item by shift_by number
    # add the new item in new location to the new result_list
    # return the result_list

    for index in range(length):
        new_index = (index + shift_by) % length
        result_list[new_index] = list[index]

    return result_list

# Hard mode:

def rotate_list(list, shift_by):
    length = len(list)
    shift_by = shift_by % length  # handle shifts larger than list size
    return list[-shift_by:] + list[:-shift_by]


print(rotate_list([1,2,3,4,5] , 4))