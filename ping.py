import subprocess

def ping(host):
    try: 
        output = subprocess.run(["ping", "-n", "1", host], capture_output=True, text=True)

        if "TTL=" in output.stdout:
            print(f"{host} is reachable")
        else:
            print(f"{host} is not reachable")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    host = input("Enter a host ( IP or domain):")
    ping(host)

