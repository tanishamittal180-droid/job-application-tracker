import smtplib

def send_email(to_email, subject, message):

    sender = "your_email@gmail.com"
    password = "your_app_password"

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender, password)

        msg = f"Subject: {subject}\n\n{message}"

        server.sendmail(sender, to_email, msg)
        server.quit()

        return True

    except Exception as e:
        print("Email Error:", e)
        return False