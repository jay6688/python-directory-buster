import requests
import concurrent.futures

# ==========================================
# 1. THE SETUP
# ==========================================
# We will use the same legal practice site from your SQLi tester!
# Make sure the URL ends with a slash (/)
target_url = "http://testphp.vulnweb.com/" 
wordlist_file = "dirs.txt"

print(f"[*] Starting Directory Buster on: {target_url}")
print("-" * 50)

# ==========================================
# 2. THE WORKER INSTRUCTIONS
# ==========================================
def check_directory(directory):
    # Combine the base URL with the guessed word
    # Example: "http://testphp.vulnweb.com/" + "admin" = "http://testphp.vulnweb.com/admin"
    url_to_test = f"{target_url}{directory}"
    
    try:
        # Send an HTTP GET request to the guessed URL
        response = requests.get(url_to_test, timeout=3)
        
        # THE CORE LOGIC:
        # If the server replies with 200 OK, the folder exists!
        if response.status_code == 200:
            print(f"[+] 🚨 BINGO! Found hidden directory: {url_to_test}")
            
        # If the server replies with 404 Not Found, we just ignore it.
        # Notice we don't even write code for 404, we just let it pass silently.
            
    except requests.exceptions.RequestException:
        # If the internet drops or server crashes, just ignore the error
        pass

# ==========================================
# 3. LOAD THE AMMUNITION
# ==========================================
# Open our dirs.txt file and load all the words into a list, stripping out the "Enters"
with open(wordlist_file, "r") as file:
    directories_to_test = [line.strip() for line in file]

print(f"[*] Loaded {len(directories_to_test)} words. Launching multithreaded scan...")
print("-" * 50)

# ==========================================
# 4. THE MULTITHREADING MAGIC
# ==========================================
# We hire 10 workers to fire these GET requests at the exact same time
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    # The Boss hands the list of words to the workers and tells them to run 'check_directory'
    executor.map(check_directory, directories_to_test)

print("-" * 50)
print("[*] Scan Complete!")