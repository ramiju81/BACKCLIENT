import requests
import time
from requests.exceptions import ConnectionError
import json

BASE_URL = "http://192.168.230.114:8000"

def print_response(response):
    print("\n=== API Response ===")
    print(f"Status Code: {response.status_code}")
    print("Response Body:")
    try:
        print(json.dumps(response.json(), indent=2))
    except:    
        print(response.text)
    print("=======================\n")

def wait_for_api():
    max_retries = 5
    retry_count = 0

    while retry_count < max_retries:
        try:
            response = requests.get(f"{BASE_URL}/", timeout=60)
            if response.status_code == 200:
                print("API is up and running!")
                print_response(response)
                return True
            else:
                print(f"API returned status code: {response.status_code}")
        except ConnectionError:
            print("Connection failed, retrying...")

        print(f"Retrying in {2 ** retry_count} seconds...")
        if retry_count >= max_retries:
            print("Max retries reached. Exiting.")
            return False
        retry_count += 1
        time.sleep(2 ** retry_count)

def main ():
    wait_for_api()

if __name__ == "__main__":
    main()
    