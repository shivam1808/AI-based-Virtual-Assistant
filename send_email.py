import smtplib
import urllib.request as urllib
# Senders email
sender_email = "virtualassistant.aibot@gmail.com"
# Receivers email

def sending_mail(name, rec_email, message):

    # Initialize the server variable
    message = "Hello " + name + ',\n' + message 
    server = smtplib.SMTP('smtp.gmail.com', 587)
    # Start the server connection
    server.starttls()
    # Login
    server.login("virtualassistant.aibot@gmail.com", "*******")
    print("Login Success!")
    # Send Email
    server.sendmail("Shivam Gupta", rec_email, message)
    server.quit()
    return ("Email has been sent successfully to "+rec_email)
