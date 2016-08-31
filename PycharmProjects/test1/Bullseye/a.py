def answer(input_file_name, output_file_name):
    input_file = open(input_file_name, 'r')
    output_file = open(output_file_name, 'w')
    T = int(input_file.readline())
    for case_number in range(1, T + 1):
        linea = input_file.readline().split(" ")
        #linea = line.split(" ")
        r = int(linea[0])
        t = int(linea[1])
        # x = input_file.readline().split()
        # y = input_file.readline().split()
        # for i in range(len(x)):
        #    x[i] = int(x[i])
        #    y[i] = int(y[i])
        lo = 0
        hi = 10000000000
        while hi > lo + 1:
            mid = (lo + hi) / 2
            if 2 * r * mid + (2 * mid - 1) * mid <= t:
                lo = mid
            else:
                hi = mid
        #output_file.write('Case #' + str(case_number) + ':' + ans + '\n')
        output_file.write('Case #%d: %d' % (case_number, lo) + '\n')
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


def solve(r, t):
    lo = 0
    hi = 10000000000
    while hi > lo + 1:
        mid = (lo + hi) / 2
        if 2 * r * mid + (2 * mid - 1) * mid <= t:
            lo = mid
        else:
            hi = mid
