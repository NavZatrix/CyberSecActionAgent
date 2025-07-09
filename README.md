# CyberSecActionAgent

**CyberSecActionAgent** is an action-enabled AI system designed to assist cybersecurity teams by automating key vulnerability management tasks. It uses OpenAI's function-calling capability to understand input and trigger relevant actions such as querying vulnerability data, creating task cards, and sending email notifications.

## 🔍 Use Case

When a user inputs a command like:

Check vulnerability CVE-2023-12345

The agent:
1. Queries a (simulated) vulnerability database.
2. Creates a task card in Trello to investigate and remediate the issue.
3. Sends an automated email to the security team for awareness and tracking.

## ⚙️ Features

- 📥 Accepts natural language queries
- 📡 Queries vulnerability data (simulated API)
- 📋 Creates Trello task cards (simulated)
- 📧 Sends email notifications (console output)
- 🧠 Powered by OpenAI GPT with function calling

## 🛠️ Tech Stack

- Python 3
- OpenAI GPT API (function calling)
- Trello API (simulated)
- SMTP (simulated email)
- CLI-based user interaction

## 🧪 Example Input

Enter your query: Check vulnerability CVE-2023-12345

Output:

Trello card created: Investigate CVE-2023-12345
Email sent to security_team@example.com regarding CVE-2023-12345


🔐 This project simulates how AI agents can enhance cybersecurity workflows by automating repetitive and time-sensitive tasks.
