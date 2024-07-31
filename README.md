
# Axcient x360Recover Client Dashboard

This project provides a simple Python application to fetch and display a list of clients and their devices from the Axcient x360Recover API. It includes a CLI-based script (`list_clients.py`) and a more advanced Tkinter-based GUI dashboard (`client_dashboard.py`).

## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
  - [CLI Application](#cli-application)
  - [GUI Dashboard](#gui-dashboard)
- [License](#license)

## Requirements

- Python 3.x
- `requests` library
- `python-dotenv` library
- `tkinter` library (comes with standard Python installations)

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/axcient-x360recover-client-dashboard.git
   cd axcient-x360recover-client-dashboard
   ```

2. **Create a Virtual Environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the Required Packages:**

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. **Environment Variables:**

   Create a `.env` file in the project directory and add your API key:

   ```env
   API_KEY=your_actual_api_key_here
   ```

   Replace `your_actual_api_key_here` with your actual API key.

## Usage

### CLI Application

The CLI application (`list_clients.py`) fetches and displays a list of clients from the Axcient x360Recover API.

**Running the CLI Application:**

```bash
python list_clients.py
```

This script will print the list of clients and their IDs to the console.

### GUI Dashboard

The GUI dashboard (`client_dashboard.py`) provides an interactive interface for viewing clients and their associated devices.

**Running the GUI Dashboard:**

```bash
python client_dashboard.py
```

This will open a window displaying a list of clients. Clicking on a client will fetch and display the devices associated with that client.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
