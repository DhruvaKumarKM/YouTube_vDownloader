import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from pytube import YouTube

def download_video():
    url = url_entry.get()
    path = filedialog.askdirectory()
    try:
        yt = YouTube(url)
        video = yt.streams.first()
        video.download(path)
        messagebox.showinfo("Info", "Video downloaded successfully!")
    except:
        messagebox.showerror("Error", "An error occurred while downloading the video.")

root = tk.Tk()
root.title("YouTube Video Downloader created by DHRUVA")
root.config(bg='black')
root.geometry("600x400")
root.geometry('500x570+100+30')

url_label = tk.Label(root, text="Enter the URL of the YouTube video:")
url_label.pack(pady=10)

url_entry = tk.Entry(root)
url_entry.pack(pady=10,padx=20)

download_button = tk.Button(root, text="Download", command=download_video)
download_button.pack(pady=5)

root.mainloop()
