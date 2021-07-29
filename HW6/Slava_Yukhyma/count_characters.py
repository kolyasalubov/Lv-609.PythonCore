# function for letters only

def count_letters(user_string, result_counted_letters={}):
    ''' Function takes a string and counts 
        amount of each letter, ignoring other characters.
        Returns dictionary where letter is a key, amount is a value.
        Dictionary to return is announced in parameters(default) 
    '''
    for letter in user_string:
        if letter.isalpha():
            if letter in result_counted_letters:
                result_counted_letters[letter] += 1
            else:
                result_counted_letters[letter] = 1

    print(result_counted_letters)

    return result_counted_letters


count_letters('aa dd,ff, gg,hhhh , gg')


# the same one


def count_letters_in_str(user_str):
    ''' Function takes a string and counts
        amount of each letter, ignoring other characters.
        returns dictionary where letter is a key, amount is a value
    '''
    return{a: user_str.count(a) for a in user_str if a.isalpha()} if type(user_str) == str else print('Enter string again, please')


print(count_letters_in_str('aa  sss ff jjj, kk'))


def count_characters(user_string):
    '''
    Function takes a string and return dictionary with counted appereance 
    of each character.

    '''

    return {character: user_string.count(character) for character in user_string} if isinstance(user_string, str) else print('You entered not a string!')


print(count_characters('aa, ddd. fff kkk '))
