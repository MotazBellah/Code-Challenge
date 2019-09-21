def opn():
    

def test(x, y=[]):
    if x[0] and y:
        machine_gen = (((x[-1]+1 - i[0]) * i[-1]) + (x[1]- i[1]) for i in y if x[1] >= i[1])
        return max(machine_gen)
    else:
        return x[1]
def AMC3(x, y):
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

     
        
def AMC2(x, y):
    if not x[0]:
        return x[1]
    day = sorted(y, key=lambda z: z[0])
    cheapst = sorted(y, key=lambda z: z[1])
    if day[-1][0] == y[-1]:
        g = x[1] + day[-1][2]
    a = cheapst[0]
    print(a)
    total = x[1] - a[1]
    print(total)
    rest = (x[2]+1) - a[0]
    print(rest)
    profit = rest * a[-1]
    print(profit)
    return total + profit
    
