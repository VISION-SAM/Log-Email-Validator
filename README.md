# 🔍 Log-Email-Validator

**A recursive log-scanning tool for security analysts and penetration testers.**

This tool automates the discovery and verification of email addresses hidden within log files and text documents. Unlike basic parsers, it performs live **DNS MX-record checks** to ensure the domains discovered are actually capable of receiving mail.

---

## 🚀 Key Features
* **Recursive Discovery:** Scans all subdirectories for `.log` and `.txt` files.
* **Intelligent Parsing:** Uses a robust Regex pattern to find email structures in messy log data.
* **Live Verification:** Integrates `email-validator` to perform deliverability checks via DNS.
* **Deduplication:** Automatically handles unique email tracking using Python sets.

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/VISION-SAM/Log-Email-Validator.git
   cd Log-Email-Validator
   
2. Install dependencies:

```Bash
pip install -r requirements.txt
```

💻 Usage
Provide the target folder path as a command-line argument:

```Bash
python emailextractor.py ./logs/server_data
```

🛡️ Security Use Cases
OSINT: Verifying employee email patterns during reconnaissance.

Incident Response: Extracting contact points from compromised server logs.

Data Cleaning: Filtering out "dead" or fake domains from leaked datasets.
