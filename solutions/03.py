import os

script_dir = os.path.dirname(__file__)
rel_path = '../inputs/03.txt'


def read_lines_with_context(filename):
    prev_line, current_line = None, None
    with open(filename, 'r', encoding='utf-8') as file:
        for next_line in file:
            next_line = next_line.rstrip('\n')
            if current_line:
                yield (prev_line, current_line, next_line)
            prev_line, current_line = current_line, next_line
        yield (prev_line, current_line, None)

def is_special_char(char):
    return not char is None and not char.isnumeric() and char != '.'

def is_special_character_surrounding(index, prev_line, current_line, next_line):
    if prev_line is None: prev_line = ['.'] * len(current_line)
    if next_line is None: next_line = ['.'] * len(current_line)

    surrounding_chars = [
        prev_line[index] if index < len(prev_line) else None,
        prev_line[index + 1] if index + 1 < len(prev_line) else None,
        prev_line[index - 1] if index - 1 >= 0 else None,
        current_line[index - 1] if index - 1 >= 0 else None,
        current_line[index + 1] if index + 1 < len(current_line) else None,
        next_line[index],
        next_line[index + 1] if index + 1 < len(next_line) else None,
        next_line[index - 1] if index - 1 >= 0 else None
    ]
    return any(is_special_char(char) for char in surrounding_chars)


def parse_number_at(index, text):
    if not text[index].isnumeric(): return None
    parsing_forward = True
    parsing_backward = True
    number_string = text[index]
    forward_index = index
    backward_index = index

    while parsing_forward or parsing_backward:
        forward_index += 1
        backward_index -= 1

        if not parsing_forward or forward_index >= len(text) or not text[forward_index].isnumeric():
            parsing_forward = False
        else:
            number_string += text[forward_index]

        if not parsing_backward or backward_index < 0 or not text[backward_index].isnumeric():
            parsing_backward = False
        else:
            number_string = text[backward_index] + number_string

    return number_string

def get_numbers_surrounding(index, prev_line, current_line, next_line):
    numbers = []

    if prev_line is not None:
        number_above = parse_number_at(index, prev_line)

        if number_above is not None:
            numbers.append(number_above)
        else:
            left_above = parse_number_at(index - 1, prev_line)
            right_above = parse_number_at(index + 1, prev_line)
            if left_above is not None: numbers.append(left_above)
            if right_above is not None: numbers.append(right_above)

    current_line_left = parse_number_at(index - 1, current_line)
    current_line_right = parse_number_at(index + 1, current_line)
    if current_line_left is not None: numbers.append(current_line_left)
    if current_line_right is not None: numbers.append(current_line_right)

    if next_line is not None:
        number_below = parse_number_at(index, next_line)

        if number_below is not None:
            numbers.append(number_below)
        else:
            left_below = parse_number_at(index - 1, next_line)
            right_below = parse_number_at(index + 1, next_line)
            if left_below is not None: numbers.append(left_below)
            if right_below is not None: numbers.append(right_below)

    return numbers


def main ():
    sum1 = 0

    for prev_line, current_line, next_line in read_lines_with_context(os.path.join(script_dir, rel_path)):
        number_string_so_far = ""
        is_current_number_valid = False

        for index, char in enumerate(current_line):
            next_char = current_line[index + 1] if index + 1 < len(current_line) else None
            if not char.isnumeric(): continue

            number_string_so_far += char
            if not is_current_number_valid: is_current_number_valid = is_special_character_surrounding(index, prev_line, current_line, next_line)
            if next_char is None or not next_char.isnumeric():
                if is_current_number_valid: sum1 += int(number_string_so_far)

                number_string_so_far = ""
                is_current_number_valid = False
    print('Part 1:', sum1)


    sum2 = 0


    for prev_line, current_line, next_line in read_lines_with_context(os.path.join(script_dir, rel_path)):


        for index, char in enumerate(current_line):
            if char != '*': continue

            numbers = get_numbers_surrounding(index, prev_line, current_line, next_line)

            if len(numbers) != 2: continue

            sum2 += int(numbers[0]) * int(numbers[1])

    print('Part 2:', sum2)

main()
