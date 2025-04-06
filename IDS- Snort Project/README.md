# 🛡️ Intrusion Detection System (IDS) using Snort

This project demonstrates the setup and working of an Intrusion Detection System (IDS) using **Snort** on a virtual Ubuntu Server. The IDS monitors network traffic and detects simulated attacks using custom rules.

---

## 📄 Abstract

In today’s digital era, network security is paramount, and Intrusion Detection Systems (IDS) are a core component of cybersecurity. This project focuses on setting up a basic IDS using Snort, an open-source tool, to monitor network traffic for suspicious activity. By creating a virtual network environment using VirtualBox and Ubuntu Server, Snort is configured to listen for ICMP (ping) traffic and generate alerts based on a custom rule. This project successfully demonstrates how Snort detects basic intrusion attempts, providing a foundational understanding of IDS operation and behavior in a simulated network environment.

---

## 🎯 Objectives

- Set up an Intrusion Detection System using Snort.
- Simulate a virtual network environment using VirtualBox.
- Configure and test Snort on Ubuntu Server.
- Write and apply a custom Snort rule.
- Simulate a network attack and observe alert generation.
- Understand how Snort processes and reports suspicious activity.

---

## 🧰 Tools & Technologies Used

- 🐧 Ubuntu Server 22.04 (VirtualBox)
- 🐷 Snort IDS
- 💻 ICMP Protocol Simulation
- 📄 Custom Snort Rules
- 🖥️ VirtualBox

---

## 🚀 Setup & Configuration

### Step 1: Install VirtualBox
Download and install from: [https://www.virtualbox.org](https://www.virtualbox.org)

### Step 2: Install Ubuntu Server
Download ISO: [Ubuntu Server 22.04 ISO](https://releases.ubuntu.com/22.04/)  
Create VM with:
- 2GB RAM or more
- 20GB+ storage
- Network: Bridged Adapter (for connectivity)

Install and set up username/password.

### Step 3: Update System
```bash
sudo apt update && sudo apt upgrade -y
```

### Step 4: Install Snort
```bash
sudo apt install snort -y
```
During setup, select the correct network interface (usually `enp0s3`).

---

## 🛠️ Snort Configuration

### Edit Snort Rule File
```bash
sudo nano /etc/snort/rules/local.rules
```

Add this custom rule:
```snort
alert icmp any any -> any any (msg:"ICMP test detected"; sid:1000001; rev:1;)
```

### Confirm Snort Configuration
Make sure this line exists in `/etc/snort/snort.conf`:
```bash
var RULE_PATH /etc/snort/rules
```

---

## 🧪 Demonstration

### Step 1: Run Snort
```bash
sudo snort -A console -q -c /etc/snort/snort.conf -i enp0s3
```

### Step 2: Simulate Ping Attack
Open another terminal (or system on the same network):
```bash
ping <Snort_VM_IP>
```

### Step 3: Observe Alert
Snort will display:
```
[**] [1:1000001:1] ICMP test detected [**]
```

---

## 🔍 Working & Methodology

1. **Virtual Environment**: A virtual Ubuntu Server was set up using VirtualBox.
2. **Snort Installation**: Snort was installed and configured to monitor the network.
3. **Rule Creation**: A custom ICMP rule was added to detect ping traffic.
4. **Attack Simulation**: A basic `ping` was used to simulate a network probe.
5. **Detection**: Snort captured the ping and generated a real-time alert.
6. **Verification**: The alert validated the IDS was working as expected.

---
## 📸 Screenshots of IDS working

- VirtualBox VM setup - (screenshots/Picture1.jpg)
  
- Ubuntu installation steps  
- Terminal after Snort installation  
- `snort -V` command output  
- Contents of `local.rules`  
- Snort running in console  
- Terminal showing alert from ICMP rule  
- `ping` command terminal used for test

---


## ✅ Conclusion

This project illustrates how an Intrusion Detection System like Snort can be used to monitor traffic and detect basic attacks such as ICMP pings. The virtual lab environment provided hands-on experience in configuring Snort, writing rules, and interpreting alerts. It offers foundational insight into IDS operations, which is essential for further learning in cybersecurity.

---

## 🎥 Demo Video

🎥 [Watch Demo Video Here](https://drive.google.com/file/d/1FS9Og6Px6-K-bcK2XvlDGvXlJ5ZhXIBj/view?usp=sharing)

---

## 🗂️ Repository Structure

```
IDS-Snort-Project/
️├── README.md
├── report.docx / report.pdf
├── /screenshots
│   ├── vm-setup.png
│   ├── snort-install.png
│   ├── rule-config.png
│   └── alert-output.png

```


## 💡 Future Scope

- Include more advanced rules for TCP, HTTP, or brute force detection.
- Integrate Snort with a log management tool like Splunk or ELK stack.
- Use Security Onion for full-featured IDS/IPS environment.

---

## 🍿 License

This project is for academic purposes only.  
Snort is an open-source project maintained by Cisco Talos.

---

## 🙌 Acknowledgements

- Snort by Cisco Talos  
- Ubuntu Community  
- VirtualBox  
- Network Security Educators and Open Source Contributors

  
