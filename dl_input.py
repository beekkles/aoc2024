import requests
import os
import sys

def d_input(cookie, dia):
    url = f"https://adventofcode.com/2024/day/{dia}/input"
    dia = f"{int(dia):02d}"
    d_folder = os.path.join(".", dia)
    input_path = os.path.join(d_folder,"input.txt")
    headers = {
        "Cookie": f"session={cookie}"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        os.makedirs(d_folder, exist_ok=True)

        with open(input_path, "w") as f:
            f.write(response.text)
            print("hecho!")

    except requests.RequestException as e:
        print("no existe ese día xd")

if __name__ == "__main__":
    cookie = sys.argv[1]
    dia = sys.argv[2]

    d_input(cookie, dia)