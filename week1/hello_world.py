from time import sleep

def animate_string(string, iterations=5, delay=0.5):
    str_size = len(string)
    for _ in range(iterations): 
        for _ in range(str_size):
            print(' ' + string, end='', flush=True)
            print('\r', end='', flush=True)
            sleep(delay)

            string = string[-1] + string[:-1]

    print(' ' + string)

animate_string("Hello World! ", iterations=2, delay=0.12)
