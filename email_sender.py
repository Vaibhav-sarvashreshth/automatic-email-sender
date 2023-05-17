import smtplib

def send_email():
    # Get user input
    recipient = input("Enter recipient's email address: ")
    subject = "Type Subject Here"
    body = "Type Body Here"
    num_times = int(input("Enter the number of times to send the email: "))

    # SMTP server configuration 
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587  # Default SMTP port

    # Sender's credentials
    sender_email = 'your_email_id@gmail.com'
    app_password = ''

    # Connect to the SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, app_password)

    # Send the email multiple times
    for i in range(num_times):
        message = f"Subject: {subject}\n\n{body}"
        server.sendmail(sender_email, recipient, message)
        print(f"Email {i+1}/{num_times} sent successfully.")

    # Disconnect from the server
    server.quit()

# Call the function to send the email
send_email()
