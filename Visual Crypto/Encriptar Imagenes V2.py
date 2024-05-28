from PIL import Image, ImageTk
import numpy as np
import random as rd
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def read_image(filepath):
    try:
        image = Image.open(filepath).convert('1')
        return np.array(image)
    except Exception as e:
        print(f"Imagen no apropiada: {e}")
        return None

def save_image(array, filepath):
    try:
        image = Image.fromarray(array)
        image.save(filepath)
        print(f"Imagen guardada como {filepath}")
    except Exception as e:
        print("Error")

def vertical_encode(image):
    rows, cols = image.shape
    img1 = np.zeros((rows*2, cols * 2), dtype=np.uint8)
    img2 = np.zeros((rows*2, cols * 2), dtype=np.uint8)
    
    for r in range(rows):
        for c in range(cols):
            mix = rd.randint(0, 9)
            if image[r, c] == 0:
                if mix % 2 == 0:
                    img1[r*2, c * 2] = 255
                    img1[r*2+1, c * 2] = 255
                    img2[r*2, c * 2 + 1] = 255
                    img2[r*2+1, c * 2 + 1] = 255
                else:
                    img1[r*2, c * 2 + 1] = 255
                    img1[r*2+1, c * 2 + 1] = 255
                    img2[r*2, c * 2] = 255
                    img2[r*2+1, c * 2] = 255
            else:
                if mix % 2 == 0:
                    img1[r*2, c * 2] = 255
                    img1[r*2+1, c * 2] = 255
                    img2[r*2, c * 2] = 255
                    img2[r*2+1, c * 2] = 255
                else:
                    img1[r*2, c * 2 + 1] = 255
                    img1[r*2+1, c * 2 + 1] = 255
                    img2[r*2, c * 2 + 1] = 255
                    img2[r*2+1, c * 2 + 1] = 255
                
    return img1, img2

def horizontal_encode(image):
    rows, cols = image.shape
    img1 = np.zeros((rows * 2, cols*2), dtype=np.uint8)
    img2 = np.zeros((rows * 2, cols*2), dtype=np.uint8)
    
    for r in range(rows):
        for c in range(cols):
            mix = rd.randint(0, 9)
            if image[r, c] == 0:
                if mix % 2 == 0:
                    img1[r * 2, c*2] = 255
                    img2[r * 2 + 1, c*2] = 255
                    img1[r * 2, c*2+1] = 255
                    img2[r * 2 + 1, c*2+1] = 255
                else:
                    img1[r * 2 + 1, c*2] = 255
                    img2[r * 2, c*2] = 255
                    img1[r * 2 + 1, c*2+1] = 255
                    img2[r * 2, c*2+1] = 255
            else:
                if mix % 2 == 0:
                    img1[r * 2, c*2] = 255
                    img2[r * 2, c*2] = 255
                    img1[r * 2, c*2+1] = 255
                    img2[r * 2, c*2+1] = 255
                else:
                    img1[r * 2 + 1, c*2] = 255
                    img2[r * 2 + 1, c*2] = 255
                    img1[r * 2 + 1, c*2+1] = 255
                    img2[r * 2 + 1, c*2+1] = 255
                
    return img1, img2

def four_pixel_encode(image):
    rows, cols = image.shape
    img1 = np.zeros((rows * 2, cols * 2), dtype=np.uint8)
    img2 = np.zeros((rows * 2, cols * 2), dtype=np.uint8)
    
    for r in range(rows):
        for c in range(cols):
            mix = rd.randint(0, 9)
            if image[r, c] == 0:
                if mix % 2 == 0:
                    img1[r * 2, c * 2] = 255
                    img1[r * 2 + 1, c * 2 + 1] = 255
                    img2[r * 2 + 1, c * 2] = 255
                    img2[r * 2, c * 2 + 1] = 255
                else:
                    img2[r * 2, c * 2] = 255
                    img2[r * 2 + 1, c * 2 + 1] = 255
                    img1[r * 2 + 1, c * 2] = 255
                    img1[r * 2, c * 2 + 1] = 255
            else:
                if mix % 2 == 0:
                    img1[r * 2 + 1, c * 2] = 255
                    img1[r * 2, c * 2 + 1] = 255
                    img2[r * 2 + 1, c * 2] = 255
                    img2[r * 2, c * 2 + 1] = 255
                else:
                    img1[r * 2, c * 2] = 255
                    img1[r * 2 + 1, c * 2 + 1] = 255
                    img2[r * 2, c * 2] = 255
                    img2[r * 2 + 1, c * 2 + 1] = 255
                    
    return img1, img2

def decode(img1, img2, method):
    global methodUsed
    methodUsed = method
    if method == 'vertical':
        return decode_vertical(img1, img2)
    elif method == 'horizontal':
        return decode_horizontal(img1, img2)
    elif method == '4pixel':
        return decode_four_pixel(img1, img2)

def decode_vertical(img1, img2):
    rows, cols = img1.shape
    decoded = np.zeros((rows, cols), dtype=np.uint8)
    
    for r in range(rows):
        for c in range(cols):
            if img1[r, c] + img2[r, c] > 244:
                decoded[r, c] = 0
            else:
                decoded[r, c] = 255                
    return decoded

def decode_horizontal(img1, img2):
    rows, cols = img1.shape
    decoded = np.zeros((rows, cols), dtype=np.uint8)
    
    for r in range(rows):
        for c in range(cols):
            if img1[r, c] + img2[r, c] > 244:
                decoded[r, c] = 0
            else:
                decoded[r, c] = 255
                
    return decoded

def decode_four_pixel(img1, img2):
    rows, cols = img1.shape
    decoded = np.zeros((rows, cols), dtype=np.uint8)
    
    for r in range(rows):
        for c in range(cols):
            if img1[r, c] + img2[r, c] > 244:
                decoded[r, c] = 0
            else:
                decoded[r, c] = 255
                
    return decoded

def load_image():
    global image
    filepath = filedialog.askopenfilename(filetypes=[("BMP Files", "*.bmp")])
    if not filepath:
        return None, None
    image = read_image(filepath)
    if image is not None:
        display_image(image, "Imagen original.")
        return image, filepath
    else:
        messagebox.showerror("Error", "No hay imagen en memoria.")
        return None, None

def display_image(image, title):
    img = Image.fromarray(image)
    img_tk = ImageTk.PhotoImage(img)
    frame = tk.Frame(image_frame)
    frame.pack(side=tk.LEFT, padx=10)
    label = tk.Label(frame, text=title)
    label.pack()
    panel = tk.Label(frame, image=img_tk)
    panel.image = img_tk
    panel.pack()

def encode_and_display(image, method):
    global img1, img2, methodG
    if method == 'vertical':
        methodG = 'vertical'
        img1, img2 = vertical_encode(image)
    elif method == 'horizontal':
        methodG = 'horizontal'
        img1, img2 = horizontal_encode(image)
    elif method == '4pixel':
        methodG = '4pixel'
        img1, img2 = four_pixel_encode(image)
    
    display_image(img1, "Imagen codificada 1")
    display_image(img2, "Imagen codificada 2")
    
    return img1, img2

def decode_and_display(img1, img2, method):
    decoded = decode(img1, img2, method)
    display_image(decoded, "Imagen Decifrada")
    return decoded

def start_encoding(method):
    global image, filepath
    if image is None:
        messagebox.showerror("Error", "Abre una imagen primero.")
        return

    for widget in image_frame.winfo_children():
        widget.destroy()

    img1, img2 = encode_and_display(image, method)

    save_image(img1, 'Encoded1.bmp')
    save_image(img2, 'Encoded2.bmp')

def display_decoded_image():
    global img1, img2, methodG
    if image is None:
        messagebox.showerror("Error", "Abre una imagen primero.")
        return
    for widget in image_frame.winfo_children():
        widget.destroy()

    decoded = decode_and_display(img1, img2, methodG)
    save_image(decoded, 'Decoded.bmp')

def main():
    global root, image_frame, image, filepath
    image = None
    filepath = None

    root = tk.Tk()
    root.title("Criptografia Visual")

    load_button = tk.Button(root, text="Cargar Imagen", command=load_image)
    load_button.pack()

    encode_vertical_button = tk.Button(root, text="Codificar Verticalmente", command=lambda: start_encoding('vertical'))
    encode_vertical_button.pack()

    encode_horizontal_button = tk.Button(root, text="Codificar Horizontalmente", command=lambda: start_encoding('horizontal'))
    encode_horizontal_button.pack()

    encode_four_pixel_button = tk.Button(root, text="Codificar a 4 Pixeles", command=lambda: start_encoding('4pixel'))
    encode_four_pixel_button.pack()

    display_decoded_button = tk.Button(root, text="Mostrar imagen decodificada", command=display_decoded_image)
    display_decoded_button.pack()

    image_frame = tk.Frame(root)
    image_frame.pack()

    root.mainloop()

if __name__ == '__main__':
    main()

