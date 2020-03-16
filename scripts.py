import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

email = EmailMessage()
email['from'] = 'Hoang Long'
email['To'] = 'hoanglong.hcmus@gmail.com'
email['subject'] = 'Hello, Im from Viet Nam'

template_mail = Template(Path('template.html').read_text())

email.set_content(template_mail.substitute({'name': 'Hoang Long'}), 'html')

if __name__ == "__main__":
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('lovemyfamily1712@gmail.com', '0919610909aA')
        smtp.send_message(email)
        print('done')

