def rotate(cur_pos: int, rotation: str) -> int:
    if rotation[0] == "L":
        return (cur_pos - int(rotation[1:])) % 100

    return (cur_pos + int(rotation[1:])) % 100


def count_zeroes_a() -> int:
    cur_pos = 50
    zero_count = 0

    with open("input.txt") as input_file:
        for rotation in input_file:
            cur_pos = rotate(cur_pos, rotation)
            zero_count += 1 if cur_pos == 0 else 0

    return zero_count


def count_zeroes_b() -> int:
    cur_pos = 50
    zero_count = 0

    with open("input.txt") as input_file:
        for rotation in input_file:
            rot_amt = int(rotation[1:])

            for _ in range(rot_amt):
                cur_pos = rotate(cur_pos, f"{rotation[0]}1")

                if cur_pos == 0:
                    zero_count += 1

    return zero_count
