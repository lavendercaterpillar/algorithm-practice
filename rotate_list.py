# Add your clarifying questions here

# is "shift-by" number always positive?
# is "shift-by" number always shift to the right? Yes
# can "shift-by" number be zero? 
# can "shift-by" number be bigger than the list length?
# Empty or 1-element list?

# First attempt: Time and Space complex = O(n)
# def rotate_list(list, shift_by):

    # length = len(list)
    # result_list = [None] * length

    # for index in range(length):
    #     new_index = (index + shift_by) % length
    #     result_list[new_index] = list[index]

    # return result_list  

# Hard mode - In place shifting (Gpt assisted!): Time Compl = O(n), Space comp = O(1)
# The idea is slicing the list based on the shift number and then swap

def rotate_list(list, shift_by):
    length = len(list)
    shift_by = shift_by % length  # handle shifts larger than list size; this is where the list is sliced
    return list[-shift_by:] + list[:-shift_by]  #  = [4,5] + [1,2,3]


print(rotate_list([1,2,3,4,5] , 2))