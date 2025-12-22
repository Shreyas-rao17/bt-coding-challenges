class DecimalSplitter:
    """
    Method to get the whole number from a double
    """
    @staticmethod
    def get_whole(number):
        return int(number)

    """
    Method to get the fractional part of a double number
    """
    @staticmethod
    def get_fraction(number):
        whole = int(number)
        return round(number - whole, 6)

    """
    Method to check if a given number is odd or even
    """
    @staticmethod
    def is_odd(number):
        return int(number) % 2 != 0
