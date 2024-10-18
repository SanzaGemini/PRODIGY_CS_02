

# PRODIGY_CS_02: Image Encryption/Decryption Program

This Python program allows users to encrypt and decrypt images by manipulating pixel positions through a defined swapping pattern. It provides a simple, interactive interface for users to select an image, choose whether to encrypt or decrypt it, and save the processed image with a new name.

## Features:
- **Image Encryption:** Obscures the image by swapping pixels in a defined horizontal and vertical pattern.
- **Image Decryption:** Reverses the encryption by applying the same pixel-swapping technique in reverse order.
- **Interactive User Input:** Allows users to select images using a graphical file dialog and specify the output file name.
  
## Dependencies:
- **Pillow (PIL):** For handling image operations (loading, manipulating, saving).
- **Tkinter:** Used for displaying a file dialog for image selection.

## How It Works:
1. **Image Selection:**  
   - The user is prompted to select an image using a GUI-based file dialog. The program supports `.jpg`, `.jpeg`, and `.gif` formats.

2. **Encryption/Decryption Process:**
   - **Encryption:** Swaps pixels horizontally and vertically to modify the image.
   - **Decryption:** Swaps pixels in reverse order (vertically first, then horizontally) to restore the original image.

3. **Pixel Swapping:**  
   - **Horizontal Pixel Swap:** Swaps pixels in blocks of 20 along the image's width, reversing the position of each block.
   - **Vertical Pixel Swap:** Similar to horizontal swapping, but applied along the image's height.

4. **Saving the Image:**  
   - After encryption/decryption, the user is prompted to name the file. The processed image is saved as a JPEG file, with a prefix indicating whether it was encrypted or decrypted.

5. **Program Termination:**  
   - Users can exit the program by entering `1` when prompted for encryption or decryption.

## Functions:

- **`loadImage()`**: Opens a file dialog for selecting an image to process.
- **`encryptDecrypt(img, operationType)`**: Processes the image based on the selected operation (encrypt/decrypt).
- **`horizontalPixelSwap(width, height, pixels)`**: Swaps pixels horizontally in blocks of 20.
- **`verticalPixelSwap(width, height, pixels)`**: Swaps pixels vertically in blocks of 20.
- **`saveImage(img, operationType, imageName)`**: Saves the processed image with a user-defined name.
- **`getOperationType()`**: Prompts the user to choose between encryption and decryption.
- **`getImageName()`**: Prompts the user for a name to save the processed image.

## How to Use:

### 1. Install Required Libraries:
Ensure you have `Pillow` and `Tkinter` installed. You can install them using the following commands:

```bash
pip install pillow
sudo apt-get install python3-tk
```

### 2. Run the Program:
```bash
python image_encryption.py
```

### 3. Follow the Prompts:
- Choose whether to encrypt or decrypt.
- Select the image you wish to process using the file dialog.
- Provide a name for the new, processed image.

The new image will be saved in the current working directory with either `encrypt_` or `decrypt_` prefixed to the file name.

### Example:

1. **Encryption Example:**
   - You select `sample.jpg` and choose to encrypt it.
   - After processing, you are prompted to enter a name for the new file. You type `encrypted_image`, and the program saves the file as `encrypt_encrypted_image.jpeg`.

2. **Decryption Example:**
   - After encrypting, you choose to decrypt the encrypted image.
   - You select the file, enter `decrypted_image`, and the program saves the result as `decrypt_decrypted_image.jpeg`.

## Notes:
- Only supports `.jpg`, `.jpeg`, and `.gif` formats.
- The decryption will only work correctly if the image was previously encrypted with the same algorithm. If the image was altered or corrupted, decryption may not restore the original image.

## License:
This project is open-source and free to use for personal and educational purposes.