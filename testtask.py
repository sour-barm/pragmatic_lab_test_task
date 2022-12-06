from sys import argv


def ternary(num):
    base = 3
    res = ""
    while num > 0:
        res = str(num % base) + res
        num //= base
    return res


def math_expression(ter: dict):
    ter_list = list(ter)
    mark = [""] * 9
    for i in range(1, 10):
        t = i - 1
        i *= -1
        if t < len(ter_list):
            element = int(ter_list[i])
            if element == 0:
                mark[i] = ""
            elif element == 1:
                mark[i] = "+"
            elif element == 2:
                mark[i] = "-"
        else:
            mark[i] = ""
    math_expression = ""
    for i in range(9):
        math_expression += f"{9-i}{mark[i]}"
    math_expression += "0"
    return math_expression


def solution() -> dict:
    ret = {}
    quantity = 3**9
    for i in range(quantity):
        expression = math_expression(ternary(i))
        result = eval(expression)
        if result in ret:
            ret[result].append(expression)
        else:
            ret[result] = [expression]
    return ret


def main() -> None:
    expected = 200
    if len(argv) != 1:
        expected = int(argv[1])
    data = solution()
    if expected in data:
        print(data[expected])
    else:
        print("Not found for " + expected)


if __name__ == "__main__":
    main()
