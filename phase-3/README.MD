We implemented Fail2Ban on the Metasploitable3 machine to protect against SSH brute-force attacks, to automatically bans IP addresses after multiple failed login attempts.
1. A brute-force SSH attack was simulated using Hydra on the attacker machine.
2. Weused incorrect credentials from a password list.
3. After three failed login attempts, Fail2Ban triggered and automatically banned the attacker's IP address (192.168.183.7).
4. This demonstrates that Fail2Ban effectively mitigated SSH brute-force attacks by detecting failed login patterns and blocking attackers.

Steps:

1. Pinging the Victim Machine: to verify the network connectivity between the attacker and the victim.
2. Install Fail2Ban on Metasploitable3:using (sudo apt-get update) &
(sudo apt-get install fail2ban)
3. Configure Fail2Ban for SSH Protection:(sudo nano /etc/fail2ban/jail.d/ssh.conf)
set configuration to block after 3 failed login attempts:
([sshd]
enabled = true
port = ssh
filter = sshd
logpath = /var/log/auth.log
maxretry = 3
bantime = 600)
4. Restart Fail2Ban Service:(sudo service fail2ban restart)
5. Launch SSH Brute-Force Attack Using Hydra (from Kali): (hydra -l root -P pass.txt ssh://192.168.183.3 -t 4)
6. Verify Banned IP Address on Victim Machine
Check Fail2Ban status:
(sudo fail2ban-client status sshd)
View log entries:
(sudo tail /var/log/fail2ban.log): Verified that IP 192.168.183.7 was banned.
7. Manual SSH Login Attempt Test
Attempted to SSH into the victim using in theattacker machine:(ssh vagrant@192.168.183.3)
Entered 3 wrong passwords.
Connection was denied after 3 incorrect tries, which confirming the defense works.

Tools/Environmrnt:

Victim: Metasploitable3
Attacker: Kali Linux
Tools: Fail2Ban, Hydra, SSH

IP Adresses:
Attacker: 192.168.183.7
Victim: 192.168.183.3
