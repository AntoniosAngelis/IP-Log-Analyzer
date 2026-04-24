
import re

with open("log.txt", "r") as file:
    logs = file.readlines()

ip_counter = {}
failed_login_ips = {}

for log in logs:
    match = re.search(r"\d+\.\d+\.\d+\.\d+", log)

    if match:
        ip = match.group()

        ip_counter[ip] = ip_counter.get(ip, 0) + 1


        if "Failed login" in log:
            failed_login_ips[ip] = failed_login_ips.get(ip, 0) + 1

print("\n=== IP Activity ===")
for ip, count in ip_counter.items():
    print(f"{ip} -> {count} events")

print("\n=== Suspicious IPs ===")
found = False

for ip, count in failed_login_ips.items():
    if count >= 3:
        print(f" {ip} -> {count} failed login attempts")
        found = True

if not found:
    print("No suspicious activity detected.")
