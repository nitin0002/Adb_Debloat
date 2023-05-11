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
        selected_indices = map(int, lb.curselection())
        selected_packages = [packages[idx] for idx in selected_indices]
        for package in selected_packages:
            subprocess.run(['adb','shell', 'pm', 'uninstall','--user','0', package])


    # Create a Tkinter window and listbox to display packages with checkboxes
    root = tk.Tk()
    root.geometry("800x600")
    lb_frame = tk.Frame(root)
    lb_scroll = tk.Scrollbar(lb_frame, orient=tk.VERTICAL)
    lb_scroll.pack(side=tk.RIGHT, fill=tk.Y)
    lb = tk.Listbox(lb_frame, width=90, height=28, font=('courier', 12), yscrollcommand=lb_scroll.set, selectmode="multiple")
    for package in packages:
        lb.insert(tk.END, package)
    lb.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    lb_scroll.config(command=lb.yview)
    lb_frame.pack(fill=tk.BOTH, expand=True)

    # Add a button to uninstall selected packages
    btn_uninstall = tk.Button(root, text="Uninstall Selected", command=uninstall_selected)

    # Pack the listbox and button into the window
    lb.pack()
    btn_uninstall.pack()

    # Start the Tkinter event loop
    root.mainloop()



