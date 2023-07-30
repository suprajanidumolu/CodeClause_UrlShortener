import tkinter as tk
import pyshorteners 

root = tk.Tk()
root.configure(background="orange")
root.title("URL Shortener")
root.geometry('600x300')
root.rowconfigure([0,1,2,3,4], minsize=25)
root.columnconfigure(0, minsize=100)
head = tk.Label(root, text = "URL SHORTENER", font = 'bold', fg = 'red')
head.place(x = 150,y = 10)

sh = tk.Label(root, text = "Enter the long URL : ", fg = 'blue')
sh.place(x = 150,y = 65)
url = tk.Entry(root, width = 30)
url.place(x = 150,y = 90)

def shorten():
    long = url.get()
    s = pyshorteners.Shortener()
    res['text'] = f"The shortened URL is:\n\n   {s.tinyurl.short(long)}"
    print(s.tinyurl.short(long))

btn = tk.Button(root, text = "shorten", bg = 'light green', fg = 'red', command = shorten)
btn.place(x = 340,y = 90)

fr = tk.Frame(root, bd=2,bg = 'grey')
fr.place(x=150, y=145, width=210, height=80)
res = tk.Label(root, fg = 'purple')
res.place(x = 170,y = 160)
root.mainloop()
