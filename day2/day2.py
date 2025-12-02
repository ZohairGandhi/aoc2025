def is_id_valid(id: str) -> bool:
    if len(id) % 2 != 0:
        return True

    mid_point = len(id) // 2
    return id[:mid_point] != id[mid_point:]


with open("input.txt") as input_file:
    id_ranges = input_file.read().split(",")
    sum = 0

    for id_range in id_ranges:
        [start, end] = id_range.split("-")

        for id in range(int(start), int(end) + 1):
            sum += int(id) if not is_id_valid(str(id)) else 0

    print(sum)
