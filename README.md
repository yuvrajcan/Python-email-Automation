# Email Automation Project

## 📌 Overview
This repository contains Python scripts for automating email tasks including sending text emails, emails with attachments, and scheduled emails. The scripts use Gmail's SMTP server for reliable email delivery.

## 🚀 Features

### 📤 Email Scripts:
1. **Plain Text Emails** (`text_to_mail.py`)
   - Simple text email sender
   - Interactive input for recipient, subject, and body

2. **Email with Attachments** (`file_to_mail.py`)
   - Send PDF attachments
   - Supports any file type with minor modifications

3. **Scheduled Emails** (`schedule_mail.py`)
   - Automatically resends email every 5 seconds
   - Tracks number of emails sent

## 🛠️ Setup Instructions

### Prerequisites
- Python 3.6+
- Required packages: `schedule`

```bash
pip install schedule
```

### Configuration
1. Clone the repository:
```bash
git clone https://github.com/your-username/email-automation.git
cd email-automation
```

2. For security, create a `.env` file:
```env
EMAIL_USER=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
```

3. Modify scripts to use environment variables (recommended):
```python
import os
from dotenv import load_dotenv

load_dotenv()
my_email = os.getenv('EMAIL_USER')
password = os.getenv('EMAIL_PASSWORD')
```

## 📋 Usage

| Script | Command | Description |
|--------|---------|-------------|
| Text Email | `python text_to_mail.py` | Send basic text email |
| File Email | `python file_to_mail.py` | Email with PDF attachment |
| Scheduled | `python schedule_mail.py` | Recurring email sender |

## ⚠️ Important Notes
- 🔒 Never commit actual credentials to version control
- 📧 Gmail has daily sending limits (~100-150 emails/day)
- ⏳ The scheduled email script runs indefinitely (Ctrl+C to stop)
- 🚫 Avoid using your primary email password - use [App Passwords](https://myaccount.google.com/apppasswords)

## 📄 Sample Files
- `file.pdf`: Example internship offer letter (demonstration only)
- `.gitignore`: Prevents accidental credential leakage

## 🤝 Contributing
Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## 📜 License
MIT License - Free for personal and commercial use

---

**💡 Pro Tip**: For production use, consider:
- Using email services like SendGrid or Mailgun
- Implementing proper error handling
- Adding logging functionality
- Creating a configuration file for email templates
