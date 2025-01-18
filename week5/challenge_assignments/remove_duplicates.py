"""
Description: Remove duplicate elements from a list, preserving the original order of elements.
Input Arguments:
lst (list): A list of elements that may contain duplicates.
"""

def remove_duplicates(lst): 
    unique_list = []
    for i in lst: 
        if i not in unique_list: 
            # use addition operator...
            unique_list += [i]
            # ...or use .append()
            # unique_list.append(i)

    return unique_list
