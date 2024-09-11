import smtplib
import json
from email.mime.text import MIMEText
from modules.files import readJson
from email.mime.multipart import MIMEMultipart


def send_email(**context):
    subject = context["var"]["value"].get("subject_mail")
    from_address = context["var"]["value"].get("email")
    password = context["var"]["value"].get("email_password")
    to_address = context["var"]["value"].get("to_address")


    data_uploaded=readJson()
    if len(data_uploaded)<=2:
        data_uploaded="No new data to upload!"

    print(subject)
    print(from_address)
    print(password)
    print(to_address)

    # Create a MIMEText object
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject

    # Create HTML content
    html_content = f"""
    <html>
    <body>
        <p>El proceso de extracción y de carga de nuevas películas a Redshift ha sido realizado con éxito</p>
        <p><strong>{data_uploaded}</strong></p>
    </body>
    </html>
    """

    # Attach HTML content
    msg.attach(MIMEText(html_content, 'html'))

    try:
        # Create an SMTP session
        server = smtplib.SMTP('smtp.gmail.com', 587)  # Use your SMTP server and port
        server.starttls()  # Enable security

        # Login to the server
        server.login(from_address, password)

        # Send the email
        text = msg.as_string()
        server.sendmail(from_address, to_address, text)
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {str(e)}")