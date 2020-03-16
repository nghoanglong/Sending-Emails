import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def get_user(filename):
    customers = []
    with open(filename, 'r') as f:
        for user in f:
            customers.append({'email': user})
    return customers


if __name__ == "__main__":
    # phần dữ liệu này mình chỉ để minh họa, khi làm project dữ liệu này phải được bảo mật
    my_info = {
        'email': 'lovemyfamily1712@gmail.com',
        'pwd': '0919610909aA',
        'name': 'hoanglongsairoi'
    }
    customers = get_user('data.txt')
    template_mail = open('template.html', 'r')

    email = MIMEMultipart()
    email['From'] = my_info['name']
    email['Subject'] = "Yo Yo Yo"

    message = MIMEText(template_mail.read(), 'html')
    email.attach(message)  # đính kèm message đã tạo ở trên là form html

    for user in customers:
        email['To'] = user['email']
        with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(my_info['email'], my_info['pwd'])
            smtp.sendmail(my_info['email'], user.get('email'), email.as_string())
        print('done')
