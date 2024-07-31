import tkinter as tk
from tkinter import ttk, messagebox
import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Define the API endpoint
API_BASE_URL = "https://axapi.axcient.com/x360recover/client"
API_KEY = os.getenv("API_KEY")  # Get the API key from the environment variable

headers = {
    "x-api-key": API_KEY,
    "Content-Type": "application/json"
}

def fetch_clients():
    """Fetch the list of clients from the API."""
    response = requests.get(API_BASE_URL, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        messagebox.showerror("Error", f"Failed to fetch clients. Status code: {response.status_code}")
        return []

def fetch_devices(client_id):
    """Fetch the devices for a given client ID."""
    response = requests.get(f"{API_BASE_URL}/{client_id}/device", headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        messagebox.showerror("Error", f"Failed to fetch devices. Status code: {response.status_code}")
        return []

def on_client_select(event):
    """Handle the selection of a client."""
    selected_item = event.widget.selection()
    if selected_item:
        client_id = client_tree.item(selected_item, "text")
        devices = fetch_devices(client_id)
        display_devices(devices)

def display_devices(devices):
    """Display the list of devices for the selected client."""
    device_list.delete(0, tk.END)
    for device in devices:
        device_info = f"ID: {device['id']}, Name: {device.get('name', 'N/A')}, Type: {device.get('type', 'N/A')}"
        device_list.insert(tk.END, device_info)

# Create the main application window
root = tk.Tk()
root.title("Client Dashboard")

# Create a frame for the client list
client_frame = ttk.LabelFrame(root, text="Clients")
client_frame.pack(fill="both", expand=True, padx=10, pady=10)

# Create a treeview for displaying clients
client_tree = ttk.Treeview(client_frame, columns=("Name", "Health Status"), show='headings')
client_tree.heading("Name", text="Name")
client_tree.heading("Health Status", text="Health Status")
client_tree.pack(fill="both", expand=True)

# Create a frame for the device list
device_frame = ttk.LabelFrame(root, text="Devices")
device_frame.pack(fill="both", expand=True, padx=10, pady=10)

# Create a listbox for displaying devices
device_list = tk.Listbox(device_frame)
device_list.pack(fill="both", expand=True)

# Fetch and display clients
clients = fetch_clients()
for client in clients:
    client_tree.insert("", "end", text=client["id"], values=(client["name"], client["health_status"]))

# Bind the select event to the client tree
client_tree.bind("<<TreeviewSelect>>", on_client_select)

# Start the Tkinter event loop
root.mainloop()
