# 📊 Phase 2 – SSH Log Analysis with Splunk

## 🔍 Objective
To extract authentication logs from the victim machine (Metasploitable3), ingest them into Splunk, and visualize SSH login behavior in order to detect brute-force attack patterns.

---

## 🔧 Steps Taken

1. **Extracting the Logs**  
   The authentication log file (authlog.txt- can be found in SIEM logs folder) was extracted from the victim machine for analysis.

![Authlogs](https://github.com/lameesmmi/ICS344-PROJECT/blob/main/phase-2/siem-logs/authlog.png)

2. **Downloading and Signing in to Splunk Web**  
   Splunk Enterprise was downloaded and installed. The analyst signed in through the Splunk web interface.

![Splunk](https://github.com/lameesmmi/ICS344-PROJECT/blob/main/phase-2/visuals/Download%20Splunk%20web%20and%20sign%20in.png)


3. **Running a Search for SSH Login Activity**  
   - Navigate to: Search & Reporting > Data Summary  
   - Select the Host: metasploitable3  
   - Source: authlog(1).txt  
   - Search query used: ("Failed password" OR "Accepted password")  
   - This allowed for clear filtering of SSH login attempts.
![Search](https://github.com/lameesmmi/ICS344-PROJECT/blob/main/phase-2/visuals/Apply%20the%20search.png)

---

## 📈 Analysis Outcomes

![Visualisation](https://github.com/lameesmmi/ICS344-PROJECT/blob/main/phase-2/visuals/Visualization%20and%20analysis%20of%20the%20attack.png)

1. Splunk successfully ingested and parsed the log file from the victim machine.

2. SSH authentication activity was clearly visible, showing a large number of "Failed password" events compared to relatively few "Accepted password" events.

3. Attack data was effectively classified into two categories (Failed, Accepted) using a search command in Splunk.

4. A bar chart visualization provided a clear view of brute-force attack patterns, with **1,423 failed login attempts** and only **27 successful ones**, indicating suspicious login behavior.

5. This visualization enables security teams to quickly detect and respond to brute-force SSH login attempts, highlighting the importance of monitoring failed authentications in real-time.
