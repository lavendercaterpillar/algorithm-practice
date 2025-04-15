# Add your clarifying questions here

# what if building list is empty?
# what if bldg list has only 1 item?
# Can we see the negative bldg? No
# Can we include 0-level bldg? 
# Can we see shorter bldgs behind highrises? No
# if two bldgs with same length, do we see both or just one of them? Just 1
# Are we looking from the first item of the list or another index? 1st

def skyline(building_list):
    # Loop over all items in the bldg list,
    # starting from first item in the list we should compare the item height 
    # with ground level (viewer) and with all buildings before it.
    # if heigher than all of them add it to result list.

    # if not building_list:
    #     return []

    # result_list = [building_list[0]]

    # for i in range(1, len(building_list)):
    #     current = building_list[i]

    #     # Skip negative or zero-height buildings
    #     if current <= 0:
    #         continue

    #     # Check if current is taller than ALL previous buildings
    #     if current > max(building_list[:i]):
    #         result_list.append(current)

    # -------------------------------------
    result_list = []

    for i in range(len(building_list)):
        current = building_list[i]

        # Skip non-positive buildings
        if current <= 0:
            continue

        # First valid building
        if not result_list:
            result_list.append(current)
            
        # Add only if strictly taller than all before
        elif current > max(result_list):
            result_list.append(current)

    return result_list


    # second approach:
    # find the position of the maximum height building, 

print(skyline([-1, 1, 3, 7, 7, 3]))
print(skyline([-1, 1, 3, 6, -2, 3]))