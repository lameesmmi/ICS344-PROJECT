# 🔐 Phase 1: SSH Brute-Force Attack on Metasploitable3

## 🖥️ VM Network Configuration

| Machine         | OS              | Role     | IP Address        |
|-----------------|------------------|----------|-------------------|
| Kali Linux      | Kali Rolling     | Attacker | `192.168.56.104`  |
| Metasploitable3 | Windows/Linux    | Victim   | `192.168.56.103`  |

> Both machines are configured to communicate within the same **Host-Only Adapter** network.

---

## ⚙️ Step 1: Configured Static IPs

![Kali IP](https://github.com/lameesmmi/ICS344-PROJECT/blob/main/phase-1/Screenshots/kali%20ip%20and%20ping.png?raw=true)
*Static IP and ping from Kali Linux*

![Metasploitable IP](https://github.com/lameesmmi/ICS344-PROJECT/blob/main/phase-1/Screenshots/metasploitable%20ip.png?raw=true)
*Static IP from Metasploitable3*

---

## 📡 Step 2: Verified Connectivity Using `ping` and `nmap`

**Metasploitable pinging Kali:**

![Metasploitable Pinging Kali](https://github.com/lameesmmi/ICS344-PROJECT/blob/main/phase-1/Screenshots/metasploitable%20pinging%20kali.png?raw=true)

**Kali pinging Metasploitable:**

![Kali Pinging Metasploitable](https://github.com/lameesmmi/ICS344-PROJECT/blob/main/phase-1/Screenshots/kali%20ip%20and%20ping.png?raw=true)

---

## 🛠️ Step 3: Brute-Forcing SSH with Metasploit

Used the `ssh_login` module from Metasploit to perform a brute-force attack on the SSH service.

![Metasploit SSH Attack](https://github.com/lameesmmi/ICS344-PROJECT/blob/main/phase-1/Screenshots/metasploit%20tool%20ssh%20attack%20.png?raw=true)

---

## ✏️ Step 4: Custom Password List

Created and used a custom password list (`passwords.txt`) for the brute-force attack.

![Custom Script File](https://github.com/lameesmmi/ICS344-PROJECT/blob/main/phase-1/Screenshots/custom%20script%20file%20content.png?raw=true)

---

## 💣 Step 5: Executed Custom Brute-Force Script

Ran a Python-based custom brute-force script targeting SSH login.

![Custom Script Attack](https://github.com/lameesmmi/ICS344-PROJECT/blob/main/phase-1/Screenshots/custom_script%20attack.png?raw=true)

---

## ✅ Step 6: Successful Compromise

Successfully gained shell access after finding the correct credentials.

![Successful Login](https://github.com/lameesmmi/ICS344-PROJECT/blob/main/phase-1/Screenshots/successful%20login.png?raw=true)

---

## 📁 Files Included

| File Name           | Description                                |
|---------------------|--------------------------------------------|
| `ssh_bruteforce.sh` | Custom brute-force script (Python/bash)    |
| `passwords.txt`     | Wordlist used for testing                  |

---

## 📎 Notes

- 🔑 **Target username:** `vagrant`  
- 📄 **Wordlist used:** `passwords.txt`  
- ✅ The service is considered **compromised** if login is successful and shell access is obtained.
