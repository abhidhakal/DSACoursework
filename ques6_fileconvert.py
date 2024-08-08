# This scenario presents another sample Java GUI application using multithreading and an asynchronous framework
# (SwingWorker) to demonstrate asynchronous progress updates and batch processing.
# Features:
# File selection dialog: Choose multiple files for conversion.
# Conversion options: Select the desired output format (e.g., PDF to Docx, image resize).
# Start button: Initiates conversion of selected files concurrently.
# Progress bar: Shows overall conversion progress with individual file indicators.
# Status bar: Displays information about each file being processed (name, conversion type, progress).
# Cancel button: Allows stopping the entire conversion process or individual files.
# Completion notification: Provides a message when all conversions are finished.
# Challenges:
# Efficiently manage multiple file conversions using separate threads.
# Update the GUI asynchronously to show individual file progress without blocking the main thread.
# Handle potential errors during file access or conversion and provide informative feedback.
# Allow cancelling specific files or the entire process gracefully.
# Implementation:
# Swing GUI: Design a graphical interface using Swing components for file selection, buttons, progress bars, and
# status messages.
# Multithreading: Use a thread pool to manage multiple conversion threads efficiently.

import customtkinter as ctk
from tkinter import filedialog, messagebox
import time
import concurrent.futures

ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class FileConversionApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("File Conversion App")
        self.geometry("600x500")

        # Create main frame
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Create components
        self.file_selector = ctk.CTkButton(self.main_frame, text="Select Files", command=self.select_files)
        self.file_selector.pack(pady=10, padx=10, fill="x")

        self.conversion_type = ctk.CTkOptionMenu(self.main_frame, values=["PDF to Docx", "Image Resize"])
        self.conversion_type.pack(pady=10, padx=10, fill="x")

        self.conversion_starter = ctk.CTkButton(self.main_frame, text="Start Conversion", command=self.start_conversion)
        self.conversion_starter.pack(pady=10, padx=10, fill="x")

        self.conversion_canceller = ctk.CTkButton(self.main_frame, text="Cancel", command=self.cancel_conversion, fg_color="red", hover_color="dark red")
        self.conversion_canceller.pack(pady=10, padx=10, fill="x")

        self.progress = ctk.CTkProgressBar(self.main_frame)
        self.progress.pack(pady=10, padx=10, fill="x")
        self.progress.set(0)

        self.status_display = ctk.CTkTextbox(self.main_frame, height=200, state="disabled")
        self.status_display.pack(pady=10, padx=10, fill="both", expand=True)

        self.selected_files = []
        self.executor = None
        self.futures = []

    def select_files(self):
        files = filedialog.askopenfilenames()
        self.selected_files = files
        self.update_status(f"Selected files:\n{', '.join(self.selected_files)}\n")

    def update_status(self, message):
        self.status_display.configure(state="normal")
        self.status_display.insert("end", message + "\n")
        self.status_display.configure(state="disabled")
        self.status_display.see("end")

    def process_file(self, file, conversion_type):
        try:
            for i in range(11):
                time.sleep(0.5)
                self.update_status(f"Processing {file}: {i * 10}%")
                self.progress.set((i + 1) / 11)
            self.update_status(f"Finished processing {file}")
        except Exception as e:
            self.update_status(f"Error processing {file}: {str(e)}")

    def start_conversion(self):
        if not self.selected_files:
            messagebox.showerror("Error", "No files selected!")
            return

        conversion_type = self.conversion_type.get()
        if not conversion_type:
            messagebox.showerror("Error", "No conversion type selected!")
            return

        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=len(self.selected_files))
        self.futures = [self.executor.submit(self.process_file, file, conversion_type) for file in self.selected_files]
        self.update_status("Conversion started...")

    def cancel_conversion(self):
        if self.executor:
            self.executor.shutdown(wait=False)
            for future in self.futures:
                future.cancel()
            self.update_status("Conversion cancelled.")
        
if __name__ == "__main__":
    app = FileConversionApp()
    app.mainloop()