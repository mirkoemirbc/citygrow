import random


# Generic Functions
def percent(num1, num2):
    """ Return the percent """
    return round(num1 / num2 * 100, 2)


def containedin(originallist, lencount):
    """
    Return a list of N random elements selected from originallist
    """
    list_temp = []
    for counter in range(len(originallist)):
        item = random.choice(originallist)
        if item not in list_temp:
            list_temp.append(item)
        if len(list_temp) == lencount:
            break

    return list_temp
