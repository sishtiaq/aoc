# Day 5, Part 1
from enum import Enum

class input_type(Enum):
    fresh_range = 1
    available_ingredients = 2

def main():
    fresh_ranges = set()
    fresh_available = 0
    input_mode = input_type.fresh_range

    while True:
        try:
            line = input()
            if line == "":
                input_mode = input_type.available_ingredients
                continue
            if input_mode == input_type.fresh_range:
                # process fresh range input
                (lo,hi) = line.split("-")
                # print(f"Processing fresh range: {lo}-{hi}")
                fresh_ranges.add((lo,hi))
            else: #if input_mode == input_type.available_ingredients:
                ingredient = int(line)
                not_found = True
                for (lo,hi) in fresh_ranges:
                    if int(lo) <= ingredient <= int(hi) and not_found:
                        # print(f"Ingredient {ingredient} is available in fresh range {lo}-{hi}")
                        not_found = False
                        fresh_available += 1
        except EOFError:
            break

    print(f"Fresh available ingredients: {fresh_available}")

if __name__ == "__main__":
    main()