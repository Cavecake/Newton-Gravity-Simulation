class Constants():
    value = None
    order_of_magnitude = None
    uncertainty = None # using same order of magnitude

    def __init__(self, mantissa, mantissa_uncertainty, exponent) -> None:
        """_summary_

        Args:
            mantissa (int): The mantissa of the constant (in nex it would be n)
            mantissa_uncertainty (int): The uncertainty, provided in the same order of magnitude as the mantissa
            exponent (int): The exponent, ten will be raised to (in nex if would be x)
        """
        self.set_value(mantissa,mantissa_uncertainty,exponent)

    def get_uncertainty_mantissa(self):
        return self.uncertainty
    
    def get_uncertainty_absolute_value(self):
        return self.uncertainty * (10**self.order_of_magnitude)
    
    def set_value(self, mantissa, mantissa_uncertainty, exponent):
        """_summary_

        Args:
            mantissa (int): The mantissa of the constant (in nex it would be n)
            mantissa_uncertainty (int): The uncertainty, provided in the same order of magnitude as the mantissa
            exponent (int): The exponent, ten will be raised to (in nex if would be x)
        """
        self.value = mantissa
        self.order_of_magnitude = exponent
        self.uncertainty = mantissa_uncertainty

    def get_value_seperated(self) -> tuple[int]:
        return self.value, self.order_of_magnitude
    
    def get_value(self) -> int:
        return self.value * (10**self.order_of_magnitude)

    # Output formatting
    def __repr__(self) -> str:
        return str(self.value)+"e"+str(self.order_of_magnitude)
    
    def __str__(self) -> str:
        return str(self.value)+"e"+str(self.order_of_magnitude)
    
    # Conversion to other types
    def __float__(self):
        return self.get_value()
    
    def __int__(self):
        return int(self.get_value())

    def __bool__(self):
        return (self.value != 0 or self.order_of_magnitude != 0)

    # Comparisions

    # special functions

    # arithmatic operations
    def __add__(self,other):
        number = self.get_value()
        return number + other
    def __radd__(self,other):
        number = self.get_value()
        return number + other

    def __sub__(self,other):
        number = self.get_value()
        return number - other
    def __rsub__(self,other):
        number = self.get_value()
        return number - other

    def __divmod__(self,other):
        number = self.get_value()
        return divmod(number, other)
    def __rdivmod__(self,other):
        number = self.get_value()
        return divmod(other, number)
    def __truediv__(self,other):
        number = self.get_value()
        return number / other
    def __rtruediv__(self,other):
        number = self.get_value()
        return other / number


    def __floordiv__(self,other):
        number = self.get_value()
        return number / other
    def __rfloordiv__(self,other):
        number = self.get_value()
        return other / number


    def __mul__(self,other):
        number = self.get_value()
        return number * other
    def __rmul__(self,other):
        number = self.get_value()
        return number * other