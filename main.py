import tkinter as tk
from tkinter import ttk
import subprocess


def onSubmit():
    output_text.set("Fetching URL...")
    root.update_idletasks()
    root.after(100, downloadAfterDelay)

def downloadAfterDelay():
    url = url_entry.get()
    downloadVideo(url)
    
def downloadVideo(url):
    command = f"yt-dlp -x -o \"%(title)s.%(ext)s\" --audio-format \"m4a\" --audio-quality 0 --embed-thumbnail --embed-metadata  --verbose '{url}'"
    #print(command)
    try:
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        while True:
            line = process.stdout.readline()
            if not line and process.poll() is not None:
                break

            # Display live output in a text widget
            output_text.set(line.strip())
            output_entry.update_idletasks()

        # Check if the process completed successfully
        if process.returncode == 0:
            output_text.set("Audio Downloaded Successfully.")
        else:
            output_text.set(f"Error: {process.stderr.read().strip()}")
        #todo : add setoutput var
    except subprocess.CalledProcessError as e:
        output_text.set(f"Error: {e.output}")
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

