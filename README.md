# Password Manager

A secure desktop application for managing your passwords, built with Python and Tkinter.

## Features

* **Secure Password Storage:** Utilizes AES encryption to store your passwords securely in a local database.
* **Environment Variable Key Protection:** The encryption key is protected by retrieval from environment variables, adding an extra layer of security.
* **Add New Passwords:** Easily add new website/application credentials to the database.
* **View Passwords:** Securely retrieve and view your stored passwords.
* **Update Passwords:** Modify existing password entries as needed.
* **Delete Passwords:** Remove unwanted password entries from the database.
* **User-Friendly GUI:** A modern and intuitive graphical interface built with Tkinter.
* **Standalone Application:** Packaged for easy distribution and use without requiring Python installation.

## Technologies Used

* **Python:** The primary programming language.
* **Tkinter:** For creating the graphical user interface.
* **PyCryptodome (or similar):** For AES encryption.
* **Potentially PyInstaller/cx_Freeze:** For packaging the application into a standalone executable.
* **Environment Variables:** For securely managing the encryption key.

## Security Considerations

* **AES Encryption:** Passwords are encrypted using the Advanced Encryption Standard (AES), a robust symmetric encryption algorithm.
* **Key Management:** The AES encryption key is intended to be stored and retrieved from environment variables. **It is crucial to set strong and unique environment variables and protect your system accordingly.**
* **Local Storage:** The password database is stored locally on your machine. Ensure your system is protected from unauthorized access.
* **No Cloud Sync:** This application does not offer cloud synchronization, meaning your password database is only accessible on the machine where it is stored.

**Disclaimer:** While this application aims to provide secure password management, security is a complex field. Use this software at your own discretion and understand the inherent risks of storing sensitive data locally. It is recommended to use strong system passwords and keep your operating system up to date.

## Getting Started

### Prerequisites

* No Python installation is required if using the standalone application.
* If running from source, you will need Python 3.x installed on your system and potentially the `pycryptodome` library (`pip install pycryptodome`).

### Installation

1.  **Standalone Application (Recommended):** Download the pre-built executable for your operating system (if available in the releases).
2.  **Running from Source:**
    * Clone the repository: `git clone [repository URL]`
    * Navigate to the project directory: `cd password-manager`
    * Install dependencies (if any): `pip install -r requirements.txt`

### Usage

1.  **Set Environment Variable:** Before running the application for the first time (or any time you need to access the database), ensure you have set the environment variable that the application uses for the encryption key. **Refer to the application's specific instructions or configuration on how to name and set this environment variable.**
2.  **Run the Application:**
    * **Standalone:** Execute the downloaded executable file.
    * **Source:** Run the main Python script: `python main.py` (replace `main.py` with the actual script name).
3.  Follow the on-screen instructions provided by the graphical interface to add, view, update, and delete your passwords.

## Contributing

Contributions to this project are welcome. Please feel free to submit bug reports, feature requests, or pull requests.

## License

[Specify the license under which this project is distributed (e.g., MIT License, GPLv3, etc.)]

## Acknowledgements

* [Optional: Mention any libraries or resources that were particularly helpful.]
