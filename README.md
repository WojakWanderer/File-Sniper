
![Logo](https://i.imgur.com/v5TOEnl.jpeg)



File Sniper is a desktop application designed to identify and remove duplicate files in a specified directory. The application leverages file hashing to detect duplicates and offers a user-friendly interface for managing files.


## Features

- **Choose a Folder**: Select the directory you want to scan for duplicate files.
- **Remove Duplicates**: Scan the selected directory for duplicate files based on file hashes and remove them.
- **Output Log**: View the log of actions performed, including which files were deleted and messages for empty directories or no duplicates.
## Requirements

- Python 3.x
- `customtkinter` library

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/WojakWanderer/file-sniper.git
    cd file-sniper
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment**:
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

4. **Install the required libraries**:
    ```bash
    pip install customtkinter
    ```

## Usage

1. **Run the application**:
    ```bash
    python main.py
    ```

2. **Use the application**:
    - **Choose a folder**: Click the "Choose a folder" button to select the directory you want to scan.
    - **Remove duplicates**: Click the "Remove duplicates" button to start scanning and deleting duplicate files.
    - **View output**: Check the output text box for a log of actions performed.
## Contributing

Contributions are welcome! Please fork the repository, make your changes, and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

