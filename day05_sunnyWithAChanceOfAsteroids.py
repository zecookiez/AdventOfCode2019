def solve(arr, input):
    p = 0
    sz = {1: 3, 2: 3, 3: 1, 4: 1, 5: 2, 6: 2, 7: 3, 8: 3, 99: 0}
    while arr[p] != 99:
        inst, op = divmod(arr[p], 100)
        p += 1
        val = []
        address = []
        for pos in xrange(sz[op]):
            param = inst // pow(10, pos) % 10
            val.append(arr[p] if param == 1 else arr[arr[p]])
            address.append(-1 if param == 1 else arr[p])
            p += 1
        if op == 1:
            arr[address[2]] = val[0] + val[1]
        elif op == 2:
            arr[address[2]] = val[0] * val[1]
        elif op == 3:
            arr[address[0]] = input
        elif op == 4:
            print "OUTPUT: %d" % val[0]
        elif op == 5:
            if val[0] != 0:
                p = val[1]
        elif op == 6:
            if val[0] == 0:
                p = val[1]
        elif op == 7:
            arr[address[2]] = [0, 1][val[0] < val[1]]
        elif op == 8:
            arr[address[2]] = [0, 1][val[0] == val[1]]
    return arr[0]
