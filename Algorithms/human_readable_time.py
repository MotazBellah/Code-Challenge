def make_readable(s):
    return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)
