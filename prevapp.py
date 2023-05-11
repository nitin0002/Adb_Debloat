'''
Create a GUI using a Python library such as Tkinter, PyQt, or wxPython to display the list of sorted packages
and allow the user to select and uninstall packages. Here is an example using Tkinter
'''
import tkinter as tk
import subprocess
import pandas as pd

def mainApp():
    # Load sorted packages into a list
    df = pd.read_csv('sorted_packages.csv')
    packages = df['package_name'].tolist()

    # Define a function to uninstall selected packages
    def uninstall_selected():
        selected = [packages[i] for i in lb.curselection()]
        for package in selected:
            subprocess.run(['adb','shell', 'pm', 'uninstall','--user','0', package])

    # Create a Tkinter window and listbox to display packages
    root = tk.Tk()
    root.geometry("800x600")
    lb = tk.Listbox(root,width=90, height=28,font=('courier', 12))
    for package in packages:
        lb.insert(tk.END, package)

    # Add a button to uninstall selected packages
    btn_uninstall = tk.Button(root, text="Uninstall Selected", command=uninstall_selected,justify='right')

    # Pack the listbox and button into the window
    lb.pack()
    btn_uninstall.pack()

    # Start the Tkinter event loop
    root.mainloop()
