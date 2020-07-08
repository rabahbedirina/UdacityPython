class Pants:
    """ The Pants class represents an article of clothing sold in a store """

    def __init__(self, pants_color, pants_waist_size, pants_lenght, pants_price):
        """ Method for initializing a Pants object

        Args:
            color (str)
            waist_size (int)
            length (int)
            price (float)

        Attributes:
            color (str): color of a pants object
            waist_size (str): waist size of a pants object
            length (str): length of a pants object
            price (float): price of a pants object """
        self.color = pants_color
        self.waist_size = pants_waist_size
        self.length = pants_lenght
        self.price = pants_price

    def change_price(self, new_price):
        """The change_price method changes the price attribute of a pants object

        Args:
            new_price (float): the new price of the pants object

        Returns: None

        """

        self.price = new_price

    def discount(self, discount):
        """The discount method outputs a discounted price of a pants object

        Args:
            percentage (float): a decimal representing the amount to discount

        Returns:
            float: the discounted price
        """
        return self.price*(1-discount)
