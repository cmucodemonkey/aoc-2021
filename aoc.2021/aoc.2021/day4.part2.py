MARKED_VALUE = "X"

def is_bingo(card):
    for row in card:
        if row.count(MARKED_VALUE) == 5:
            return True

    for column_id in range(5):
        temp = []

        for row_id in range(5):
            row = card[row_id]
            temp.append(row[column_id])

        if temp.count(MARKED_VALUE) == 5:
            return True

    return False

def calculate_card_score(card):
    total = 0
    
    for row in card:
        for column in row:
            if column.isnumeric():
                total += int(column)

    return total

def main():
    input_list = open("Input\day4.txt", "r").read().split("\n")
    card = []
    winning_card = []
    numbers_drawn_before_bingo = 0
    last_drawn_number = -1

    drawn_numbers = input_list[0].split(",")

    for line_id in range(2, len(input_list)):
        if len(input_list[line_id]) > 0:
            temp = input_list[line_id].replace("  ", " ").lstrip().split(" ");
            card.append(temp)
        else:
            count = 0

            for number in drawn_numbers:
                count += 1

                for row_id in range(5):
                    row = card[row_id]

                    for column_id in range(5):
                        if row[column_id] == number:
                            row[column_id] = MARKED_VALUE

                if count >= 5 and is_bingo(card):
                    if len(winning_card) == 0 or count > numbers_drawn_before_bingo:
                        winning_card = card
                        numbers_drawn_before_bingo = count
                        last_drawn_number = number

                    card = []
                    break
    
    print(calculate_card_score(winning_card) * int(last_drawn_number))

main()
