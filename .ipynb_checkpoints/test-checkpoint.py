# general
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



# only malicious
def generate_random_data(num_rows):
    fake = Faker()
    data = []

    for _ in range(num_rows):
        ip_address = fake.ipv4()
        geolocation = random.choice(["Russia", "North Korea","United States", "Canada", "Mexico", "Brazil", "Argentina", "United Kingdom", "France", "Germany", "Italy", "Spain", "Australia", "New Zealand", "South Africa", "Nigeria", "Egypt", "Kenya", "Russia", "Norway", "Sweden", "Finland"])
        user_agent = random.choice(["Cobalt Strike", "Metasploit", "Blackhole", "Zeus"])
        session_duration = random.uniform(0, 5)  # Random session duration between 1 and 3600 seconds
        data_transfer_volume = random.uniform(200, 2000)  # Random data transfer volume between 0 and 1000 MB
        packet_sizes = random.uniform(1800, 2000)  # Random packet size between 100 and 2000 bytes
        timestamp = fake.date_time_this_decade()
        error_code = random.choice([400,401,404, 403, 500])  # Random HTTP error code
        protocol = random.choice(["SSH", "Telnet", "FTP", "ICMP", "UDP","IMAP","POP3","SMTP"])  # Random protocol
        is_proxy = 1  # Randomly indicate whether it's a proxy (1) or not (0)

        label = check_malicious(ip_address, geolocation, user_agent, session_duration, data_transfer_volume, packet_sizes, timestamp, error_code, protocol, is_proxy)
        
        data.append([ip_address, geolocation, user_agent, session_duration, data_transfer_volume, packet_sizes, timestamp, error_code, protocol, is_proxy, label])

    return data


# only bengin
def generate_random_data(num_rows):
    fake = Faker()
    data = []

    for _ in range(num_rows):
        ip_address = fake.ipv4()
        geolocation = random.choice(["China", "India", "Japan", "South Korea", "Indonesia", "Pakistan", "Bangladesh", "Philippines", "Vietnam", "Iran", "Turkey", "Thailand", "Myanmar", "Iraq", "Afghanistan", "Saudi Arabia", "Uzbekistan", "Malaysia", "Yemen", "Nepal"])
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
        session_duration = random.uniform(6, 3600)  # Random session duration between 1 and 3600 seconds
        data_transfer_volume = random.uniform(0, 199)  # Random data transfer volume between 0 and 1000 MB
        packet_sizes = random.uniform(100, 1800)  # Random packet size between 100 and 2000 bytes
        timestamp = fake.date_time_this_decade()
        error_code = random.choice([200,301,302, 503])  # Random HTTP error code
        protocol = random.choice(["HTTP","HTTPS","TCP"])  # Random protocol
        is_proxy = 0  # Randomly indicate whether it's a proxy (1) or not (0)

        label = check_malicious(ip_address, geolocation, user_agent, session_duration, data_transfer_volume, packet_sizes, timestamp, error_code, protocol, is_proxy)
        
        data.append([ip_address, geolocation, user_agent, session_duration, data_transfer_volume, packet_sizes, timestamp, error_code, protocol, is_proxy, label])

    return data

# Malicious in geolocation
def generate_random_data(num_rows):
    fake = Faker()
    data = []

    for _ in range(num_rows):
        ip_address = fake.ipv4()
        geolocation = random.choice(["Russia", "North Korea","United States", "Canada", "Mexico", "Brazil", "Argentina", "United Kingdom", "France", "Germany", "Italy", "Spain", "Australia", "New Zealand", "South Africa", "Nigeria", "Egypt", "Kenya", "Russia", "Norway", "Sweden", "Finland"])
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
        session_duration = random.uniform(6, 3600)  # Random session duration between 1 and 3600 seconds
        data_transfer_volume = random.uniform(0, 199)  # Random data transfer volume between 0 and 1000 MB
        packet_sizes = random.uniform(100, 1800)  # Random packet size between 100 and 2000 bytes
        timestamp = fake.date_time_this_decade()
        error_code = random.choice([200,301,302, 503])  # Random HTTP error code
        protocol = random.choice(["HTTP","HTTPS","TCP"])  # Random protocol
        is_proxy = 0  # Randomly indicate whether it's a proxy (1) or not (0)

        label = check_malicious(ip_address, geolocation, user_agent, session_duration, data_transfer_volume, packet_sizes, timestamp, error_code, protocol)
        
        data.append([ip_address, geolocation, user_agent, session_duration, data_transfer_volume, packet_sizes, timestamp, error_code, protocol, label])

    return data