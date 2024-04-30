import csv
import os
import random

def generate_random_data(num_rows):
    data = []

    for _ in range(num_rows):
        geolocation = random.choice(['China', 'India', 'Indonesia', 'Pakistan', 'Bangladesh', 'Japan', 'Philippines', 'Vietnam', 'Turkey', 'Iran'])
        user_agent = random.choice([
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/99.0.1150.37 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
])
        session_duration = random.randint(6, 3600)  # Random session duration between 1 and 3600 seconds
        data_transfer_volume = random.randint(0, 199)  # Random data transfer volume between 0 and 1000 MB
        packet_sizes = random.randint(100, 1800)  # Random packet size between 100 and 2000 bytes
        error_code = random.choice([200,301,302, 503])  # Random HTTP error code
        protocol = random.choice(["SSH","HTTPS","TCP"])  # Random protocol
        is_proxy = 0  # Randomly indicate whether it's a proxy (1) or not (0)

        label = check_malicious(geolocation, user_agent, session_duration, data_transfer_volume, packet_sizes, error_code, protocol, is_proxy)
        
        data.append([geolocation, user_agent, session_duration, data_transfer_volume, packet_sizes, error_code, protocol, is_proxy, label])

    return data

def check_malicious(geolocation, user_agent, session_duration, data_transfer_volume, packet_sizes, error_code, protocol, is_proxy):
    # Check for malicious geolocations
    malicious_geolocations = ['Russia', 'Germany', 'United Kingdom', 'France', 'Italy', 'Spain', 'Ukraine', 'Poland', 'Romania', 'Netherlands']
    if geolocation in malicious_geolocations:
        return 1  # Malicious

    # Check for specific user agents associated with malicious activity
    malicious_user_agents = ["Cobalt Strike", "Metasploit", "Blackhole", "Zeus"]
    for agent in malicious_user_agents:
        if agent.lower() in user_agent.lower():
            return 1  # Malicious

    # Check for unusual session duration, data transfer volume, or packet sizes
    if session_duration < 5 or data_transfer_volume > 200 or packet_sizes > 1800:
        return 1  # Malicious

    # Check for specific error codes or protocols associated with malicious activity
    malicious_error_codes = [400,401,404, 403, 500]
    malicious_protocols = ["HTTP", "Telnet", "ICMP", "UDP","IMAP","POP3","SMTP"]
    if error_code in malicious_error_codes or protocol in malicious_protocols:
        return 1  # Malicious
    # check it it from proxy servers
    if is_proxy == 1:
        return 1

    # All other cases considered benign
    return 0  # Benign


def write_to_csv(data, filename):
    file_exists = os.path.isfile(filename)
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Geolocation", "User Agent", "Session Duration", "Data Transfer Volume", "Packet Size", "Status Code", "Protocol", "Proxy Detected", "Label"])
        writer.writerows(data)

# Generate 25000 rows of random data
num_rows = 1000
random_data = generate_random_data(num_rows)

# Write the data to a CSV file
filename = "modified_dataset.csv"
write_to_csv(random_data, filename)

print("CSV file generated successfully!")
