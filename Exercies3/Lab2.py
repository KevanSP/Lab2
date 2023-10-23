def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")
    get_user_input()
def get_user_input():
    userinput = input().split(",")
    userinput = [float(item) for item in userinput]
    print(userinput)
def calc_average():
    print("Float")
def find_min_max():
    print("List of Floats in the format [min_temp, max_temp]")
def sort_temperature():
    print("List of Floats sorted in ascending order")
def calc_median_temperature():
    print("Float")

display_main_menu()