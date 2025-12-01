import re
def parse(s):
    match = re.match(r"([LR])(\d+)", s)
    if match:
        dir = match.group(1)
        dist = int(match.group(2))
        return (dir, dist)
    else:
        raise ValueError("Invalid input format.")
