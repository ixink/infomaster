import platform
import subprocess
import requests
from bs4 import BeautifulSoup
import re

print('''
     ___        __       __  __           _            
    |_ _|_ __  / _| ___ |  \/  | __ _ ___| |_ ___ _ __ 
     | || '_ \| |_ / _ \| |\/| |/ _` / __| __/ _ \ '__|
     | || | | |  _| (_) | |  | | (_| \__ \ ||  __/ |   
    |___|_| |_|_|  \___/|_|  |_|\__,_|___/\__\___|_|
            ______________________________________________
                              coded by:ixink(Rayhan Ahmed)
                                  tutorial :t.me/ixiinkhat
               contact me:linkedin.com/in/rayhan-ahmed-uiu
                                                   
''')

print("What would you like to start?")
option =("1. Get Device Info\n2. Check Vulnerablity of Website\n3. Change IP\n")
message = input(option)

if message == "1":
    system=platform.system()
    node=platform.node()
    release=platform.release()
    version=platform.version()
    processor=platform.processor()

    # Print system info
    print("System: ", system)
    print("Node: ", node)
    print("Release: ", release)
    print("Version: ", version)
    print("Processor: ", processor)

    # Run lscpu command and capture output
    lscpu_output=subprocess.check_output(["lscpu"]).decode("utf-8")

    #print lscpu output
    print("\nlscpu Output:")
    print(lscpu_output)

    #Additional info
    print("Machine: ", platform.machine())
    print("Architecture: ",  platform.architecture())
    print("Python Version: ", platform.python_version())
elif message == "2":

    def find_vulnerabilities(url):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            page_content = soup.text.lower()

            # Check for SQL injection
            if re.search(r"select|insert|update|delete", page_content):
                print("Potential SQL injection vulnerability found")

            # Check for cross-site scripting (XSS)
            if re.search(r"<script>", page_content):
                print("Potential XSS vulnerability found")

            # Check for cross-site request forgery (CSRF)
            if re.search(r"token|nonce", page_content):
                print("Potential CSRF vulnerability found")

            # Check for file inclusion vulnerability
            if re.search(r"include|require", page_content):
                print("Potential file inclusion vulnerability found")

            # Check for directory traversal
            if re.search(r"\.\./\.\./\.\./", page_content):
                print("Potential directory traversal vulnerability found")

            # Check for insecure direct object references
            if re.search(r"\$\{.*\}", page_content):
                print("Potential insecure direct object reference vulnerability found")

            # Perform a directory brute force attack
            for i in range(1000):
                directory_path = f"/{i}"
                response = requests.get(f"{url}{directory_path}")
                if response.status_code == 200:
                    print(f"Potential directory found: {directory_path}")

            # Perform a file inclusion vulnerability scan
            for ext in [".php", ".html", ".txt"]:
                for i in range(1000):
                    file_path = f"/{i}{ext}"
                    response = requests.get(f"{url}{file_path}")
                    if response.status_code == 200:
                        print(f"Potential file found: {file_path}")

        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

    if __name__ == "__main__":
        url = input("Enter the URL of the website to scan: ")
        find_vulnerabilities(url)
        
                
elif message == "3":
    
    def run_apt_up():
        try:
            subprocess.run(["sudo", "bash", "ipcng.sh"], check=True)
        except subprocess.CalledProcessError:
            print("Error!")

    if __name__ =="__main__":
        run_apt_up()
else:
  print("Error Input")
