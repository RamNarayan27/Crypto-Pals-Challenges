# Challenge 2
# Fixed XOR
# Produce an XOR combination of two equal-length buffers
def xorTheHexValues(hex1,hex2):
    num = hex1^hex2
    return hex(int(num))


if __name__ == "__main__":
    hexstring1 = '1c0111001f010100061a024b53535009181c'
    hexstring2 = '686974207468652062756c6c277320657965'
    hexnum1 = '0x'+hexstring1
    hexnum2 = '0x'+hexstring2
    Value = xorTheHexValues(int(hexnum1,16),int(hexnum2,16))
    print(Value)