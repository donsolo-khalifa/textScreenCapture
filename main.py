import easyocr
import numpy as np
from pynput import keyboard
import tkinter as tk
from PIL import ImageGrab
import pyperclip
from tkinter import messagebox


class ScreenCaptureOCR:
    def __init__(self):
        self.reader = easyocr.Reader(["en"])
        self.start_x = None
        self.start_y = None
        self.rect_id = None
        self.root = None
        self.canvas = None
        self.is_active = False

    def on_select(self, event):
        """Record the initial point of selection."""
        self.start_x, self.start_y = event.x, event.y

    def on_drag(self, event):
        """Update the selection rectangle while dragging."""
        if self.rect_id:
            self.canvas.delete(self.rect_id)
        self.rect_id = self.canvas.create_rectangle(
            self.start_x, self.start_y, event.x, event.y,
            outline="red", width=2
        )

    def on_release(self, event):
        """Capture the selected area and process the image."""
        try:
            x1 = min(self.root.winfo_rootx() + self.start_x, self.root.winfo_rootx() + event.x)
            y1 = min(self.root.winfo_rooty() + self.start_y, self.root.winfo_rooty() + event.y)
            x2 = max(self.root.winfo_rootx() + self.start_x, self.root.winfo_rootx() + event.x)
            y2 = max(self.root.winfo_rooty() + self.start_y, self.root.winfo_rooty() + event.y)

            if abs(x2 - x1) < 10 or abs(y2 - y1) < 10:
                messagebox.showwarning("Warning", "Selection area too small!")
                self.close_tk()
                return

            # Take a screenshot of the selected area
            screenshot = ImageGrab.grab(bbox=(x1, y1, x2, y2))

            # Convert the screenshot to a NumPy array
            screenshot_array = np.array(screenshot)

            # Extract text using EasyOCR
            result = self.reader.readtext(screenshot_array)

            # Extract and copy text to clipboard
            extracted_text = "\n".join([text for _, text, _ in result])

            if extracted_text:
                pyperclip.copy(extracted_text)
                print("Extracted text copied to clipboard!")
                print("\nExtracted Text:\n" + extracted_text)
            else:
                print("No text detected!")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
        finally:
            self.close_tk()

    def close_tk(self):
        """Safely destroy the Tkinter window."""
        if self.root:
            self.root.destroy()
            self.root = None
            self.is_active = False

    def activate_selection(self):
        """Activate the selection window."""
        if self.is_active:
            return

        self.is_active = True
        self.root = tk.Tk()
        self.root.attributes("-fullscreen", True, "-topmost", True)
        self.root.attributes("-alpha", 0.3)
        self.root.config(cursor="cross")

        self.root.bind("<Escape>", lambda e: self.close_tk())

        self.canvas = tk.Canvas(self.root, bg="gray20")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.rect_id = None
        self.canvas.bind("<Button-1>", self.on_select)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

        self.root.mainloop()

    def on_key_press(self, key):
        """Handle Print Screen key press."""
        if key == keyboard.Key.print_screen:
            if not self.is_active:
                self.activate_selection()

    def start(self):
        """Start the application."""
        with keyboard.Listener(on_press=self.on_key_press) as listener:
            print("Screen Capture OCR started. Press Print Screen to activate selection.")
            listener.join()


if __name__ == "__main__":
    app = ScreenCaptureOCR()
    app.start()