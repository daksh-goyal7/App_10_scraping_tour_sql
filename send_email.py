import smtplib,ssl

def send_email(message):
    host="smtp.gmail.com"
    port=465
    # Enter gmail id here
    username="example@gmail.com"
    # Enter password generated for this app specifically.
    password="ctmdlmjxqwytdufw"
    receiver="example@gmail.com"
    context=ssl.create_default_context()
    with smtplib.SMTP_SSL(host,port,context=context) as server:
        server.login(username,password)
        server.sendmail(username,receiver,message)
    print("mail send successfully")

