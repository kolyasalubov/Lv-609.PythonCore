def enough(cap, on, wait):
    return (wait + on)-cap if cap - on <= wait else 0

    #     if cap - on <= wait:
#         print(f'I can take {cap - on} ')
#         return (wait+on)-cap
#     else:
#         return 0
