# Given a string, return the expansion of that string.
# Input will consist of only lowercase letters and numbers (1 to 9) in valid parenthesis.
# There will be no letters or numbers after the last closing parenthesis.

# solve("3(ab)") = "ababab"     -- because "ab" repeats 3 times
# solve("2(a3(b))") = "abbbabbb" -- because "a3(b)" == "abbb", which repeats twice.

def solve(str):
    new = str.replace('(', '').replace(')', '')
    d = [i for i in new if i in '123456789']
    if not len(d):
        return new

    s = ''
    l = list(new)
    for i in range(len(new)-1, -1, -1):
        if new[i] in '123456789':
            l.pop(i)
            l.insert(i, s[::-1] * int(new[i]))
            return solve(''.join(l))
        else:
            s += new[i]
            l.pop(i)

    return l


print(solve("2(a3(b))"))
print('#############')
print(solve("3(ab)"))
print('#############')
print(solve("2(a3(b))"))
print('#############')
print(solve("3(b(2(c)))"))
print('#############')
print(solve("k(a3(b(a2(c))))"))
# print(solve("2abbb"))
