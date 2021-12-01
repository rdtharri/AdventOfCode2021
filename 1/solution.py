import pyperclip


def main():

    with open("input.txt") as f:
        measurements = [int(measurement) for measurement in f.readlines()]

    larger = 0
    for i in range(1, len(measurements)):
        if measurements[i] > measurements[i - 1]:
            larger += 1

    print(f"Solution 1: {larger}")
    pyperclip.copy(larger)

    larger = 0
    for i in range(3, len(measurements)):
        if sum(measurements[(i - 2) : (i + 1)]) > sum(measurements[(i - 3) : i]):
            larger += 1

    print(f"Solution 2: {larger}")
    pyperclip.copy(larger)


if __name__ == "__main__":
    main()
