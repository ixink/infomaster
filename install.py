import subprocess


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



def run_apt_up():
    try:
        subprocess.run(["pip3", "install", "requests"], check=True)
        subprocess.run(["pip3", "install", "bs4"], check=True)
        subprocess.run(["pip3", "install", "re"], check=True)
        subprocess.run(["sudo", "apt", "update"], check=True)
        print("Installed!")
    except subprocess.CalledProcessError:
        print("Error!")

if __name__ == "__main__":
    run_apt_up()
