# The objective of this challenge is to convert the given hex string into base64 format
# hex string = 49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d

hexString = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
def hexToBin(hexString):
    binOfHex=''
    for char in hexString:
        if char == '0':
            binOfHex+='0000'
        elif char == '1':
            binOfHex+='0001'
        elif char == '2':
            binOfHex+='0010'
        elif char == '3':
            binOfHex+='0011'
        elif char == '4':
            binOfHex+='0100'
        elif char == '5':
            binOfHex+='0101'
        elif char == '6':
            binOfHex+='0110'
        elif char == '7':
            binOfHex+='0111'
        elif char == '8':
            binOfHex+='1000'
        elif char == '9':
            binOfHex+='1001'
        elif char == 'a':
            binOfHex+='1010'
        elif char == 'b':
            binOfHex+='1011'
        elif char == 'c':
            binOfHex+='1100'
        elif char == 'd':
            binOfHex+='1101'
        elif char == 'e':
            binOfHex+='1110'
        elif char == 'f':
            binOfHex+='1111'
    return binOfHex

def binToBase64(binnum):
    base64EncodedText=''
    b64_index_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    for i in range(0,len(binnum),6):
        chunk = binnum[i:i+6]
        decValueOfChunk=int(chunk,2)
        base64EncodedText+=b64_index_table[decValueOfChunk]   
    return base64EncodedText

output=binToBase64(hexToBin(hexString))
print(output)