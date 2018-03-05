import main

def test_agent():
    '''
    Testing main class Agent.
    :return: None
    '''
    agent = main.Agent()
    agent.add_property()
    agent.display_properties()
    agent.assets()
    agent.taxes_percentage()
def test_house_rental():
    '''
    Testing House class, Property class and Rental class.
    :return: None
    '''
    init = main.HouseRental.prompt_init()
    house = main.HouseRental(**init)
    house.display()
def test_apartment_rental():
    '''
    Testing Apartment class, Property class  and Rental class.
    :return: None
    '''
    init = main.ApartmentRental.prompt_init()
    apartment = main.ApartmentRental(**init)
    apartment.display()
def test_apartment_purchase():
    '''
    Testinf Apartment class, Property class and Purchase class.
    :return: None
    '''
    init = main.ApartmentPurchase.prompt_init()
    apartment = main.ApartmentPurchase(**init)
    apartment.display()
def test_house_purchase():
    '''
    Testing House class, Property class and Purchase class.
    :return:
    '''
    init = main.HousePurchase.prompt_init()
    house = main.HousePurchase(**init)
    house.display()



if __name__=='__main__':
    test_agent()
    test_house_purchase()
    test_apartment_rental()
    test_house_rental()
    test_apartment_purchase()