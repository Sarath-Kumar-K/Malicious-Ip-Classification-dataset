import csv
import os
import random
from faker import Faker

def generate_random_data(num_rows):
    fake = Faker()
    data = []

    for _ in range(num_rows):
        ip_address = fake.ipv4()
        geolocation = fake.country()
        user_agent = fake.user_agent()
        session_duration = random.uniform(1, 3600)  # Random session duration between 1 and 3600 seconds
        data_transfer_volume = random.uniform(0, 1000)  # Random data transfer volume between 0 and 1000 MB
        packet_sizes = random.uniform(100, 2000)  # Random packet size between 100 and 2000 bytes
        timestamp = fake.date_time_this_decade()
        error_code = random.choice([200,301,302,400,401,403, 404, 500,503])  # Random HTTP error code
        protocol = random.choice(["HTTP", "HTTPS", "SSH", "Telnet", "FTP", "ICMP","TCP", "UDP","IMAP","POP3","SMTP"])  # Random protocol
        is_proxy = random.choice([0, 1])  # Randomly indicate whether it's a proxy (1) or not (0)

        label = check_malicious(ip_address, geolocation, user_agent, session_duration, data_transfer_volume, packet_sizes, timestamp, error_code, protocol,is_proxy)
        
        data.append([ip_address, geolocation, user_agent, session_duration, data_transfer_volume, packet_sizes, timestamp, error_code, protocol, is_proxy, label])

    return data

def check_malicious(ip_address, geolocation, user_agent, session_duration, data_transfer_volume, packet_sizes, timestamp, error_code, protocol, is_proxy):
    # Check for malicious geolocations
    malicious_geolocations = ["Russia", "North Korea","United States", "Canada", "Mexico", "Brazil", "Argentina", "United Kingdom", "France", "Germany", "Italy", "Spain", "Australia", "New Zealand", "South Africa", "Nigeria", "Egypt", "Kenya", "Norway", "Sweden", "Finland"]
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
    malicious_protocols = ["SSH", "Telnet", "FTP", "ICMP", "UDP","IMAP","POP3","SMTP"]
    if error_code in malicious_error_codes or protocol in malicious_protocols:
        return 1  # Malicious
    # check it it from proxy servers
    if is_proxy == 1:
        return 1

    # All other cases considered benign
    return 0  # Benign

# # Example usage:
# ip_address = "192.168.1.100"
# geolocation = "Russia"
# user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
# session_duration = 5
# data_transfer_volume = 200
# packet_sizes = 1800
# timestamp = "2022-06-15 03:27:00"
# error_code = 404
# protocol = "HTTP"

# label = check_malicious(ip_address, geolocation, user_agent, session_duration, data_transfer_volume, packet_sizes, timestamp, error_code, protocol)
# print("Label:", label)  # Output: Label: 1 (Malicious)


def write_to_csv(data, filename):
    file_exists = os.path.isfile(filename)
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["IP Address", "Geolocation", "User Agent", "Session Duration", "Data Transfer Volume", "Packet Sizes", "Timestamp", "Error Code", "Protocol", "Is_Proxy", "Label"])
        writer.writerows(data)

# Generate 25000 rows of random data
num_rows = 800
random_data = generate_random_data(num_rows)

# Write the data to a CSV file
filename = "malicious_benign_dataset.csv"
write_to_csv(random_data, filename)

print("CSV file generated successfully!")
