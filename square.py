
# ---- Global variables -------------------------------------------------------
N = int(input("\nEnter square size N: ")) # N - lenght of side
LIST = []
NUMBER_LENGTH = len(str(N*N)) # Check how many digits the largest number has

# ---- Class for colours ------------------------------------------------------
class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'

# ---- Functtions ----- -------------------------------------------------------
def count_rooms():
    # Find edge rooms in a given square of size N. Code complexity: 4x4 = 16.
    for i in range(1, N) :
        run_script(i+1) # top side
        run_script(N+N*i) # right side
        run_script(1 + (i-1)*N) # left side
        run_script(N*(N-1)+i) # bottom side

def run_script(number):
    # Output to screen and append to a list
    #print(number)
    LIST.append(number)

def print_image():
    # visualize the results
    print("Initial list:")
    print(LIST)
    LIST.sort()
    print("Sorted list:")
    print(LIST)
    print()
    string = ""

    for i in range(N):
        # top side
        number_block = blokify_number(LIST[i])
        string += bcolors.GREEN + number_block

    string += "\n"

    for i in range(N-2):
        # right & left sides
        number_block = blokify_number(LIST[N+(i*2)]) # right side
        string += number_block
        string += " " + bcolors.YELLOW # offset by 1 space
        for n in range((N-2)*(NUMBER_LENGTH+1)-1): # block_size = NUMBER_LENGTH + 1; and offset by -1
            string += "#" # square filling
        number_block = blokify_number(LIST[N+(i*2)+1]) # left side
        string += bcolors.GREEN + number_block
        string += "\n"

    for i in range(N):
        number_block = blokify_number(LIST[len(LIST)-N+i]) # bottom side
        string += number_block

    print(string)

def blokify_number(number):
    # Create blocks of numbers by appending required amount of empty space in front
    number = str(number)
    block = " "
    for n in range(NUMBER_LENGTH - len(number)):
        block += " "

    number = block + number
    return(number)

# ---- Main -------------------------------------------------------------------
if __name__ == '__main__':
    print("Maximum number length is: %d\nBlock size is: %d\n" % (NUMBER_LENGTH, NUMBER_LENGTH+1))
    count_rooms()
    print_image()
