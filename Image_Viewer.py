import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Viewer")
        self.root.geometry("800x600")

        # Label to display images
        self.image_label = tk.Label(root)
        self.image_label.pack(expand=True)

        # Frame for buttons
        self.btn_frame = tk.Frame(root)
        self.btn_frame.pack(side=tk.BOTTOM, fill=tk.X)

        # Buttons for navigation and actions
        self.prev_button = tk.Button(self.btn_frame, text="Previous", command=self.show_previous)
        self.prev_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.next_button = tk.Button(self.btn_frame, text="Next", command=self.show_next)
        self.next_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.open_button = tk.Button(self.btn_frame, text="Open Folder", command=self.load_images)
        self.open_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.exit_button = tk.Button(self.btn_frame, text="Exit", command=root.quit)
        self.exit_button.pack(side=tk.LEFT, padx=10, pady=10)

        # Variables to store images
        self.image_paths = []
        self.current_index = 0

    def load_images(self):
        """Opens a folder and loads all image files."""
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.image_paths = [os.path.join(folder_selected, f) for f in os.listdir(folder_selected)
                                if f.lower().endswith(('png', 'jpg', 'jpeg', 'bmp'))]
            if self.image_paths:
                self.current_index = 0
                self.display_image()
            else:
                print("No valid image files found in the selected folder.")

    def display_image(self):
        """Displays the current image."""
        if self.image_paths:
            img_path = self.image_paths[self.current_index]
            img = Image.open(img_path)
            img = img.resize((700, 500), Image.Resampling.LANCZOS)
            img = ImageTk.PhotoImage(img)

            self.image_label.config(image=img)
            self.image_label.image = img

    def show_next(self):
        """Displays the next image."""
        if self.image_paths and self.current_index < len(self.image_paths) - 1:
            self.current_index += 1
            self.display_image()

    def show_previous(self):
        """Displays the previous image."""
        if self.image_paths and self.current_index > 0:
            self.current_index -= 1
            self.display_image()

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageViewer(root)
    root.mainloop()
