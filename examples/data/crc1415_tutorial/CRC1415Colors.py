"""DOCSTRING:"""

def ShowColors():
    """
    Shows list of colors in CRCcd.
    """
    CRCcd = ReturnCRCDict()
    return list(CRCcd.keys())  # Directly get the keys as a list 
    

def CRCcolor(color: str) -> tuple:
    """
    Converts string from dict CRCcd to [0, 1] and returns as tuple. Needed for Matplotlib.

    color: str .... color from CRCcd standart colors.     
    return: tuple

    example: CRCcdToMpl("black")
                returns (R, G, B) = (0.0, 0.0, 0.0)
    """
    standardReturn = (0.0, 0.0, 0.0)


    if type(color) != str:
        print("ERROR: Please put color as string from CRCcd. Black is returned.")
        ShowColors()
        return standardReturn
    

    CRCcd = ReturnCRCDict()
    try:
        choosenColor = CRCcd[color]
        R = float(choosenColor[0]) / 255.0
        G = float(choosenColor[1]) / 255.0
        B = float(choosenColor[2]) / 255.0 
        RGBTuple = (R, G, B)
        return RGBTuple

    except KeyError:
        print("ERROR: This color is not part of CRCcd:", color, ",Black is returned.")
        ShowColors()
        return standardReturn

    

def ReturnCRCDict():
    """
    Returns dict of CRC1415 colors as with color string as key and corresponding RGB tuple as ints (0..255, 0..255, 0..255) as value.
    """
    CRCcd = {
    "black" : (000, 000, 000),
    "white" : (255, 255, 255),
    "CRC1415A00"  : ( 70, 121, 167), 
    "CRC1415A01"  : ( 85, 145, 199), 
    "CRC1415A02"  : (132, 174, 220), 
    "CRC1415A03"  : (184, 205, 232), 
    "CRC1415B00"  : (191, 144,   0), 
    "CRC1415B01"  : (238, 181,   0), 
    "CRC1415B02"  : (255, 213, 151), 
    "CRC1415B03"  : (255, 226, 183), 
    "CRC1415C00"  : ( 84, 130,  53), 
    "CRC1415C01"  : (102, 158,  64), 
    "CRC1415C02"  : (143, 187, 119), 
    "CRC1415C03"  : (172, 202, 158), 
    "CRC1415Z00"  : (196,  28,   0), 
    "CRC1415Z01"  : (255, 101,  75), 
    "CRC1415Z02"  : (255, 162, 147), 
    "CRC1415Z03"  : (255, 209, 201)
    }   
    return CRCcd
    
if __name__ == "__main__":
    main()
