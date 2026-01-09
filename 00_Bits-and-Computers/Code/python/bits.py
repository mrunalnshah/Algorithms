class Bit:
    @staticmethod
    def _and(x: bool, y: bool) -> bool:
        """
        Perform a bitwise AND operation on two boolean values.
        
        :param x: First boolean operand
        :type x: bool
        :param y: Second boolean operand
        :type y: bool
        :return: True if both x and y are True, otherwise False.
        :rtype: bool
        """
        result = x & y

        return result
    
    @staticmethod
    def _or(x: bool, y: bool) -> bool:
        """
        Perform a bitwise OR operation on two boolean values.
        
        :param x: First boolean operand
        :type x: bool
        :param y: Second boolean operand
        :type y: bool
        :return: True if either x or y is True, otherwise False.
        :rtype: bool
        """
        result = x | y

        return result
    
    @staticmethod
    def _xor(x:bool, y: bool) -> bool:
        """
        Perform a bitwise XOR (exclusive OR) operation on two boolean values.
        
        :param x: First boolean operand
        :type x: bool
        :param y: Second boolean operand
        :type y: bool
        :return: True if exactly one of x or y is True, otherwise False.
        :rtype: bool
        """
        result = x ^ y

        return result
    
    @staticmethod
    def _not(x: bool) -> bool:
        """
        Perform a logical NOT operation on a boolean value.

        Note:
            This method should use logical NOT (`not x`) rather than the
            bitwise NOT operator (`~x`) to avoid returning negative integers.

        :param x: Boolean value to invert
        :type x: bool
        :return: False if x is True, True if x is False.
        :rtype: bool
        """
        # result = ~x # Its wrong in python, its bitwise not
        result = not x

        return result
    

    @staticmethod
    def countBits(number: int) -> int:
        """
        Count the number of set bits (1s) in the binary representation
        of a non-negative integer.

        Note: Python 3.8+ has number.bit_count() for the same result.

        :param number: The integer whose set bits are to be counted. 
                       Must be a non-negative integer.
        :type number: int
        :return: The number of bits set to 1 in the binary representation.
        :rtype: int
        """
        count = 0
        while number > 0:
            if number & 1 == 1:
                count += 1
            number = number >> 1 
        
        return count

class Nand2Gates:
    ...

if __name__ == "__main__":
    bit = Bit()

    values = [(False, False), (False, True), (True, False), (True, True)]

    for value in values:
        x, y = value

        print(f""" 
        {x}, {y} =======================
            {x} & {y} = {bit._and(x, y)}
            {x} | {y} = {bit._or(x, y)}
            {x} ^ {y} = {bit._xor(x, y)}
            ~{x} = {bit._not(x)}
            ~{y} = {bit._not(y)}
        ================================
        """)

    number = 23
    count = bit.countBits(23)

    print(f"Number of 1's bits in {number} is",  count)