import tkinter as tk
from tkinter import ttk

class GroupApplication:
    # Constants
    MIN_GROUP_MEMBERS = 5
    MAX_GROUP_MEMBERS = 10

    

    def __init__(self, root):
        self.root = root
        self.root.title("Sunshine Adventure Camp Program")
        self.group_data = []


        # Group Name
        self.group_name_label = tk.Label(root, text="Group Leader:")
        self.group_name_label.grid(row=0, column=0, padx=5, pady=5)
        self.group_name = tk.StringVar()
        self.group_name_entry = tk.Entry(root, textvariable=self.group_name)
        self.group_name_entry.grid(row=0, column=1, padx=5, pady=5)


        self.can_move_label = tk.Label(root, text="Staying in location?")
        self.can_move_label.grid(row=1, column=0, padx=5, pady=5)
        self.can_move = tk.StringVar(value="Yes")
        self.can_move_menu = tk.OptionMenu(root, self.can_move, "Yes", "No")
        self.can_move_menu.grid(row=1, column=1, padx=5, pady=5)

        # Location
        self.location_label = tk.Label(root, text="Location:")
        self.location_label.grid(row=2, column=0, padx=5, pady=5)
        self.location = tk.StringVar()
        self.location_entry = tk.Entry(root, textvariable=self.location)
        self.location_entry.grid(row=2, column=1, padx=5, pady=5)

        # Weather
        self.weather_label = tk.Label(root, text="Weather:")
        self.weather_label.grid(row=3, column=0, padx=5, pady=5)
        self.weather = tk.StringVar(value="Sunny")
        self.weather_menu = tk.OptionMenu(root, self.weather, "Sunny", "Rainy", "Snowy", "Humid", "Windy", "Stormy", "Partly Cloudy")
        self.weather_menu.grid(row=3, column=1, padx=5, pady=5)

        # Group Members
        self.group_members_label = tk.Label(root, text="Number of Group Members:")
        self.group_members_label.grid(row=4, column=0, padx=5, pady=5)
        self.group_members = tk.StringVar()
        self.group_members_entry = tk.Entry(root, textvariable=self.group_members)
        self.group_members_entry.grid(row=4, column=1, padx=5, pady=5)

        # Continue Button
        self.continue_button = tk.Button(root, text="Continue", command=self.continue_action)
        self.continue_button.grid(row=5, column=0, padx=5, pady=5)

        # Done Button
        self.done_button = tk.Button(root, text="Done", command=self.done_action)
        self.done_button.grid(row=5, column=1, padx=5, pady=5)

        # Delete Button
        self.delete_button = tk.Button(root, text="Delete", command=self.delete_action)
        self.delete_button.grid(row=5, column=2, padx=5, pady=5)

        # Display Button
        self.display_button = tk.Button(root, text="Display", command=self.display_action)
        self.display_button.grid(row=5, column=3, padx=5, pady=5)

        # Output Box
        self.output_box_label = tk.Label(root, text="Output:")
        self.output_box_label.grid(row=6, column=0, padx=5, pady=5)
        self.output_box = tk.Text(root, height=10, width=50)
        self.output_box.grid(row=7, column=0, columnspan=4, padx=5, pady=5)

    
    # Actions
    def continue_action(self):
        group_name = self.group_name.get()
        can_move = self.can_move.get()
        location = self.location.get()
        weather = self.weather.get()
        group_members = self.group_members.get()

        # Validate Group Members
        if not group_members.isnumeric():
            self.output_box.insert(tk.END, "Number of Group Members must be a number.\n")
            return

        group_members = int(group_members)
        if group_members < self.MIN_GROUP_MEMBERS or group_members > self.MAX_GROUP_MEMBERS:
            self.output_box.insert(tk.END, f"Number of Group Members must be between {self.MIN_GROUP_MEMBERS} and {self.MAX_GROUP_MEMBERS}.\n")
            return

        self.group_data.append({
            "group_name": group_name,
            "can_move": can_move,
            "location": location,
            "weather": weather,
            "group_members": group_members
        })

        self.group_name.set("")
        self.can_move.set("Yes")
        self.location.set("")
        self.weather.set("Sunny")
        self.group_members.set("")

        self.output_box.insert(tk.END, "Group added successfully.\n")

    def done_action(self):
        self.output_box.insert(tk.END, f"Total groups added: {len(self.group_data)}\n")
        self.group_data = []

    def delete_action(self):
        self.output_box.delete('1.0', tk.END)

    def display_action(self):
        self.output_box.delete('1.0', tk.END)

        for group in self.group_data:
            self.output_box.insert(tk.END, f"Group Name: {group['group_name']}\n")
            self.output_box.insert(tk.END, f"Can Group Move?: {group['can_move']}\n")
            self.output_box.insert(tk.END, f"Location: {group['location']}\n")
            self.output_box.insert(tk.END, f"Weather Conditions: {group['weather']}\n")
            self.output_box.insert(tk.END, f"Number of Group Members: {group['group_members']}\n\n")

    def done_action(self):
        # Clear the output box
        self.output_box.delete('1.0', tk.END)

        # Create the treeview widget
        treeview = ttk.Treeview(self.root, columns=["group_name", "can_move", "location", "weather", "group_members"])
        treeview.heading("#0", text="Group #")
        treeview.heading("group_name", text="Group Leader")
        treeview.heading("can_move", text="Staying in location?")
        treeview.heading("location", text="Location")
        treeview.heading("weather", text="Weather")
        treeview.heading("group_members", text="Number of Group Members")

        # Add the group data to the treeview
        for i, group in enumerate(self.group_data, 1):
            treeview.insert("", "end", text=str(i), values=(group["group_name"], group["can_move"], group["location"], group["weather"], group["group_members"]))

        # Display the treeview
        treeview.grid(row=7, column=0, columnspan=4, padx=5, pady=5)

        # Clear the group data
        self.group_data = []

root = tk.Tk()
app = GroupApplication(root)
root.mainloop()
