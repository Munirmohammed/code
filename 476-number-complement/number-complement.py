class Solution(object):
    def findComplement(self, num):
        def decimal_to_binary(n):
            if n == 0:
                return "0"
            binary = ""
            while n > 0:
                binary = str(n % 2) + binary
                n = n // 2
            return binary

        def binary_to_decimal(binary_str):
            decimal = 0
            binary_str = binary_str[::-1]  
            for i in range(len(binary_str)):
                decimal += int(binary_str[i]) * (2 ** i)
            return decimal

        binary = decimal_to_binary(num)
        n = len(binary)

        complement = ''
        for i in range(n):
            if binary[i] == '0':
                complement += '1'
            else:
                complement += '0'

        return binary_to_decimal(complement)        