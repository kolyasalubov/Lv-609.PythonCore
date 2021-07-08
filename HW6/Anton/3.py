def count_of_characters(string):
    return f'count of characters: {len(string)}' if type(string) == str else f'it "{string}" must be string'

# SECOND VARIANT 

# def count_of_characters(string):
#     count = 0
#     if type(string) == str:
#         for i in string:
#             count += 1
#         return f'count of characters: {count}'
#     else:
#         return f'it "{string}" must be string'
    