import smtplib
import config

# -------------------------------------------------------отправка сообщении-------------------------------------------------------------------

# def send_mail(message: str):
#     sender  = config.sender
#     password = config.password

#     server = smtplib.SMTP("smtp.gmail.com", 587)
#     server.starttls()

#     try:
#         server.login(sender, password)
#         server.sendmail(sender, "baimuratovaibek01@gmail.com", message)
#         return "MAIL SEND"
#     except Exception as error:
#         return f"Error: {error}"


# print(send_mail("salam, che delaesh?"))            

# -------------------------------------------------------- отправка рассылки---------------------------------------------------------------------

# def send_mail(subject: str, message: str):
#     sender  = config.sender
#     password = config.password

#     server = smtplib.SMTP("smtp.gmail.com", 587)
#     server.starttls()

#     try:
#         server.login(sender, password)
#         server.sendmail(sender, "baimuratovaibek01@gmail.com", f"subject: {subject} \n\n {message}")
#         return "Оправленно"
#     except Exception as error:
#         return f"Error: {error}"

# print(send_mail("Last Sunday GeekTech", "This Sunday, December 31st wil  be Last Sunday. Well be waiting for you:)"))

# -----------------------------------------------Групповой рассылка---------------------------------------------------------------------------------------

with open("emails.txt", "r") as e:
    res  = e.read().split()
    print(res)


def mailing(emails:list, subject, message):
    sender = config.sender
    password = config.password

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()


    try:
        server.login(sender, password)
        server.sendmail(sender, emails, f"subject: {subject} \n \n {message}")
        return  f" Рассылка окончено"
    except Exception as error:
        return f"Error: {error}"

print(mailing(res, "Mailing", 'hello worldd'))        