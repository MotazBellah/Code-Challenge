def solution(phone_numbers, phone_owners, number):
    dictionary = dict(zip(phone_numbers, phone_owners))
    try:
        value = dictionary[number]
    except KeyError:
        return number
    return value
