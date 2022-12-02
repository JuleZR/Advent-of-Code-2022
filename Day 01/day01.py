""" Riddle Day 1"""

from itertools import groupby

def calc_calories() -> list:
    """Reads day1_input.txt line by line, splits the individual values into
    a list of lists, sums them up, outputs the highest value and returns the
    list of all values.

    Returns:
        list: List of all summed up callory values
    """
    int_list = []
    with open('day01_input.txt', 'r', encoding='utf8') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            line = int(line) if line != "" else ''
            int_list.append(line)
        callory_list = [list(cont) for ele, cont in groupby(int_list, key=bool) if ele]
        sum_list = [(sum(l)) for l in callory_list]
        print(max(sum_list))
        return sum_list

def calc_top_three(list_of_value:list):
    """Sorts a list of calorie values backwards, and prints the sum of the three
    largest values

    Args:
        list_of_value (list): List of all summed up callory values
    """
    sorted_values = sorted(list_of_value, reverse=True)
    top_3 = sum(sorted_values[:3])
    print(top_3)

def main():
    """Main Function"""
    luggage = calc_calories()
    calc_top_three(luggage)

if __name__ == '__main__':
    main()
    