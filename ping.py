import subprocess
import csv
from datetime import datetime
import logging

logging.basicConfig(
    filename="ping_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def ping(host):
    try: 
        output = subprocess.run(
            ["ping", "-n", "1", host], 
            capture_output=True, 
            text=True
        )

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
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{timestamp} | {host} -> {status}")
        
        #add to results for csv
        results.append([timestamp, host, status])

        #log the results
        logging.info(f"{host} -> {status}")

    with open("ping_results.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Timestamp","Host", "Status"])
        writer.writerows(results)
    
    print("\nResults saved to ping_results.csv and ping_log.txt")

