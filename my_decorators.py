def greet_the_client(func):
    def say_hi(code):
        print('Your turn is:')
        func(code)
        print('Wait to be served. Thanks!')
    return say_hi

# def show_queue(func):
#     def show(code):
#         print('The queue is:')
#         func(code)
#         print('Take a ticket and wait to be served. Thanks!')
#     return show