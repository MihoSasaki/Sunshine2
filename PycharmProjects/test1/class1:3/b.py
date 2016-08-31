def answerb(input_file_name):
    input_file = open(input_file_name, 'r')
    T = int(input_file.readline())
    for case_number in range(1, T + 1):
        N = input_file.readline()
        N = N.split()
        for i in range(len(N)):
            N[i] = reverse(N[i])
            ans = join(N)
            print('Case #' + str(case_number) + ':' + ans)
            output_file.write('Case #' + str(case_number) + ':' + ans)


def solve(N):
    for i in range(I - 1):
        for j in range(i + 1, I):
            if P[i] + P[j] == C:
                return str(i + 1) + '' + str(j + 1)


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
    line.reverse
    return ' '.join(line)
