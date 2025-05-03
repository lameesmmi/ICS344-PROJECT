# 🛡️ Phase 3 – SSH Brute-Force Defense with Fail2Ban

##  Defense Mechanism
We implemented Fail2Ban on the Metasploitable3 to protect against SSH brute-force attacks. The goal was to validate an effective defense mechanism on the Metasploitable3 victim machine. Fail2Ban was chosen for its ability to monitor failed login attempts and automatically block attacker IPs after a defined number of failures. The defense was tested using Hydra from the attacker machine to simulate a real brute-force scenario.

---

##  Testing & Validation
We performed a brute-force SSH attack with Hydra on the attacker machine, using incorrect credentials from a password list. As intended, the attack triggered Fail2Ban after multiple failed login attempts. The attacker's IP address (192.168.183.7) was automatically blocked. Fail2Ban successfully mitigated SSH brute-force attacks by detecting failed login patterns and banning the attacker. This demonstrates an effective defense mechanism against automated intrusion attempts.

---

## 🔢 Steps Taken

1. **Simulating an SSH Brute-Force Attack**  
   We began Phase 3 by simulating a brute-force SSH attack from the attacker machine (Kali Linux). A password list containing weak and common credentials was created, and Hydra was used to automate the attack against the Metasploitable3 victim machine.
![attacer](https://github.com/lameesmmi/ICS344-PROJECT/blob/main/phase-3/Screenshots/Attacker%20IP.png)


![victim](https://github.com/lameesmmi/ICS344-PROJECT/blob/main/phase-3/Screenshots/Victim%20IP.png)
2. **Confirming Vulnerability**  
   The attack was initially successful in sending multiple failed SSH login attempts to the victim machine. At this point, no defense was in place, and the system was exposed to brute-force intrusion.

![attack](https://github.com/lameesmmi/ICS344-PROJECT/blob/main/phase-3/Screenshots/Before%20the%20attack.png?raw=true)


3. **Installing Fail2Ban on the Victim Machine**  
   After confirming the system's vulnerability, we installed Fail2Ban on the Metasploitable3 machine. This tool is designed to monitor authentication logs and automatically block suspicious IPs.
![fail2ban](https://github.com/lameesmmi/ICS344-PROJECT/blob/main/phase-3/Screenshots/Install%20Fail2Ban%20on%20Metasploitable3.png?raw=true)

4. **Configuring Fail2Ban for SSH Protection**  
   A configuration file was created to monitor SSH login attempts. The settings specified that an IP address should be banned after three failed login attempts. The ban duration was also defined to temporarily block access from malicious sources.



![configure](https://github.com/lameesmmi/ICS344-PROJECT/blob/main/phase-3/Screenshots/Configure%20Fail2Ban%20for%20SSH.png?raw=true)

5. **Activating the Defense Mechanism**  
   The Fail2Ban service was restarted to apply the configuration and begin monitoring login activity on the SSH port.

![restart](https://github.com/lameesmmi/ICS344-PROJECT/blob/main/phase-3/Screenshots/Restart%20Fail2Ban%20Service.png?raw=true)


6. **Rerunning the SSH Brute-Force Attack**  
   With the defense active, we reran the Hydra attack from the Kali machine. After three failed attempts, Fail2Ban automatically detected the brute-force behavior and blocked the attacker’s IP.

7. **Verifying Fail2Ban’s Response**  
   On the victim machine, we checked the Fail2Ban status and log files to confirm that the attacker’s IP had been successfully banned. The ban entry was visible in both the Fail2Ban service output and the fail2ban log.

8. **Validating the Effectiveness of the Defense**  
   To further confirm the defense, we attempted to SSH into the victim machine again from the attacker. The connection was refused, demonstrating that Fail2Ban was actively protecting the system by preventing repeated unauthorized login attempts.

---

##  Tools & Environment

- **Victim Machine**: Metasploitable3  
- **Attacker Machine**: Kali Linux  
- **Tools Used**: Fail2Ban, Hydra, SSH  

---

## 🌐 IP Addresses

- **Attacker IP**: 192.168.183.7  
- **Victim IP**: 192.168.183.3

