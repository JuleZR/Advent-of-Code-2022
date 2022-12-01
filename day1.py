""" Riddle Day 1"""

from itertools import groupby

def calc_luggage():
    int_list = []
    with open('day1_input.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            line = int(line) if line != "" else ''
            int_list.append(line)
        luggage_list = [list(cont) for ele, cont in groupby(int_list, key=bool) if ele]
        sum_list = [(sum(l)) for l in luggage_list]
        print(max(sum_list))
        return sum_list

def calc_top_three(list_of_value:list):
    sorted_values = sorted(list_of_value, reverse=True)
    top_3 = sum(sorted_values[:3])
    print(top_3)

def main():
    luggage = calc_luggage()
    calc_top_three(luggage)

if __name__ == '__main__':
    main()