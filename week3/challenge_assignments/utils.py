def input_int(message: str) -> int: 
    """
        function for inputing an int
    """
    while (True): 
        in_str = input(f"{message} (int): ")
        try: 
            value = int(in_str)
            return value
        except:
            print("invalid input")
