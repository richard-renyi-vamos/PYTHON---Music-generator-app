import tkinter as tk
from tkinter import ttk
from pydub.generators import Sine
import os

class MusicGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Generator")
        
        # Frequency and Duration options
        self.freq_label = ttk.Label(root, text="Frequency (Hz):")
        self.freq_label.grid(row=0, column=0, padx=10, pady=10)
        
        self.freq_entry = ttk.Entry(root)
        self.freq_entry.grid(row=0, column=1, padx=10, pady=10)
        self.freq_entry.insert(0, "440")

        self.duration_label = ttk.Label(root, text="Duration (ms):")
        self.duration_label.grid(row=1, column=0, padx=10, pady=10)

        self.duration_entry = ttk.Entry(root)
        self.duration_entry.grid(row=1, column=1, padx=10, pady=10)
        self.duration_entry.insert(0, "500")

        # Buttons
        self.generate_button = ttk.Button(root, text="Generate Tone", command=self.generate_tone)
        self.generate_button.grid(row=2, column=0, columnspan=2, pady=20)

        self.play_button = ttk.Button(root, text="Play Tone", command=self.play_tone, state=tk.DISABLED)
        self.play_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.file_path = None

    def generate_tone(self):
        try:
            frequency = float(self.freq_entry.get())
            duration = int(self.duration_entry.get())

            # Generate tone using Sine wave
            tone = Sine(frequency).to_audio_segment(duration=duration)

            # Save tone to file
            self.file_path = "generated_tone.wav"
            tone.export(self.file_path, format="wav")

            self.play_button["state"] = tk.NORMAL
            ttk.Label(self.root, text="Tone generated successfully!", foreground="green").grid(row=4, column=0, columnspan=2, pady=5)
        except Exception as e:
            ttk.Label(self.root, text=f"Error: {str(e)}", foreground="red").grid(row=4, column=0, columnspan=2, pady=5)

    def play_tone(self):
        if self.file_path and os.path.exists(self.file_path):
            os.system(f"start {self.file_path}")  # This works on Windows. Use "afplay" for Mac or "aplay" for Linux.
        else:
            ttk.Label(self.root, text="No tone found to play!", foreground="red").grid(row=5, column=0, columnspan=2, pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicGeneratorApp(root)
    root.mainloop()
