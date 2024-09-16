# PRODIGY_CS_02
# Image Encryption/Decryption Program

This Python program allows users to encrypt and decrypt images using pixel manipulation. The program swaps pixels both horizontally and vertically based on a defined pattern. The user can interactively load an image using a file dialog, choose whether to encrypt or decrypt it, and save the result with a new name.

## Features:
- **Image Encryption:** Pixel swapping is applied to obscure the original image.
- **Image Decryption:** The same pixel swapping technique is used to reverse the encryption.
- **User Interaction:** A GUI-based file selection dialog allows users to select images for encryption/decryption, and the user can specify the file name for saving the processed image.

## Dependencies:
- **Pillow (PIL):** A Python Imaging Library (Pillow) fork used to handle image manipulation.
- **Tkinter:** Used for file dialog to allow users to select an image file easily.

## How it Works:
1. **Image Selection:** 
   - The program prompts the user to select an image using a file dialog.
   - It accepts `.jpg`, `.jpeg`, and `.gif` formats.

2. **Encryption/Decryption Process:**
   - **Encryption:** If the user chooses to encrypt, the pixels are swapped horizontally and then vertically using a predefined swapping algorithm.
   - **Decryption:** If the user chooses to decrypt, the same swapping is applied but in reverse order: first vertical swap, then horizontal swap.

3. **Pixel Swapping:** 
   - **Horizontal Pixel Swap:** Swaps pixels in blocks of 20 along the width. For each block, pixel 0 is swapped with pixel 19, pixel 1 with pixel 18, and so on.
   - **Vertical Pixel Swap:** Swaps pixels in blocks of 20 along the height, following the same pattern as horizontal swapping.

4. **Saving the Image:**
   - After the image is processed, the user is prompted to enter a name for the new image. The image is saved as a JPEG file, prefixed with either "encrypt_" or "decrypt_" depending on the operation.

5. **Program Termination:**
   - The user can end the program by entering `1` when prompted for encryption/decryption.

## Functions:

- `load_image()`: Opens a file dialog for the user to select an image file.
- `encrypt_decrypt(img, type)`: Encrypts or decrypts the image based on the user's choice by calling the appropriate pixel-swapping functions.
- `horizontal_pixel_swap(width, height, pixels)`: Swaps pixels in blocks of 20 along the width of the image.
- `vertical_pixel_swap(width, height, pixels)`: Swaps pixels in blocks of 20 along the height of the image.
- `save_image(img, type, image_name)`: Saves the processed image with a new file name.
- `getType()`: Prompts the user to choose between encrypting or decrypting an image.
- `get_image_name()`: Prompts the user for a file name to save the processed image.

## How to Use:

1. Install the required libraries:
   ```bash
   pip install pillow
   sudo apt-get install python3-tk
   ```

2. Run the program:
   ```bash
   python image_encryption.py
   ```

3. Follow the prompts:
   - Choose whether to encrypt or decrypt.
   - Select an image file to process.
   - Provide a name to save the processed image.

4. The encrypted or decrypted image will be saved in the current directory with the specified name.

## Example:

1. **Encryption:** You select an image `sample.jpg` and choose to encrypt it. The program processes the image and prompts you to enter a name for the new image. You type `encrypted_image`, and the program saves the result as `encrypt_encrypted_image.jpeg`.

2. **Decryption:** You then choose to decrypt the same image. After selecting the encrypted file, you type `decrypted_image` and the program saves it as `decrypt_decrypted_image.jpeg`.

## Notes:
- Ensure that the image format is supported (`.jpg`, `.jpeg`, or `.gif`).
- The encryption and decryption algorithms rely on the exact pixel-swapping method, so decryption is only successful if the image was encrypted using the same algorithm.

## License:
This program is open-source and free to use for personal or educational purposes.
