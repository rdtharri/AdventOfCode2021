import pyperclip


def main():

    with open("input.txt") as f:
        instructions = [line.split(" ") for line in f.readlines()]

    x = 0
    d = 0
    for instruction in instructions:
        if instruction[0] == "forward":
            x += int(instruction[1])
        elif instruction[0] == "down":
            d += int(instruction[1])
        elif instruction[0] == "up":
            d -= int(instruction[1])

    print(f"X Pos: {x}")
    print(f"Depth: {d}")
    print(f"Solution: {x*d}")
    pyperclip.copy(x * d)

    x = 0
    d = 0
    aim = 0
    for instruction in instructions:
        if instruction[0] == "forward":
            x += int(instruction[1])
            d += aim * int(instruction[1])
        elif instruction[0] == "down":
            aim += int(instruction[1])
        elif instruction[0] == "up":
            aim -= int(instruction[1])

    print(f"X Pos: {x}")
    print(f"Depth: {d}")
    print(f"Aim: {aim}")
    print(f"Solution: {x*d}")
    pyperclip.copy(x * d)


if __name__ == "__main__":
    main()
