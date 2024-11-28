
def send_email(message, recipient, *, sender="university.help@gmail.com"):
    def is_valid_email(email):
        return "@" in email and email.endswith((".com", ".ru", ".net"))

    if not is_valid_email(recipient) or not is_valid_email(sender):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient} .")
        return

    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return

    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")

send_email("Hello, this is a test message.", "sobachka@gmail.com")
send_email("Hello, this is a test message.", "sobachka@gmail.com", sender="blablabla@gmail.com")
send_email("Hello, this is a test message.", "sobachka@gmail.com", sender="invalid_email")
send_email("Hello, this is a test message.", "university.help@gmail.com")