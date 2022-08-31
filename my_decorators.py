def greet_the_client(func):
    def say_hi(code):
        print('*' * 26)
        print('Your turn is:')
        func(code)
        print('Wait to be served. Thanks!')
        print('*' * 26)
    return say_hi

# def show_queue(func):
#     def show(code):
#         print('The queue is:')
#         func(code)
#         print('Take a ticket and wait to be served. Thanks!')
#     return show