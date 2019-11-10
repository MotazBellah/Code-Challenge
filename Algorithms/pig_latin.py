def pig_it(text):
    update_list = []

    for v in text.split():
        if v.isalpha():
            update_list.append((v[1:] + v[:1] + 'ay'))

        else:
             update_list.append(v)

    return " ".join(update_list)
