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

    def __repr__(self) -> str:
        return str(self.value)+"e"+str(self.order_of_magnitude)
    
    def __str__(self) -> str:
        return str(self.value)+"e"+str(self.order_of_magnitude)