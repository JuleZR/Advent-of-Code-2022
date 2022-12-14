"""
Advent of Code 2022
Day     11
"""


def parse(filename):
    with open(filename, 'r') as file:
        lines = [line.strip('\n') for line in file.readlines()]

        # Get Monkeys
        monkeys = []
        raw_monkeys = lines[0::7]
        for m_name in raw_monkeys:
            m_name = m_name[7:8]
            monkeys.append(m_name)
        monkeys = list(map(int, monkeys))

        # Get Startingitems for monkeys
        starting_items = []
        raw_items = lines[1::7]
        for item in raw_items:
            item = item[18:]
            item = item.replace(' ', '')
            item = item.split(',')
            item = list(map(int, item))
            starting_items.append(item)

        # Get operation
        operation = []
        raw_operation = lines[2::7]
        for op in raw_operation:
            op = op[23:]
            op = op.split(' ')
            operation.append(op)

        # Get Test
        tests = []
        raw_test = lines[3::7]
        raw_true = lines[4::7]
        raw_false = lines[5::7]
        for idx, test in enumerate(raw_test):
            test = int(test[21:])
            true_c = raw_true[idx][29:]
            false_c = raw_false[idx][30:]
            tests.append([test, {True: int(true_c), False: int(false_c)}])

        # Make Dataset
        m_dict = {}
        for i, monkey in enumerate(monkeys):
            m_dict[monkey] = {
                'items': starting_items[i],
                'op': operation[i],
                'test': tests[i],
                'inspected': 0
            }
    return m_dict


def calc_worry(item_level: int, operator: str, op_value: str):
    if op_value == 'old':
        op_value = item_level
    match operator:
        case '+':
            return item_level + int(op_value)
        case '-':
            return item_level - int(op_value)
        case '*':
            return item_level * int(op_value)
        case '/':
            return item_level / int(op_value)


def is_devisable_by(c_worry: int, devisor: int):
    if c_worry % devisor == 0:
        return True
    else:
        return False


def product(*args):
    product = 1
    for a in args:
        product *= a
    return product


def get_monkey_buissness(inspected: list):
    inspected.sort(reverse=True)
    inspected = inspected[0:2]
    buisness = product(*inspected)
    print('=== PART 1 ===')
    print(f"Monkey buissness = {buisness}")


def part_one(monkey_dict: dict):
    for _ in range(20):
        for monkey in monkey_dict:
            for idx, item in enumerate(monkey_dict[monkey]['items']):
                # calculate worry level
                op = monkey_dict[monkey]['op'][0]
                multiplyer = monkey_dict[monkey]['op'][1]
                worry_level = calc_worry(item, op, multiplyer)

                c_worry = int(worry_level / 3)

                devisor = monkey_dict[monkey]['test'][0]
                devide_chk = is_devisable_by(c_worry, devisor)

                target_monkey = monkey_dict[monkey]['test'][1][devide_chk]
                monkey_dict[target_monkey]['items'].append(c_worry)

                monkey_dict[monkey]['inspected'] += 1

                if idx == len(monkey_dict[monkey]['items']) - 1:
                    monkey_dict[monkey]['items'] = []

    monkey_inspected = []
    for monkey in monkey_dict:
        inspect = monkey_dict[monkey]['inspected']
        monkey_inspected.append(inspect)
    get_monkey_buissness(monkey_inspected)


def main():
    """ Main function"""
    p_input = parse('day11_input.txt')
    part_one(p_input)


if __name__ == "__main__":
    main()
