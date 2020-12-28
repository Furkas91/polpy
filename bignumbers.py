import numpy as np

class BigNumbers:
    
    def __init__(self, value):
        #sign of count: 0 - positive, 1 - negative
        self.sign = 0

        self.number = np.array(0)
        if isinstance(value, str):
            if value[0] != '-':
                self.number = np.array(len(value))
                for i in range(len(value)):
                    self.number[i] = int(value[i])
            else:
                self.sign = 1
                self.number = np.array(len(value) - 1)
                for i in range(1, len(value)):
                    self.number[i - 1] = int(value[i])
        elif isinstance(value, int):
            if value >= 0:
                self.sign = 0
            else:
                self.sign = 1
            number_str = str(value).split('')
            self.number = np.array(len(number_str))
            for i, n in enumerate(number_str):
                self.number[i] = int(n)
        else:
            self.number = value.copy()

    def __str__(self):
        if self.sign == 0:
            return str(self.number)
        else:
            return "-" + str(self.number)

    def __lt__(self, other):
        #If self is negative and other is positive
        if self.sign > other.sign:
            return True
        #If self is positive and other is negative
        elif self.sign < other.sign:
            return False
        #If they have one positive sign
        elif self.sign == 0:
            #If self has more characters
            if len(self.number) > len(other.number):
                return False
            #If self has fewer characters
            elif len(self.number) < len(other.numer):
                return True
            #If they have same number of characters
            else:
                for i in range(len(self.number)):
                    if self.number[i] > other.number[i]:
                        return False
                    elif self.number[i] < other.number[i]:
                        return True
                    else:
                        continue
                # If they are equal
                return False
        else:
            # If self has more characters
            if len(self.number) > len(other.number):
                return True
            # If self has fewer characters
            elif len(self.number) < len(other.numer):
                return False
            # If they have same number of characters
            else:
                for i in range(len(self.number)):
                    if self.number[i] > other.number[i]:
                        return True
                    elif self.number[i] < other.number[i]:
                        return False
                    else:
                        continue
                #If they are equal
                return False

    def __eq__(self, other):
        if self.sign == other.sign and np.equal(self.number, other.number):
            return True
        else:
            return False

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return not (self <= other)

    def __ge__(self, other):
        return self > other or self == other

    def __ne__(self, other):
        return not self == other

    def __add__(self, other):
        if isinstance(other, BigNumbers):
            # len_self = len(self.number)
            # len_other = len(other.number)
            # len_max = max(len_self, len_other)
            # len_min = min(len_self, len_other)
            # result =
            # if self.sign + other.sign == 1:
            #     for i in range(len_min):
            #         result[i] =