from PIL import Image
from tkinter import filedialog   

def load_image():
    return Image.open(filedialog.askopenfilename(title="Select Image To Encrypt/Decrypt.",filetypes=[("Image files","*.jpg *.jpeg *.gif")]))
     

def encrypt_decrypt(img,type):

    pixels = img.load()
    height = img.height
    width = img.width

    if type == "encrypt":
        horizontal_pixel_swap(width,height,pixels)
        vertical_pixel_swap(width,height,pixels)
    else:
        vertical_pixel_swap(width,height,pixels)
        horizontal_pixel_swap(width,height,pixels)

    return img

def horizontal_pixel_swap(width,height,pixels):
    for h in range(height):
        for w in range(0, width - 19, 20):  # Iterate in blocks of 20 along width
            # Swap 0 with 19, 1 with 18, 2 with 17, 3 with 16, and 4 with 15. etc
            for i in range(10):
                r1, g1, b1 = pixels[w + i, h]
                r2, g2, b2 = pixels[w + (19 - i), h]
                # Swap the pixels
                pixels[w + i, h] = (r2, g2, b2)
                pixels[w + (19 - i), h] = (r1, g1, b1)


def vertical_pixel_swap(width,height,pixels):
    for w in range(width):
        for h in range(0, height - 19, 20):  # Iterate in blocks of 20 along height
            # Swap 0 with 19, 1 with 18, 2 with 17, 3 with 16, and 4 with 15..etc 
            for i in range(10):
                r1, g1, b1 = pixels[w, h + i]
                r2, g2, b2 = pixels[w, h + (19 - i)]
                # Swap the pixels
                pixels[w, h + i] = (r2, g2, b2)
                pixels[w, h + (19 - i)] = (r1, g1, b1)

def save_image(img,type,image_name):
    img.save(f"{type}_{image_name}.jpeg")

def getType():
    print("If You Want To End The Program Enter 1\n")
    type = input("Would You Like To Encrypt Or Decrypt An Image?")
    if type.lower() in ["encrypt","decrypt"]:
        return type
    elif type  == "1":
        return None
    else: return getType()


def get_image_name():
    return input("\nEnter A Name To Save The New Image: ")

if __name__ == "__main__":
    print("*** Welcome To The Image Encryption/Decryption Program ***")
    while(True):
        type = getType()
        if type == None:
            break

        image = load_image()
        image = encrypt_decrypt(image,type)
        image_name = get_image_name()
        save_image(image,type,image_name)
    print("\n*** Thank You For Using The Image Encryption/Decryption Program ***")