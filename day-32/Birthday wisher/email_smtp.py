# 1. Make sure you've got the correct smtp address for your email provider:

# Gmail: smtp.gmail.com

# Hotmail: smtp.live.com

# Outlook: outlook.office365.com

# Yahoo: smtp.mail.yahoo.com

# If you use another email provider, just Google for your email provider e.g. "Gmail SMTP address"

# Add a port number by changing your code to this:

# smtplib.SMTP("smtp.gmail.com", port=587) 

import smtplib

my_email = "anadevmanuel@gmail.com"
password = "cCuiKjXuwg82Whm"

# connection = smtplib.SMTP("smtp.gmail.com", port=587)
with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="anadevmanuel@yahoo.com", msg="Subject:Hello dear Ana\n\nMy dear I miss you")
# connection.close()