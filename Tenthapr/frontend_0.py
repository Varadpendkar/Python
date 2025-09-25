import tkinter as tk


# Create the main application window
root = tk.Tk()
root.title("Simple Tkinter App")
root.geometry("200x100")

#Function to pring "Hello world!" in the console 
def say_hello():
    print('Hello World!')
    print('goodbye')

hello_button = tk.Button(root, text="Click Me", command=say_hello)
hello_button.pack(pady=20)

# start the Tkinter event loop
root.mainloop()