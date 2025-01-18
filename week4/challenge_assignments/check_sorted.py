
def eval_is_sorted(lst: list) -> bool:
    """Check if a list is sorted in ascending order."""
    previous_el = None
    for current_el in lst: 
        # only check if previous_el has been set yet
        if previous_el and current_el < previous_el: 
            return False
        previous_el = current_el

    return True
