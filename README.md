# 📧 Python Email Sender Script

This is a Python script for sending emails using **Gmail's SMTP server**. It supports plain text emails and allows the inclusion of **attachments** and **images**. The script is flexible and can work with credentials passed either as arguments or environment variables.

---

## 🔧 Features

- Send emails to a single recipient.
- Add multiple **attachments** (e.g., files, PDFs, etc.).
- Embed **images** in the email.
- Use **environment variables** for secure email credentials.
- Simple and reusable function.

---

## 📂 Files

1. **`email_sender.py`**: The Python script containing the email-sending functionality.

---

## 🚀 Usage

### 1. Prerequisites
- Install Python 3.x.
- Install any required libraries:
  ```bash
  pip install smtplib email

Make sure to enable "Allow less secure apps" in your Gmail account or generate an App Password.

### 2. Code Example
You can directly call the send_email function from the script as follows:
```bash
 send_email(
    receiver_email='recipient@example.com',  # Recipient's email
    sub='Test Email',                       # Subject
    text='This is a test email.',           # Email body
    sender='youremail@gmail.com',           # Sender's email
    password='yourpassword',                # Sender's email password
    img=['path/to/image.jpg'],              # Optional: Attach image(s)
    attach=['path/to/file.pdf']             # Optional: Attach file(s)
  )
```
### 3. Function Parameters
receiver_email (str): Email address of the recipient.
sub (str): Subject of the email (default: 'Program Info').
text (str): Email body text (default: '').
sender (str): Sender's email address. If None, the script fetches credentials from environment variables.
password (str): Sender's email password. If None, the script fetches credentials from environment variables.
img (str or list): Optional. Path(s) to image(s) to include in the email.
attach (str or list): Optional. Path(s) to file(s) to attach to the email.

### 4. Using Environment Variables
To securely store your email credentials:

Set the following environment variables:

```bash
export Gmail_ID='youremail@gmail.com'
export Gmail_Passkey='yourpassword'
```
Call the function without providing sender and password:
```
send_email(
    receiver_email='recipient@example.com',
    sub='Secure Email',
    text='This email uses environment variables!',
    img=None,
    attach=None
)
```
### 🛠 How It Works
Establishes a connection to Gmail's SMTP server using the smtplib library.
Builds the email using MIMEMultipart for handling text, attachments, and images.
Sends the email to the specified recipient and closes the SMTP connection.
### 🛑 Common Errors and Fixes
Authentication Error: Ensure you've enabled App Passwords or "Allow less secure apps" in Gmail.
File Not Found: Provide the correct path to attachments and images.
SMTP Connection Error: Check your internet connection and Gmail SMTP settings.

