from flask import Flask, request, render_template
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    subject =request.form['subject']
    message = request.form['message']

    # Send email
    send_email(name, email, subject, message)

    return f"Thank you {name}, your message has been sent!"

def send_email(name, email,subject, message):
    sender_email = "rohanrawat.dm@gmail.com"  # Replace with your Gmail address
    receiver_email = "rohanrawat.dm@gmail.com"  # Replace with the receiver's email address
    password = "rlzx xtxc ujjj juqp"  # Replace with your Gmail password or app-specific password

    # Create a MIME message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "New Contact Form Submission"

    # Email body content
    body = f"Name: {name}\nEmail: {email}\nSubject: {subject}\n\nMessage:\n{message}"
    msg.attach(MIMEText(body, 'plain'))

    # Connect to Gmail server and send email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
