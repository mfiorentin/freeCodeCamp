#  link to replit code: https://replit.com/@MauricioFiorent/boilerplate-arithmetic-formatter#arithmetic_arranger.py

def arithmetic_arranger(problems, print_results=False):

    if len(problems) > 5:
        too_many_error = "Error: Too many problems."
        return too_many_error

    eq_parts = problems[0].split()
    term_1 = eq_parts[0]
    opt = eq_parts[1]
    term_2 = eq_parts[2]
    max_length = max(len(term_1), len(term_2))

    if len(term_1) > 4 or len(term_2) > 4:
        length_error = "Error: Numbers cannot be more than four digits."
        return length_error

    if not term_1.isdigit():
        digit_error = "Error: Numbers must only contain digits."
        return digit_error

    if not term_2.isdigit():
        digit_error = "Error: Numbers must only contain digits."
        return digit_error

    if opt not in "+-":
        operator_error = "Error: Operator must be '+' or '-'."
        return operator_error

    first_line = ((max_length+2)-len(term_1)) * " " + term_1
    second_line = opt + ((max_length+1)-len(term_2)) * " " + term_2
    third_line = "-" * (max_length+2)

    if opt in "+":
        result = int(term_1) + int(term_2)
    else:
        result = int(term_1) - int(term_2)

    result = str(result)

    result_line = ((max_length+2)-len(result)) * " " + result

    problems = problems[1:]

    #first

    for problem in problems:
        eq_parts = problem.split()
        term_1 = eq_parts[0]
        opt = eq_parts[1]
        term_2 = eq_parts[2]

        if len(term_1) > 4 or len(term_2) > 4:
            length_error = "Error: Numbers cannot be more than four digits."
            return length_error

        if not term_1.isdigit():
            digit_error = "Error: Numbers must only contain digits."
            return digit_error

        if not term_2.isdigit():
            digit_error = "Error: Numbers must only contain digits."
            return digit_error

        if opt not in "+-":
            operator_error = "Error: Operator must be '+' or '-'."
            return operator_error

        if opt in "+":
            result = int(term_1) + int(term_2)
        else:
            result = int(term_1) - int(term_2)

        max_length = max(len(term_1), len(term_2))

        first_line += "    " + str(term_1).rjust(max_length+2)
        second_line += "    " + opt + " " + str(term_2).rjust(max_length)
        third_line += "    " + (max_length+2) * "-"
        result_line += "    " + str(result).rjust(max_length+2)

        if print_results==True:
            final_solution = first_line + "\n" + second_line + "\n" + third_line + "\n" + result_line
        else:
            final_solution = first_line + "\n" + second_line + "\n" + third_line

    return final_solution
