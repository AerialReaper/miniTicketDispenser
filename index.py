import my_decorators

class Comerce:
    def __init__(self, name, key, number = 0):
        self.name = name
        self.key = key
        self.number = number

    @my_decorators.greet_the_client
    def expend_tiket(self):
        resp = f'{self.key}-{str(self.number).zfill(2)}'
        self.number += 1
        print(resp)

    def show_last_tikeck(self):
        print(f'{self.name} => {self.key}-{str(self.number).zfill(2)}')

def init():
    pharmacy = Comerce('Pharmacy', 'F')
    cosmetics = Comerce('Cosmetics','C')
    perfumery = Comerce('Perfumery','P')

    comerces = [pharmacy, cosmetics, perfumery]

    menu_option = 0

    while menu_option != 'E':
        print('Take a ticket for: Pharmacy(F), Cosmetics(C), Perfumery(P), show queue(Q) or Exit(E)')
        menu_option = input('Select an option please: ')

        if menu_option == 'F':
            pharmacy.expend_tiket()
        elif menu_option == 'C':
            cosmetics.expend_tiket()
        elif menu_option == 'P':
            perfumery.expend_tiket()
        elif menu_option == 'Q':
            print('The queue is:')
            for comerce in comerces:
                comerce.show_last_tikeck()
            print('Take a ticket and wait to be served. Thanks!')

    print("Thanks for operating whith us!")

init()