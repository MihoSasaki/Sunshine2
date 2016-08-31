def answer1(input_file_name):  # , output_file_name):
    input_file = open(input_file_name, 'r')
    # output_file = open(output_file_name, 'w')
    T = int(input_file.readline())
    for case_number in range(1, T + 1):
        C = int(input_file.readline())
        I = int(input_file.readline())
        P = input_file.readline()
        P = P.split()
        # for i in range(len(P)):
        #    P[i] = int(P[i])
        # ans = solve(C, I, P)
        ans = solve2(C, P)
        print('Case #%s:%s' % (str(case_number), ans))
        # print('Case #' + str(case_number) + ':' + ans)
        #   output_file.write('Case #' + str(case_number) + ':' + ans)


def solve(C, I, P):
    for i in range(I - 1):
        for j in range(i + 1, I):
            if P[i] + P[j] == C:
                return str(i + 1) + '' + str(j + 1)


def solve2(C, P):
    for i, v in enumerate(P):
        for j, w in enumerate(P):
            if i == j:
                continue
            if (v + w) == C:
                return i + 1, j + 1
