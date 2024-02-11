import tkinter as tk
from tkinter import ttk
import subprocess
import downloadVideo

def onSubmit():
    output_text.set("Fetching URL...")
    root.update_idletasks()
    root.after(100, downloadAfterDelay)

def downloadAfterDelay():
    url = url_entry.get()
    downloadVideo(url)
    
root = tk.Tk()
root.title("Youtube Downloader")
root.minsize(400,400)
root.maxsize(400,400)
url_label = ttk.Label(root, text="Enter YouTube URL:")
url_label.pack(pady=10)

url_entry = ttk.Entry(root, width=40)
url_entry.pack(pady=10)

submit_button = ttk.Button(root, text="Download", command=onSubmit)
submit_button.pack(pady=10)

output_text = tk.StringVar()
output_label = ttk.Label(root, text="Output:")
output_label.pack(pady=10)

output_entry = ttk.Entry(root, textvariable=output_text, state="readonly", width=40)
output_entry.pack(pady=10)
#main


root.mainloop()

