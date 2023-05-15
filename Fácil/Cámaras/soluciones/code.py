import math

while(True):
    try:
        arr = []
        T = list(map(int, input().strip().split(' ')))

        l = len(str(T[0]))
        center = len(str(T[0])) / 2

        c = (1 if (l % 2 == 0) else 0)
        # Start and end
        st = math.floor(center) - c
        en = math.ceil(center) + c

        num = list(map(int, [*str(T[0])[0:st]]))
        # Pivot number
        pivot = str(T[0])[st:en]

        pivot_num = len(str(pivot))

        num.append(int(pivot))

        # Reverse it to easy check
        num.reverse()

        # Original num
        original = [*num]

        # Adder
        adder = int('1' * pivot_num)

        while len(arr) != T[1]:
            for i in range(len(num)):

                # Before
                before = num[i]

                # Add
                adder_num = (adder if i == 0 else 1) * T[2]
                num[i] += adder_num

                if (len(str(abs(adder_num))) == len(('0' * len(str(abs(adder_num)))) if i == 0 and num[0] == 0 else str(num[i]))):
                    break
                
                num[i] = 0 if T[2] == 1 else int(('9' * len(str(abs(adder_num)))))


            pivot = ('0' * pivot_num) if num[0] == 0 else str(num[0])

            bigint = ''.join(map(str, num[1:]))


            f = bigint[::-1] + pivot + bigint

            if (len(str(int(f))) != l):
                num = [*original]
                T[2] *= -1
            else:
                arr.append(f)

        print(' '.join(arr))

    except EOFError:
        break

