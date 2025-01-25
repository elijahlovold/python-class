def wait_for_user_start() -> bool: 
    option = input("Press enter to begin or q to quit")

    return option != "q"
