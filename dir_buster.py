# ==========================================
# IMPORTANT: PREREQUISITES
# Before running this script, you must install the external 'requests' library.
# Run this command in your terminal: pip install requests
# ==========================================

import requests
import concurrent.futures

# ==========================================
# 1. THE SETUP (TARGET & AMMUNITION)
# ==========================================
# The website we are scanning. 
# IMPORTANT: It must end with a forward slash (/) so the words attach correctly!
target_url = "http://testphp.vulnweb.com/" 

# The text file containing our list of common hidden folder names (e.g., admin, backup, api)
wordlist_file = "dirs.txt"

print(f"[*] Starting Directory Buster on: {target_url}")
print("-" * 50)

# ==========================================
# 2. THE WORKER INSTRUCTIONS (THE ENGINE)
# ==========================================
def check_directory(directory):
    """
    This function is our 'worker'. It takes a single word (like 'admin'), 
    attaches it to the URL, and asks the server if the page exists.
    """
    # Glue the base URL and the guessed word together
    # Example: "http://testphp.vulnweb.com/" + "admin" = "http://testphp.vulnweb.com/admin"
    url_to_test = f"{target_url}{directory}"
    
    try:
        # Send an HTTP GET request (asking the server to fetch the page)
        # timeout=3 ensures we don't get stuck forever if the server is slow
        response = requests.get(url_to_test, timeout=3)
        
        # --- THE CORE HACKER LOGIC ---
        # HTTP Status 200 OK: The server successfully found and loaded the page.
        # This means our guess was right, and we found a hidden room!
        if response.status_code == 200:
            print(f"[+] 🚨 BINGO! Found hidden directory: {url_to_test}")
            
        # If the status code is 404 (Not Found) or 403 (Forbidden), we just do nothing.
        # By not writing an 'else' statement, the script silently ignores wrong guesses.
            
    except requests.exceptions.RequestException:
        # Safety Net: If the internet drops or the target server crashes,
        # this prevents our Python script from crashing. It just skips the error.
        pass

# ==========================================
# 3. LOAD THE AMMUNITION (PREPARING THE LIST)
# ==========================================
# Open our dirs.txt file in "read" mode
with open(wordlist_file, "r") as file:
    # Read every line in the text file. 
    # .strip() is crucial: it removes the invisible "Enter" (\n) character at the end of each word.
    directories_to_test = [line.strip() for line in file]

print(f"[*] Loaded {len(directories_to_test)} words. Launching multithreaded scan...")
print("-" * 50)

# ==========================================
# 4. THE MULTITHREADING MAGIC (SPEED BOOST)
# ==========================================
# Instead of guessing 1 word at a time, we hire 10 'workers' (threads) to guess at the exact same time.
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    # executor.map takes our worker function (check_directory) and our list of words (directories_to_test).
    # It automatically hands out words to available workers until the list is completely empty.
    executor.map(check_directory, directories_to_test)

print("-" * 50)
print("[*] Scan Complete!")
