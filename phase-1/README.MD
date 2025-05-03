# 🔐 PHASE 1

## 🖥️ VM Network Configuration

| Machine        | OS             | Role        | IP Address        |
|----------------|----------------|-------------|-------------------|
| Kali Linux     | Kali Rolling   | Attacker    | `192.168.56.104`  |
| Metasploitable3| Windows/Linux  | Victim      | `192.168.56.103`  |

Both machines are configured to communicate within the same **Host-Only Adapter** network.

##IP Addresses 
![Kali IP](https://github.com/lameesmmi/ICS344-PROJECT/blob/main/phase-1/Screenshots/kali%20ip%20and%20ping.png?raw=true)

![Metasploitable IP](https://github.com/lameesmmi/ICS344-PROJECT/blob/main/phase-1/Screenshots/metasploitable%20ip.png?raw=true)

## Reachability Through Ping:
![Metasploitable Pingig Kali](https://github.com/lameesmmi/ICS344-PROJECT/blob/main/phase-1/Screenshots/metasploitable%20pinging%20kali.png?raw=true)

![Kali Pinging Metasploitable](https://github.com/lameesmmi/ICS344-PROJECT/blob/main/phase-1/Screenshots/kali%20ip%20and%20ping.png?raw=true)



---

## 📡 Objective

- Verify **network reachability** between the two VMs.
- Perform an **SSH brute-force attack** on the victim machine using:
  - Metasploit tool
  - Custom script
---

## ✅ Steps Completed

- [x] Configured static IPs for both VMs
- [x] Verified connectivity using `ping` and `nmap`
- [x] Targeted SSH service running on `192.168.56.103`
- [x] Used Metasploit’s `ssh_login` module for brute-force
- [x] Created and used a custom password list

---

## 📂 Files Included

| File Name            | Description                                     |
|----------------------|-------------------------------------------------|
| `ssh_bruteforce.sh`  | Custom Python brute-force script                |
| `passwords.txt`         | Sample short wordlist used for testing          |


---

## 📎 Notes

- SSH target username: `vagrant`
- Wordlist used: `passwords.txt'
- Service considered **compromised** if login is successful and shell access is achieved.
