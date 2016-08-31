
def answer(input_file_name, output_file_name):
    input_file = open(input_file_name, 'r')
    output_file = open(output_file_name, 'w')
    T = int(input_file.readline())
    for case_number in range(1, T + 1):
        n = input_file.readline()
        x = input_file.readline().split()
        y = input_file.readline().split()
        for i in range(len(x)):
            x[i] = int(x[i])
            y[i] = int(y[i])
        ans = solve(n, x, y)
        output_file.write('Case #' + str(case_number) + ':' + ans + '\n')
    input_file.close()
    output_file.close()


def solve(n, x, y):
    x.sort()
    y.sort()
    y.reverse()
    ans = 0
    for i in range(n):
        ans += x[i] * y[i]
    return ans

