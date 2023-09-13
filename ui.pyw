import tkinter as tk
import os
import json
import utils as api


# popup = None


def close_window():
    root.destroy()


def update_values():
    location = entry_var1.get()
    frequency = entry_var2.get()
    print(f"Updated values: location:{location}, frequency:{frequency}")
    api.set_options_backuplocation(location)
    api.set_options_backup_frequency(frequency)
    #close_window()

def apply_folders():
    # Get folder values from the text boxes
    folder_values = [folder_entry.get() for folder_entry in folder_entries]

    # Store the folder values in "folders.json"
    with open('./folders.json', 'w') as f:
        json.dump(folder_values, f)
    popup.destroy()

# Function to create and display the configure locations popup
def configure_locations():
    global folder_entries, popup

    # Create a Toplevel window (popup)
    popup = tk.Toplevel(root)
    popup.title("Configure Backup Locations")

    folder_entries = []

    # Load folder values from "folders.json"
    with open('./folders.json', 'r') as f:
        folder_values = json.load(f)

    # Create modifiable text boxes for folder paths and populate them
    for i, folder_value in enumerate(folder_values, start=1):
        label = tk.Label(popup, text=f"Folder {i}:")
        label.grid(row=i - 1, column=0, padx=5, pady=5)

        entry_var = tk.StringVar(value=folder_value)  # Set the initial value
        folder_entries.append(entry_var)
        entry = tk.Entry(popup, textvariable=entry_var, width=30)
        entry.grid(row=i - 1, column=1, padx=5, pady=5)

    # Create an "Apply" button in the popup
    apply_button = tk.Button(popup, text="Apply", command=apply_folders)
    apply_button.grid(row=len(folder_entries), columnspan=2, padx=5, pady=10)


def open_configure_locations_popup():
    configure_locations()



root = tk.Tk()
root.geometry("400x300")  # Set window size to 4 times larger
root.title('Auto-Backup Settings')

# menu = tk.Menu(root)
# root.config(menu=menu)
# configure_menu = tk.Menu(menu)
# menu.add_cascade(label="Configure Locations", menu=configure_menu)
# configure_menu.add_command(label="Edit Backup Folders", command=configure_locations)


options = api.get_options()

entry_var1 = tk.StringVar()
entry_var1.set(options['backup_to'])

entry_var2 = tk.StringVar()
entry_var2.set(options['frequency'])
behavior_pack_uuid_label = tk.Label(root, text="Backup location:")
behavior_pack_uuid_label.pack()

entry1 = tk.Entry(root, textvariable=entry_var1, width=30)  # Enlarge the Entry widget
entry1.pack()


behavior_pack_uuid_label = tk.Label(root, text="Auto Backup Frequency (auto backups only occur when your pc is on):")
behavior_pack_uuid_label.pack()

entry2 = tk.Entry(root, textvariable=entry_var2, width=30)  # Enlarge the Entry widget
entry2.pack()

behavior_pack_uuid_label = tk.Label(root, text="days")
behavior_pack_uuid_label.pack()

behavior_pack_uuid_label = tk.Label(root, text=" ")
behavior_pack_uuid_label.pack()

button = tk.Button(root, text="apply", command=update_values, width=20)  # Enlarge the Button widget
button.pack()

button = tk.Button(root, text="cancel", command=close_window, width=20)  # Enlarge the Button widget
button.pack()

behavior_pack_uuid_label = tk.Label(root, text='For Windows users, make sure you use "\\\\" instead of "\\" or "/" in file paths.')
behavior_pack_uuid_label.pack()

locations_button = tk.Button(root, text="Locations", command=open_configure_locations_popup)
locations_button.pack()

button = tk.Button(root, text="backup now", command=api.backup_all, width=20)  # Enlarge the Button widget
button.pack()

root.mainloop()



