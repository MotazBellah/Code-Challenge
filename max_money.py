#!/usr/bin/env python3
def get_max_money(x, y=[]):
    """Take the informations about the restructuring and machine
    and return the max money could make during the restructuring
    inputs: x (list represent the info about the restructuring)
    y(list represent the info about machine related to restructuring)
    output: return an integer"""
    # Check if there are machines for sale
    if int(x[0]) and y:
        # Use generator for better performance and for more efficient memory storage and time
        # (x[-1]+1 - i[0]) * i[-1]) => subtract total restructuring days
        # from the day of the machine has been bought and multiply the value by the machine's profit rate
        # add the value to (x[1] - i[i]), subtract the total money from machine price
        # performe this math operations if machine price less than the total money
        machine_gen = max((((int(x[-1]) - int(i[0])) * int(i[-1])) + (int(x[1])- int(i[1])) + int(i[-2]) for i in y if int(x[1]) >= int(i[1])), default=int(x[1]))
        # machine_gen = max((((((int(x[-1]) - int(i[0])) * int(i[-1])) + int(x[1])- int(i[1])) + int(i[-2])) for i in y if int(x[1]) >= int(i[1])), default=int(x[1])))
        # ((((int(x[-1]) - int(i[0])) * int(i[-1])) + int(x[1])- int(i[1])) + int(i[-2]))
        # Check if the machine makes more money than the total money
        # i.e check if buying a machine is worth it
        if machine_gen > int(x[1]):
            return machine_gen
        else:
            # return total money
            return int(x[1])
    else:
        return int(x[1])
