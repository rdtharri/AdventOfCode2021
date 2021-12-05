from dataclasses import dataclass
from typing import List, Dict
import pyperclip

debug = True


@dataclass
class Square:

    value: int
    mark: bool = False


square_record: Dict[int, Square] = {}


class Board:
    def __init__(self, rows: List[List[int]]):

        self.rows: List[List[Square]] = []

        if debug:
            assert len(rows) == 5
            for row in rows:
                assert len(row) == 5

        for row in rows:
            new_row = []
            for elem in row:
                if elem not in square_record.keys():
                    square_record[elem] = Square(elem)
                new_row.append(square_record[elem])
            self.rows.append(new_row)

    def check_win(self):
        for row in self.rows:
            row_win = True
            for sq in row:
                if not sq.mark:
                    row_win = False
                    break
            if row_win:
                return True

        for col in range(len(self.rows[0])):
            col_win = True
            for row in self.rows:
                if not row[col].mark:
                    col_win = False
                    break
            if col_win:
                return True

        diag_win = True
        for i in range(len(self.rows[0])):
            if not self.rows[i][i].mark:
                diag_win = False
                break
        if diag_win:
            return True

        diag_win = True
        for i in range(len(self.rows[0])):
            if not self.rows[i][-(i + 1)].mark:
                diag_win = False
                break
        if diag_win:
            return True

        return False

    def partial_score(self):
        score = 0
        for row in self.rows:
            for sq in row:
                if not sq.mark:
                    score += sq.value
        return score


def main():

    with open("input.txt") as f:
        input_lines = [line.strip() for line in f.readlines()]

    callouts = [int(elem) for elem in input_lines[0].split(",")]

    boards: List[Board] = []
    rows: List[List[int]] = []
    for row in input_lines[2:]:
        if row == "":
            boards.append(Board(rows))
            rows = []
        else:
            rows.append([int(elem) for elem in row.replace("  ", " ").split(" ")])

    game_over = False
    for callout in callouts:
        if game_over:
            break

        square_record[callout].mark = True
        for b in boards:
            if b.check_win():
                print("Found Winning Board!")
                print(f"Score: {b.partial_score() * callout}")
                pyperclip.copy(b.partial_score() * callout)
                game_over = True
                break

    game_over = False
    boards_left = len(boards)
    board_wins = [False for i in range(len(boards))]
    for callout in callouts:
        if game_over:
            break

        square_record[callout].mark = True
        for i, b in enumerate(boards):
            if b.check_win():
                if not board_wins[i]:
                    board_wins[i] = True
                    boards_left += -1
                    if boards_left == 0:
                        print("Found Last Board!")
                        print(f"Score: {b.partial_score() * callout}")
                        pyperclip.copy(b.partial_score() * callout)
                        game_over = True
                        break


if __name__ == "__main__":
    main()
