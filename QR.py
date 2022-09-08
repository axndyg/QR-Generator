
"""

    author: Andres Gutierrez
    date: 08 - 10 - 2022

    purpose: explore python as a tool to create QR codes 
             with the qr code library 

"""

"""
imports
"""
from asyncio.windows_events import NULL
import qrcode
import cv2
import os
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask 

def main(): 
    print ("\n\"\"\"\nWelcome to the QRCode generator!\n")
    print ("This code will allow you create a custom QRCode that can be\ndownloaded to your local directory.\n\nThe data can take text, links, and image addresses.\n")
    print ("Please, take a look at the avaliable options and respond to the prompts\nto complete your QRCode.\n")
    print ("A code by Andres Gutierrez completed 08-11-2022\n\"\"\"\n")

    print ("   --------")
    print ("   1. Basic QRCode")
    print ("   2. Styled QRCode")
    print ("   3. Advance Styled QRCode")
    print ("   --------\n") 

    while True: 
        try:
            menChoice = int(input("Please enter your choice: "))
        except ValueError:
            print("Sorry, not a valid input, try again.\n")
            continue
        
        if menChoice > 4 or menChoice < 1:
            print("That number isn't an option.\n")
        else:
            break
    
    if menChoice == 1:
        genQR = getBasic()
    elif menChoice == 2:
        genQR = getStyled()
    else:
        genQR = getAdv()


    genQR.save("genQR.png")
    print("\nA new window containing your QR code will open, to continue the code,\nsimply exit it or press '0' while in the window.")
    
    display = cv2.imread("genQR.png", cv2.IMREAD_ANYCOLOR)
        #variable that takes in the image and formated color 
    cv2.imshow("QR", display)
        #prompts window to open with titel, then display content
    cv2.waitKey(0)
        #tells the window to wait till exited or exit key (in parameter)
    cv2.destroyAllWindows()
        #destroys all windows
    
    print("\n\nWould you like to keep and download the QRcode?\n")
    while True: 
        keep = str(input("   Please enter 'yes' or 'no': "))

        if 'yes' in keep.lower() or 'no' in  keep.lower():
            break
        else:
            print("Not a valid input.\n") 
            continue

    if 'yes' in keep.lower():
        print("\nFile has been saved in your local directory as: 'genQR.png'")
    else: 
        os.remove("genQR.png")
            #this removes the file from system so its temporary
            #need to implement so its a choice if you want to keep or not
            #remember, the save has to come first for cv2 to show it 

    print("\n\n\"\"\"\nThank you for using the custom QR generator!\n\"\"\"\n") 

def getBasic(): 

    data = str(input("\n   Enter the data you want encryptyed as a string: "))
        #information QR code redirects to

    img = qrcode.make(data)
        #encoding data into an image (the QR Code)

    return img
def getStyled():

    dataTwo = str(input("\n   Enter the data you want encryptyed as a string: "))
    print ("")
    
    while True: 
        try:
            verChoice = int(input("   Please enter a matrix number 1-40: "))
        except ValueError:
            print("Sorry, not a valid input, try again.\n")
            continue
        
        if verChoice > 40 or verChoice < 1:
            print("That number isn't in range.\n")
        else:
            break

    while True: 
        try:
            boxChoice = int(input("   Please enter a non-negative box number: "))
        except ValueError:
            print("Sorry, not a valid input, try again.\n")
            continue
        
        if boxChoice < 0:
            print("That number isn't an option.\n")
        else:
            break

    while True: 
        try:
            borChoice = int(input("   Please enter a border number greater than or equal to 4: "))
        except ValueError:
            print("Sorry, not a valid input, try again.\n")
            continue
        
        if borChoice < 4:
            print("That number isn't an option.\n")
        else:
            break

    advQR = qrcode.QRCode (
        version = verChoice,
            #controls overall size of qrcode
        error_correction = qrcode.constants.ERROR_CORRECT_L,
            #controls error correction
            #if data corrupts, it can recover certain %
        box_size = boxChoice,
            #controls pixel size each box of the QR
        border = borChoice,
            #controls thickness of boder on QR 
    )

    advQR.add_data(dataTwo)
    advQR.make(fit = True)
        #ensures entire version size of box is used, even if not needed

    
    rgb_fill = []
    rgb_back = []

    print("\nThe following will customize the pixel hues on the rgb scale.\n")
    for x in range(3): 
        while True: 
            try:
                colorChoice = int(input("   Please enter a number hue in range 0-255: "))
            except ValueError:
                print("Sorry, not a valid input, try again.\n")
                continue
            
            if colorChoice < 0 or colorChoice > 255:
                print("That number isn't an option.\n")
            else:
                break
        rgb_fill.append(colorChoice)
    
    print("\nThe following will customize the background hues on the rgb scale.\n")
    for x in range(3): 
        while True: 
            try:
                colorChoice = int(input("   Please enter a number hue in range 0-255: "))
            except ValueError:
                print("Sorry, not a valid input, try again.\n")
                continue
            
            if colorChoice < 0 or colorChoice > 255:
                print("That number isn't an option.\n")
            else:
                break
        rgb_back.append(colorChoice)

    imgTwo = advQR.make_image(fill_color =(rgb_fill[0],rgb_fill[1],rgb_fill[2]),
                                #the boxes color 
                            back_color= (rgb_back[0],rgb_back[1],rgb_back[2]))
                                #background color

    return imgTwo
def getAdv():

    dataThree = str(input("\n   Enter the data you want encryptyed as a string: "))
    print ("")

    qrClass = qrcode.QRCode(error_correction = qrcode.constants.ERROR_CORRECT_L)
    qrClass.add_data(dataThree)
        #qr class instance 

    print("The following will determine your cusomization options\n")

    print("   Would you like flowy pixels?\n")
    while True: 
        flowyBorder = str(input("   Please enter 'yes' or 'no': "))

        if 'yes' in flowyBorder.lower() or 'no' in  flowyBorder.lower():
            break
        else:
            print("Not a valid input.\n") 
            continue

    rgb_center = []
    rgb_edge = []

    print("\nThe following will customize the pixel gradient center color on the rgb scale.\n")
    for x in range(3): 
        while True: 
            try:
                colorChoice = int(input("   Please enter a number hue in range 0-255: "))
            except ValueError:
                print("Sorry, not a valid input, try again.\n")
                continue
            
            if colorChoice < 0 or colorChoice > 255:
                print("That number isn't an option.\n")
            else:
                break
        rgb_center.append(colorChoice)

    print("\nThe following will customize the pixel gradient edge color on the rgb scale.\n")
    for x in range(3): 
        while True: 
            try:
                colorChoice = int(input("   Please enter a number hue in range 0-255: "))
            except ValueError:
                print("Sorry, not a valid input, try again.\n")
                continue
            
            if colorChoice < 0 or colorChoice > 255:
                print("That number isn't an option.\n")
            else:
                break
        rgb_edge.append(colorChoice)

    print("\nNow enter the path of an image you want centered on the QRCode (with forward slashes)\n   or just press enter for no image")
    while True:
        embeddedImage = str(input("\n   Enter Path here: "))
        
        if os.path.exists(embeddedImage) == True or embeddedImage == '':
            break
        else:
            print("Invalid Path, try again.")
        

    if 'yes' in flowyBorder.lower(): 
        imgThree = qrClass.make_image(image_factory = StyledPilImage, module_drawer = RoundedModuleDrawer(), color_mask = RadialGradiantColorMask(edge_color=(rgb_edge[0],rgb_edge[1],rgb_edge[2]), center_color=(rgb_center[0],rgb_center[1],rgb_center[2])), embeded_image_path= embeddedImage)
    else: 
        imgThree = qrClass.make_image(image_factory = StyledPilImage, color_mask = RadialGradiantColorMask(edge_color=(rgb_edge[0],rgb_edge[1],rgb_edge[2]), center_color=(rgb_center[0],rgb_center[1],rgb_center[2])), embeded_image_path= embeddedImage)

    return imgThree

main()

#svg holder 
"""
    def getSVG():

        import qrcode.image.svg

        method = "basic"
        #also possibility: fragment / path, types of factories that format the SVG
        
        if method == 'basic':
            factory = qrcode.image.svg.SvgImage
        elif method == 'fragment':
            factory = qrcode.image.Svg.SvgFragmentImage
        elif method == 'path':
            factory = qrcode.image.svg.SvgPathImage

        dataFour = "https://www.google.com/maps/@43.7684737,11.2573475,3a,75y,76.88h,90.38t/data=!3m7!1e1!3m5!1shh3QCRWdY1qS2LNeXnZqag!2e0!6shttps:%2F%2Fstreetviewpixels-pa.googleapis.com%2Fv1%2Fthumbnail%3Fpanoid%3Dhh3QCRWdY1qS2LNeXnZqag%26cb_client%3Dmaps_sv.tactile.gps%26w%3D203%26h%3D100%26yaw%3D123.530876%26pitch%3D0%26thumbfov%3D100!7i16384!8i8192"

        imgFour = qrcode.make(dataFour, image_factory = factory)

        return imgFour
"""

### doesnt take online images with image addresses right now