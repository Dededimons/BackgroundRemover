from rembg import remove
from PIL import Image
import tkinter as tk
from tkinter import filedialog
import secrets


def select_image():
    file_path = filedialog.askopenfilename(title="Select Image File", filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif")])
    if file_path:
        label.config(text="Selected Image: " + file_path)

        def generate_random_string(length):
            return secrets.token_hex(length // 2)[:length]
        random_string = generate_random_string(8)

        input_image = file_path
        output_image = "C:/Users/erikt/Desktop/" + random_string+".png"
        input = Image.open(input_image)
        output = remove(input)
        output.save(output_image)


root = tk.Tk()
root.title("BGremover")
root.geometry("400x150")


label = tk.Label(root, text="Selected Image:")
label.pack(pady=10)


select_button = tk.Button(root, text="Select Image", command=select_image)
select_button.pack(pady=5)

root.mainloop()

