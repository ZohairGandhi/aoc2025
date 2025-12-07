def largest_joltage(bank: str) -> int:
    max_num = -1
    max_idx = 0
    max_num_prior = -1
    max_num_after = -1

    for idx, battery in enumerate(bank):
        if int(battery) > max_num:
            max_num = int(battery)
            max_idx = idx

    for battery in bank[0:max_idx]:
        if int(battery) > max_num_prior:
            max_num_prior = int(battery)

    for battery in bank[max_idx + 1 :]:
        if int(battery) > max_num_after:
            max_num_after = int(battery)

    voltage_a = (max_num_prior * 10 + max_num) if max_num_prior != -1 else 0
    voltage_b = (max_num * 10 + max_num_after) if max_num_after != -1 else 0

    return voltage_a if voltage_a > voltage_b else voltage_b


with open("input.txt") as input_file:
    total_joltage = 0

    for line in input_file:
        max_joltage = largest_joltage(line.strip())
        total_joltage += max_joltage

    print(total_joltage)
