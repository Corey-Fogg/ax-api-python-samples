import requests
from dotenv import load_dotenv
import os
import json

# Load environment variables from .env file
load_dotenv()

# Define the API endpoint and headers
API_BASE_URL = "https://axapi.axcient.com/x360recover/client"
API_KEY = os.getenv("API_KEY")  # Get the API key from the environment variable

if not API_KEY:
    print("API_KEY is not set in the environment. Please check your .env file.")
    exit(1)

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
        print(f"Failed to fetch clients. Status code: {response.status_code}")
        return []

def display_clients(clients):
    """Display the list of clients."""
    for client in clients:
        print(f"ID: {client['id']}, Name: {client['name']}")

if __name__ == "__main__":
    # Fetch and display clients
    clients = fetch_clients()
    if clients:
        display_clients(clients)
