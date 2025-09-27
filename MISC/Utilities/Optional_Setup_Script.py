import os
import sys
import subprocess

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


def check_pip():
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', '--version'])
    except subprocess.CalledProcessError:
        print("pip is not installed. Installing pip...")
        subprocess.check_call([sys.executable, '-m', 'ensurepip', '--default-pip'])


def main():
    try:
        print("Checking pip installation...\n")
        
        check_pip()
        print("pip3 - OK!")

        print("Installing PyYAML...\n")
        
        install("PyYAML")
        print("PyYAML - OK!")

        print("Installing mysql-connector-python...\n")
        
        install("mysql-connector-python")
        print("Python interface for MySQL - OK!")

        print("Installing pandas...\n")
        
        install("pandas")
        print("Pandas - OK!")
        
        print("Installing wfdb...")
        
        install("wfdb")
        print("wfdb - OK!")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred during installation: {e}")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")



if __name__ == "__main__":
    main()
