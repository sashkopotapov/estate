

def get_valid_input(input_string, valid_options):
    '''
    Checks input for requierence.
    :param input_string: string to ckeck
    :param valid_options: possible variants
    :return: bool
    '''
    input_string +=  ' ({}) '.format(', '.join(valid_options))
    response = input(input_string)
    while response.lower() not in valid_options:
        response = input(input_string)
    return response

class Property:
    '''
    Property class that characterizes basic property.
    '''
    def __init__(self, square_feet='', beds='',baths='', **kwargs):
        '''
        Initializes Property class with a few attributes.
        :param square_feet: str
        :param beds: str
        :param baths: str
        :param kwargs: dict
        '''
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.beds = beds
        self.baths = baths
    def display(self):
        '''
        Displays Property class object attributes.
        :return: None
        '''
        print('PROPERTY DETAILS')
        print('+++++++++++++++')
        print('square footage: {}'.format(self.square_feet))
        print('bedrooms: {}'.format(self.beds))
        print('bathrooms: {}'.format(self.baths))
        print()
    @staticmethod
    def prompt_init():
        '''
        Allows to give an object attributes by inputing them in console.
        :return: dict
        '''
        return dict(square_feet=input('Enter the square feet: '),
                    beds=input('Enter number of bedrooms: '),
                    baths=input('Enter number of baths: '))

class Apartment(Property):
    '''
     Property is a parent class. Apartment class characterizes apartment property.
    '''
    valid_laundries = ('coin', 'ensuite', 'none')
    valid_balconies = ('yes', 'no', 'solarium')

    def __init__(self, balcony='', laundry='', **kwargs):
        '''
        Initializes Property class with a few attributes. Inheirits Property class attributes.
        :param balcony: str
        :param laundry: str
        :param kwargs: dict
        '''
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        '''
        Displays Apartment class object attributes.
        :return: None

        '''
        super().display()
        print('APARTMENT DETAILS')
        print('laundry: %s' % self.laundry)
        print('has balcony: $s' % self.balcony)

    @staticmethod
    def prompt_init():
        '''
        Allows to give an object attributes by inputing them in console.
        :return: dict
        '''
        parent_init = Property.prompt_init()
        laundry= get_valid_input('What laundry facilities does '
                            'the property have?',
                        Apartment.valid_laundries)
        balcony = get_valid_input('Does the property have a balcony?',
                        Apartment.valid_balconies)
        parent_init.update({'laundry': laundry,
                            'balcony': balcony})
        return parent_init

class House(Property):
    '''
    Property is a parent class. House class characterizes house property.
    '''
    valid_garage = ('attached', 'detached', 'none')
    valid_fenced = ('yes', 'no')

    def __init__(self, num_stories='', garage='', fenced='', **kwargs):
        '''
        Initializes House class with a few attributes.
        :param num_stories: str
        :param garage: str
        :param fenced: str
        :param kwargs: dict
        '''
        super().__init__(**kwargs)
        self.garage = garage
        self.fenced = fenced
        self.num_stories = num_stories

    def display(self):
        '''
        Displays House class object attributes.
        :return: None
        '''
        super().display()
        print('HOUSE DETAILS')
        print('# of stories: {}'.format(self.num_stories))
        print('garage: {}'.format(self.garage))
        print('fenced yard: {}'.format(self.fenced))

    @staticmethod
    def prompt_init():
        '''
        Allows to give an object attributes by inputing them in console.
        :return: dict
        '''
        parent_init = Property.prompt_init()
        fenced= get_valid_input('Is the yard fenced? ',
                        House.valid_fenced)
        garage = get_valid_input('Is there a garage? ',
                        House.valid_garage)
        num_stories = input('How many stories? ')
        parent_init.update({'fenced': fenced,
                            'garage': garage,
                            'num_stories': num_stories})
        return parent_init

class Purchase:
    '''
    Allows to extend some object with purchase attributes.
    '''
    def __init__(self, price='', taxes='', **kwargs):
        '''
        Initializes Purchase class with a few attributes.
        :param price: str
        :param taxes: str
        :param kwargs: dict
        '''
        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes

    def display(self):
        '''
        Displays Purchase class object attributes.
        :return: None
        '''
        super().display()
        print('PURCHASE DETAILS')
        print('selling price: {}'.format(self.price))
        print('estimated taxes: {}'.format(self.taxes))
    @staticmethod
    def prompt_init():
        '''
        Allows to give an object attributes by inputing them in console.
        :return: dict
        '''
        return dict(
            price=input('What is the selling price? '),
            taxes=input('What are estimated taxes? '))

class Rental:
    '''
    Allows to extend some object with rental attributes.
    '''
    def __init__(self, furnished='', utilities='',
                 rent='', **kwargs):
        '''
        Initializes Purchase class with a few attributes.
        :param furnished: str
        :param utilities: str
        :param rent: str
        :param kwargs: dict
        '''
        super().__init__(**kwargs)
        self.furnished = furnished
        self.rent = rent
        self.utilities = utilities

    def display(self):
        '''
        Displays Purchase class object attributes.
        :return: None
        '''
        super().display()
        print('RENTAL DETAILS')
        print('rent: {}'.format(self.rent))
        print('estimated utilities: {}'.format(self.utilities))
        print('furnished: {}'.format(self.furnished))

    @staticmethod
    def prompt_init():
        '''
        Allows to give an object attributes by inputing them in console.
        :return: dict
        '''
        return dict(rent=input('What is monthly rent? '),
                    utilities = input('What are the estimated '
                    'utilities? '), furnished=
                    get_valid_input('Is the property furnihed? ',
                    ('yes', 'no')))

class HouseRental(Rental, House):
    '''
    This class allows to connect House class and Rental class.
    '''
    @staticmethod
    def prompt_init():
        '''
        Connects two classes to one dictionary.
        :return: dict
        '''
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init

class ApartmentRental(Rental, Apartment):
    '''
    This class allows to connect Apartment class and Rental class.
    '''
    @staticmethod
    def prompt_init():
        '''
        Connects two classes to one dictionary.
        :return: dict
        '''
        init = Apartment.prompt_init ()
        init.update (Rental.prompt_init ())
        return init

class ApartmentPurchase(Purchase, Apartment):
    '''
    This class allows to connect Apartment class and Purchase class.
    '''
    @staticmethod
    def prompt_init():
        '''
        Connects two classes to one dictionary.
        :return: dict
        '''
        init = Apartment.prompt_init()
        init.update (Purchase.prompt_init())
        return init

class HousePurchase(Purchase, House):
    '''
    This class allows to connect House class and Purchase class.
    '''
    @staticmethod
    def prompt_init():
        '''
        Connects two classes to one dictionary.
        :return: dict
        '''
        init = House.prompt_init ()
        init.update (Purchase.prompt_init ())
        return init

class Agent:
    '''
    This class connects all classes above and allows to work with them.
    '''
    def __init__(self):
        '''
        Inialize a list o property objects.
        '''
        self.property_list = []

    def display_properties(self):
        '''
        Display all available property
        :return: None
        '''
        for property in self.property_list:
            property.display()
    type_map = {
        ('house', 'rental'): HouseRental,
        ('house', 'purchase'): HousePurchase,
        ('apartment', 'rental'): ApartmentRental,
        ('apartment', 'purchase'): ApartmentPurchase
    }

    def add_property(self):
        '''
        Add property object to a list with all properties.
        :return:
        '''
        property_type = get_valid_input('What type of property? ',
                                        ('house', 'apartment')).lower()
        payment_type = get_valid_input('WHat payment type? ',
                                       ('purchase', 'rental')).lower()
        PropertyClass = self.type_map[(property_type, payment_type)]
        init_args = PropertyClass.prompt_init()
        self.property_list.append(PropertyClass(**init_args))

    def assets(self):
        '''
        Returns total assets controlled by agent in US Dollars.
        :return: str
        '''
        purchase = []
        rental = []
        for i in self.property_list:
            if isinstance(i, HousePurchase) or isinstance(i, ApartmentPurchase):
                purchase.append(int(i.price))
            elif isinstance(i, HouseRental) or isinstance(i, ApartmentRental):
                rental.append(int(i.rent))
        print('Total purchase price is {}.\n' \
               ' Total rental price for month is {}.\n ' \
               'Total assets for year are {}(purchase + rental x 12)'\
            .format(
            sum(purchase), sum(rental), sum(purchase) + sum(rental)*12))

    def taxes_percentage(self):
        '''
        Shows taxes part in property price in percents.
        :return: str
        '''
        taxes = []
        for i in self.property_list:
            if isinstance (i, HousePurchase):
                taxes.append('{}% of price to pay for {} square feet house'.
                             format(int(i.taxes)/int(i.price)*100, i.square_feet))
            elif isinstance(i, ApartmentPurchase):
                taxes.append('{}% of price to pay for {} square feet apartment'.
                             format((int(i.taxes)/int(i.price))*100, i.square_feet))
        for i in taxes: print(i)

