from PIL import Image

value = 123

def load_image():
    img = Image.open("Prodigy_infotech.jpeg")
    return img

def encrypt_decrypt(img):
    pixel = img.load()
    for w in range(img.width):
        for h in range(img.height):
            r,g,b = pixel[w, h]
            pixel[w, h] = (r ^ value , g ^ value , b ^ value)

    return img

def save_image(img,type):
    img.save(f"{type}_Prodigy_infotech.jpeg")

if __name__ == "__main__":
    image = load_image()
    image = encrypt_decrypt(image)
    save_image(image,"encrypt")