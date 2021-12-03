import pyperclip
from collections import Counter


def main():

    with open("input.txt") as f:
        diagnostics = [line.strip() for line in f.readlines()]

    counters = []
    for i in range(len(diagnostics[0])):
        counters.append(Counter())

    for diag in diagnostics:
        for i, elem in enumerate(diag):
            counters[i].update([elem])

    gamma = ""
    eps = ""
    for counter in counters:
        com = counter.most_common(2)
        gamma += com[0][0]
        eps += com[1][0]

    print(f"gamma:    {gamma}")
    print(f"epsilon:  {eps}")
    print(f"solution: {int(gamma,2) * int(eps,2)}")
    pyperclip.copy(int(gamma, 2) * int(eps, 2))

    oxygen_found = False
    co2_found = False

    oxygen_list = diagnostics
    co2_list = diagnostics

    for i in range(len(diagnostics[0])):

        if not oxygen_found:

            counter = Counter()
            for diag in oxygen_list:
                counter.update(diag[i])

            m_com = counter.most_common(2)[0]
            l_com = counter.most_common(2)[1]

            com = m_com[0]
            if m_com[1] == l_com[1]:
                com = "1"

            oxygen_list_copy = []
            for diag in oxygen_list:
                if diag[i] == com:
                    oxygen_list_copy.append(diag)

            if len(oxygen_list_copy) == 1:
                oxygen_found = True
                oxygen = oxygen_list_copy[0]
            else:
                oxygen_list = oxygen_list_copy

        if not co2_found:

            counter = Counter()
            for diag in co2_list:
                counter.update(diag[i])

            m_com = counter.most_common(2)[0]
            l_com = counter.most_common(2)[1]

            com = l_com[0]
            if m_com[1] == l_com[1]:
                com = "0"

            co2_list_copy = []
            for diag in co2_list:
                if diag[i] == com:
                    co2_list_copy.append(diag)

            if len(co2_list_copy) == 1:
                co2_found = True
                co2 = co2_list_copy[0]
            else:
                co2_list = co2_list_copy

    if not oxygen_found:
        oxygen = oxygen_list[0]
    if not co2_found:
        co2 = co2_list[0]

    print(f"oxygen:   {oxygen}")
    print(f"co2:      {co2}")
    print(f"solution: {int(oxygen,2) * int(co2,2)}")
    pyperclip.copy(int(oxygen, 2) * int(co2, 2))


if __name__ == "__main__":
    main()
