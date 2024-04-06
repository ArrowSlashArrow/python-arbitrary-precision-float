def bf(val):
    return BigFloat(val)

class BigFloat:
    def __init__(self, value):
        # safe type conversion to string
        str_value = str(value)

        # if value is a decimal:
        if "." in str_value:
            # set integer and decimal (float) values
            self.int = int(str_value.split(".")[0])
            self.float = str_value.split(".")[1]
        else:
            # set integer value and decimal (float) value to 0
            self.int = int(str_value)
            self.float = "0"

        if self.int != abs(self.int):
            self.neg = True
        else:
            self.neg = False

    def __str__(self):
        # string representation of BigFloat
        return str(self.int) + "." + str(self.float)

    def __add__(self, other):
        # remove trailing zeros of decimal components
        self.float.strip("0")
        other.float.strip("0")

        # add integer components
        int_sum = self.int + other.int

        # get precision difference
        prec_diff = abs(len(self.float) - len(other.float))

        # get less precise number
        less_prec = "self" if min(len(self.float), len(other.float)) == len(self.float) else "other"
        # add extra leading zeros to match precision of less precise number to more precise number
        if less_prec == "self":
            self.float = self.float + "0" * prec_diff
        else:
            other.float = other.float + "0" * prec_diff

        # in the event that the precision of the two numbers is equal, 0 extra zeros will be added,
        # so the end result will not be affected

        # add decimal components
        if (self.neg or other.neg) and not (self.neg and other.neg):
            # negative number
            float_sum = str(int(other.float) - int(self.float))
            # account for overflow of decimal value addition
            if int(float_sum) != abs(int(float_sum)):
                int_sum -= 1
                float_sum = int("1" + (len(self.float)) * "0") + int(float_sum)
        else:
            # positive sum
            float_sum = str(int(self.float) + int(other.float))
            # account for overflow of decimal value addition
            if len(float_sum) > len(other.float) or len(float_sum) > len(self.float):
                int_sum += 1
                float_sum = float_sum[1:]

        # return final result
        return BigFloat(str(int_sum) + "." + str(float_sum))

    def __sub__(self, other):
        # remove trailing zeros of decimal components
        self.float.strip("0")
        other.float.strip("0")

        # add integer components
        int_sum = self.int - other.int

        # get precision difference
        prec_diff = abs(len(self.float) - len(other.float))

        # get less precise number
        less_prec = "self" if min(len(self.float), len(other.float)) == len(self.float) else "other"
        # add extra leading zeros to match precision of less precise number to more precise number
        if less_prec == "self":
            self.float = self.float + "0" * prec_diff
        else:
            other.float = other.float + "0" * prec_diff

        # in the event that the precision of the two numbers is equal, 0 extra zeros will be added,
        # so the end result will not be affected

        # add decimal components

        if (self.neg or other.neg) and not (self.neg and other.neg):
            # positive sum
            float_sum = str(int(self.float) + int(other.float))
            # account for overflow of decimal value addition
            if len(float_sum) > len(other.float) or len(float_sum) > len(self.float):
                int_sum += 1
                float_sum = float_sum[1:]
        else:
            # negative number
            float_sum = str(int(other.float) - int(self.float))
            # account for overflow of decimal value addition
            if int(float_sum) != abs(int(float_sum)):
                int_sum -= 1
                float_sum = int("1" + (len(self.float)) * "0") + int(float_sum)

        # return final result
        return BigFloat(str(int_sum) + "." + str(float_sum))


test_float_1 = bf(-1.2390478209482304)
test_float_2 = bf(1.7298237059745738912567234965790234675892346)

print(test_float_1 - test_float_2)

