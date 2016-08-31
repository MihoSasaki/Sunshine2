def answer(input_file_name, output_file_name):
    input_file = open(input_file_name, 'r')
    output_file = open(output_file_name, 'w')
    T = int(input_file.readline())
    for case_number in range(1, T + 1):
        line = input_file.readline()
        line.rstrip()
        line = line.split()
        ans = solve(line)
        output_file.write('Case #' + str(case_number) + ':' + ans + '\n')
    input_file.close()
    output_file.close()


def solve(line):
    trans = {
       'a' = ?,
       'b' = ?,
    }
    eng = ''
    for g in line
        eng += translation[line]


def make_translation
