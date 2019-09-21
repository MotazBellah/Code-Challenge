def AMC(x, y):
    total = x[1]
    # check if there machines for sale
    if not x[0]:
        # return the total dollar
        return x[1]
    else:
        print('a')
        # sort the machines with the bought price
        # to find the cheapest machine faster
        machine = sorted(y, key=lambda z: z[1])
        cheapest_machine = machine[0]
        # check if the bought price is greater than the total money
        # OR if the bought process is worth it
        if (cheapest_machine[1] > total or
            (x[-1] - cheapest_machine[0]) * cheapest_machine[-1] <= total):
            print('b')
            return total
        # elif (x[-1] - cheapest_machine[0]) * cheapest_machine[-1] <= total:
        #     print('c')
        #     return total

        # check if there two machine with same price
        # take the one with higher profit rate
        # if profit the same take the one with high resold price
        # if the resold price the same, take any one
        elif cheapest_machine[1] == machine[1][1]:
            print('d')
            if cheapest_machine[-1] > cheapst_machine[1][-1]:
                total -= cheapest_machine[1]
                reset = x[2]+1 - cheapest_machine[0]
                profit = reset * cheapest_machine[-1]
                total += profit

            elif cheapest_machine[-1] < machine[1][-1]:
                total -= machine[1][1]
                reset = x[2]+1 - machine[1][0]
                profit = reset * machine[1][-1]
                total += profit

            elif cheapest_machine[-2] > machine[1][-2]:
                total -= cheapest_machine[1]
                reset = x[2]+1 - cheapest_machine[0]
                profit = reset * cheapest_machine[-1]
                total += profit

            elif cheapest_machine[-2] < machine[1][-2]:
                total -= machine[1][1]
                reset = x[2]+1 - machine[1][0]
                profit = reset * machine[1][-1]
                total += profit

            else:
                total -= cheapest_machine[1]
                reset = x[2]+1 - cheapest_machine[0]
                profit = reset * cheapest_machine[-1]
                total += profit
        else:
            print('e')
            total -= cheapest_machine[1]
            reset = x[2]+1 - cheapest_machine[0]
            profit = reset * cheapest_machine[-1]
            total += profit

        return total



def AMC(x, y):
    total = x[1]

    if not x[0]:
        return x[1]
    else:
        print('a')
        cheapst_machine = sorted(y, key=lambda z: z[1])
        if cheapst_machine[0][1] > total:
            print('b')
            return total
        elif (x[-1] - cheapst_machine[0][0]) * cheapst_machine[0][-1] <= total:
            print('c')
            return total
        elif cheapst_machine[0][1] == cheapst_machine[1][1]:
            print('d')
            if cheapst_machine[0][-1] > cheapst_machine[1][-1]:
                total -= cheapst_machine[0][1]
                reset = x[2]+1 - cheapst_machine[0][0]
                profit = reset * cheapst_machine[0][-1]
                total += profit

            elif cheapst_machine[0][-1] < cheapst_machine[1][-1]:
                total -= cheapst_machine[1][1]
                reset = x[2]+1 - cheapst_machine[1][0]
                profit = reset * cheapst_machine[1][-1]
                total += profit

            elif cheapst_machine[0][-2] > cheapst_machine[1][-2]:
                total -= cheapst_machine[0][1]
                reset = x[2]+1 - cheapst_machine[0][0]
                profit = reset * cheapst_machine[0][-1]
                total += profit

            elif cheapst_machine[0][-2] < cheapst_machine[1][-2]:
                total -= cheapst_machine[1][1]
                reset = x[2]+1 - cheapst_machine[1][0]
                profit = reset * cheapst_machine[1][-1]
                total += profit

            else:
                total -= cheapst_machine[0][1]
                reset = x[2]+1 - cheapst_machine[0][0]
                profit = reset * cheapst_machine[0][-1]
                total += profit
        else:
            print('e')
            total -= cheapst_machine[0][1]
            reset = x[2]+1 - cheapst_machine[0][0]
            profit = reset * cheapst_machine[0][-1]
            total += profit

        return total

# def AMC2(x, y):
#     if not x[0]:
#         return x[1]
#     day = sorted(y, key=lambda z: z[0])
#     cheapst = sorted(y, key=lambda z: z[1])
#     if day[-1][0] == y[-1]:
#         g = x[1] + day[-1][2]
#     a = cheapst[0]
#     print(a)
#     total = x[1] - a[1]
#     print(total)
#     rest = (x[2]+1) - a[0]
#     print(rest)
#     profit = rest * a[-1]
#     print(profit)
#     return total + profit
