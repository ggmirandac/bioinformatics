def ReverseComplement(Pattern):   
    Pattern = Reverse(Pattern) # reverse all letters in a string
    Pattern = Complement(Pattern) # complement each letter in a string
    return Pattern

def Reverse(Pattern):
    return Pattern[::-1]


def Complement(Pattern):
    text=""
    for letra in Pattern:
        if letra=="T":
            text+="A"
        if letra=="A":
            text+="T"
        if letra=="G":
            text+="C"
        if letra=="C":
            text+="G"
    return text

print(ReverseComplement("TTGTGTC"))