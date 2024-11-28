def send_email(receiver_email: str, sub: str = 'Program Info', text: str = '', sender: str or None = None, password: str or None = None, img: str or list or None = None, attach: str or list or None = None):
    from email.mime.text import MIMEText
    from email.mime.image import MIMEImage
    from email.mime.application import MIMEApplication
    from email.mime.multipart import MIMEMultipart
    import smtplib
    import os

    try:
        # Initialize connection to Gmail's SMTP server
        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.ehlo()
        smtp.starttls()

        # Login with provided credentials or environment variables
        if sender is None or password is None:
            sender = os.environ.get('Gmail_ID')
            password = os.environ.get('Gmail_Passkey')
            if sender is None or password is None:
                raise ValueError("Email credentials are not provided.")

        smtp.login(sender, password)

        # Build the email message
        def message(subject: str, text: str, img=None, attachment=None):
            msg = MIMEMultipart()
            msg['From'] = sender
            msg['To'] = receiver_email
            msg['Subject'] = subject
            msg.attach(MIMEText(text, 'plain'))

            if img:
                if not isinstance(img, list):
                    img = [img]
                for one_img in img:
                    with open(one_img, 'rb') as f:
                        img_data = f.read()
                        msg.attach(MIMEImage(img_data, name=os.path.basename(one_img)))

            if attachment:
                if not isinstance(attachment, list):
                    attachment = [attachment]
                for one_attachment in attachment:
                    with open(one_attachment, 'rb') as f:
                        file = MIMEApplication(f.read(), name=os.path.basename(one_attachment))
                        file['Content-Disposition'] = f'attachment; filename="{os.path.basename(one_attachment)}"'
                        msg.attach(file)

            return msg

        msg = message(subject=sub, text=text, img=img, attachment=attach)

        # Send the email
        smtp.sendmail(from_addr=sender, to_addrs=receiver_email, msg=msg.as_string())
        print("Email sent successfully!")

    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        smtp.quit()


if __name__ == '__main__':
    send_email(
        receiver_email='test@gmail.com',
        sub='Test Email',
        text='This is a test email.',
        sender='youremail@gmail.com',
        password='yourpassword',
        img=None,
        attach=None
    )
