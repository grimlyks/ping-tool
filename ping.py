import subprocess
import csv

def ping(host):
    try: 
        output = subprocess.run(["ping", "-n", "1", host], capture_output=True, text=True)

        if "TTL=" in output.stdout:
            return "Reachable"
        else:
            return "Not Reachable"
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    hosts = input("Enter hosts ( IP or domain):").split(",")
    hosts = [h.strip() for h in hosts if h.strip()]

    results = []

    for host in hosts:
        status = ping(host)
        print(f"{host} -> {status}")
        results.append([host, status])

    with open("ping_results.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Host", "Status"])
        writer.writerows(results)
    
    print("\nResults saved to ping_results.csv")

