def string_sum(s):
    set_numbers = set('0123456789')
    next_number = False
    total = 0
    init_pos = 0
    for i in range(len(s)):
        if s[i] in set_numbers:
            total += int(s[i])
    print(total)
    return s

if __name__ == '__main__':
    print(string_sum("3apples2bananas"))
    print('-----')
    print(string_sum("10cats5dogs2birds"))
    print('-----')
    print(string_sum("125344"))
    print('-----')
    print(string_sum("a1b20c300"))
    print('-----')
    print(string_sum("a12b34c56d78e90f123g456h789i0j1k2l3m4n5"))