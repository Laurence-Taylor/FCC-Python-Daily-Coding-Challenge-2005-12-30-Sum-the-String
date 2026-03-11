def string_sum(s):
    # Declare set of numbers
    set_numbers = set('0123456789')
    # declare cheking_number variable to know the actual stage of number recognition 
    cheking_number = False
    # declare and init total variable
    total = 0
    # iterate over each character in s
    for i in range(len(s)):
        # if character is a number and not cheking the hole number
        if s[i] in set_numbers and not cheking_number:
            # activate cheking_number
            cheking_number = True
            # establish init position of the number
            init_pos = i
        # if character is not a number and still cheking if the end of the number is reached
        if not s[i] in set_numbers and cheking_number:
            # add to total the number found 
            total += int(s[init_pos:i])
            # The end of the present number is reached, so cheking number is false
            cheking_number = False
        # checking last character
        if i == len(s)-1:
            if s[i] in set_numbers and cheking_number:
                total += int(s[init_pos:i+1])

    return total

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