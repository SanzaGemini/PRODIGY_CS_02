from PIL import Image
from tkinter import filedialog

def loadImage():
    """
    Prompts the user to select an image file and loads it.

    Returns:
        Image: The loaded image.
    """
    return Image.open(filedialog.askopenfilename(
        title="Select Image To Encrypt/Decrypt.",
        filetypes=[("Image files", "*.jpg *.jpeg *.gif")]
    ))

def encryptDecrypt(img, operationType):
    """
    Encrypts or decrypts an image by swapping pixels horizontally and vertically.

    Args:
        img (Image): The image to be processed.
        operationType (str): "encrypt" or "decrypt", determines the operation.

    Returns:
        Image: The processed image.
    """
    pixels = img.load()
    height = img.height
    width = img.width

    if operationType == "encrypt":
        horizontalPixelSwap(width, height, pixels)
        verticalPixelSwap(width, height, pixels)
    else:
        verticalPixelSwap(width, height, pixels)
        horizontalPixelSwap(width, height, pixels)

    return img

def horizontalPixelSwap(width, height, pixels):
    """
    Swaps pixels horizontally in blocks of 20 pixels width.

    Args:
        width (int): Width of the image.
        height (int): Height of the image.
        pixels (PixelAccess): Pixel access object for the image.
    """
    for h in range(height):
        for w in range(0, width - 19, 20):  # Iterate in blocks of 20 along width
            for i in range(10):
                r1, g1, b1 = pixels[w + i, h]
                r2, g2, b2 = pixels[w + (19 - i), h]
                pixels[w + i, h] = (r2, g2, b2)
                pixels[w + (19 - i), h] = (r1, g1, b1)

def verticalPixelSwap(width, height, pixels):
    """
    Swaps pixels vertically in blocks of 20 pixels height.

    Args:
        width (int): Width of the image.
        height (int): Height of the image.
        pixels (PixelAccess): Pixel access object for the image.
    """
    for w in range(width):
        for h in range(0, height - 19, 20):  # Iterate in blocks of 20 along height
            for i in range(10):
                r1, g1, b1 = pixels[w, h + i]
                r2, g2, b2 = pixels[w, h + (19 - i)]
                pixels[w, h + i] = (r2, g2, b2)
                pixels[w, h + (19 - i)] = (r1, g1, b1)

def saveImage(img, operationType, imageName):
    """
    Saves the processed image with a given name.

    Args:
        img (Image): The image to be saved.
        operationType (str): "encrypt" or "decrypt", used to prefix the filename.
        imageName (str): The name to save the image as.
    """
    img.save(f"{operationType}_{imageName}.jpeg")

def getOperationType():
    """
    Prompts the user for the operation type (encrypt/decrypt).

    Returns:
        str or None: "encrypt" or "decrypt", or None if the user chooses to exit.
    """
    print("\nIf You Want To End The Program Enter 1")
    operationType = input("\nWould You Like To Encrypt Or Decrypt An Image?\n")

    if operationType.lower() in ["encrypt", "decrypt"]:
        return operationType
    elif operationType == "1":
        return None
    else:
        return getOperationType()

def getImageName():
    """
    Prompts the user to provide a name for saving the new image.

    Returns:
        str: The name entered by the user.
    """
    return input("\nEnter A Name To Save The New Image: \n")

if __name__ == "__main__":
    print("*** Welcome To The Image Encryption/Decryption Program ***")

    while True:
        operationType = getOperationType()

        if operationType is None:
            break

        image = loadImage()
        image = encryptDecrypt(image, operationType)
        imageName = getImageName()
        saveImage(image, operationType, imageName)

    print("\n*** Thank You For Using The Image Encryption/Decryption Program ***")
