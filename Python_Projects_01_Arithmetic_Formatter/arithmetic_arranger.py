def arithmetic_arranger(problems, solve=False):

    if len(problems) > 5:
        return "Error: Too many problems."

    top_line = ""
    bottom_line = ""
    dash_line = ""
    solution_line = ""

    for problem in problems:
       
        num1, operator, num2 = problem.split()

        if not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits."
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."
        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        max_length = max(len(num1), len(num2))

        top_line += num1.rjust(max_length + 2) + "    "

        bottom_line += operator + num2.rjust(max_length + 1) + "    "

        dash_line += "-" * (max_length + 2) + "    "

        if solve:
            if operator == "+":
                solution = int(num1) + int(num2)
            elif operator == '-':
                solution = int(num1) - int(num2)
            solution_line += str(solution).rjust(max_length + 2) + "    "

    output = top_line.rstrip() + "\n" + bottom_line.rstrip() + "\n" + dash_line.rstrip()
    if solve == True:
        output += "\n" + solution_line.rstrip()

    return output