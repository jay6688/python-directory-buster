# 🕵️‍♂️ Python Directory Buster (DirBuster)

## 📖 Overview
This is a custom-built, multi-threaded Directory Buster (DirBuster) written in Python. It is designed to perform automated web reconnaissance by systematically guessing hidden directories and files on a target web server. 

By sending rapid HTTP requests and analyzing the server's status codes, this tool maps out the hidden architecture of a website, uncovering unlinked administrative panels, backup folders, and exposed API endpoints that regular users cannot see.

## ✨ Features
* **Lightning Fast Multithreading:** Utilizes Python's `concurrent.futures.ThreadPoolExecutor` to launch concurrent HTTP requests, drastically reducing scan time compared to a linear approach.
* **Customizable Wordlists:** Easily swap out the `dirs.txt` ammunition file to use massive industry-standard wordlists (like SecLists) or targeted custom dictionaries.
* **Clean & Focused Output:** Automatically ignores `404 Not Found` errors and only alerts the user when a valid `200 OK` directory is discovered.
* **Robust Error Handling:** Built-in exception handling ensures the scanner keeps running even if the server drops a connection or times out.

## 🧠 How It Works
The script appends words from a provided text file (`dirs.txt`) to the base URL of a target website and sends an HTTP `GET` request.
* If the server responds with a **404 Not Found**, the script knows the directory does not exist and silently moves on.
* If the server responds with a **200 OK**, the script triggers an alert, meaning a hidden file or folder has been successfully discovered.

## 🛠️ Prerequisites
* Python 3.x installed on your machine
* The Python `requests` library

You can install the required library using pip:
```bash
pip install requests
```

## 🚀 Usage

1. **Prepare your wordlist:** Ensure you have a text file named `dirs.txt` in the same directory as the script. Add the hidden directories you want to guess (one word per line).
2. **Set your target:** Open `dir_buster.py` in a text editor and update the `target_url` variable to point to your authorized target (make sure it ends with a `/`).
3. **Run the tool:**
```bash
python dir_buster.py
```

---

## ⚠️ Legal Disclaimer
> **FOR EDUCATIONAL AND AUTHORIZED TESTING PURPOSES ONLY.**
> 
> Performing directory enumeration on web servers without explicit permission is illegal and violates terms of service. This tool is designed strictly for authorized security auditing, capture-the-flag (CTF) events, and educational environments. The developer assumes no liability and is not responsible for any misuse or damage caused by this program.
