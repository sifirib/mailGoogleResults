import time
import os
import smtplib
import ssl

try:
    from googlesearch import search
except importerror:
    print("no module named 'google' found")

#query = input("What you want to search? :")
query = "Coranavirus" # your query here
query = (''.join(query)).encode('utf-8')

os.system(f'notify-send "hi"')

port = 465
sender = "example@example.com" # your email here
password = "password" # your password here
recieve = sender

def send_mail(query, j):

    message = f"""\
    Subject: Results for {query}

    Results for {query}:
    {j}

    from googlescan
    """

    context = ssl.create_default_context()
    print("starting to send")
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server: # change gmail with your provider(hotmail, outlook, yandex...)
        server.login(sender, password)
        server.sendmail(sender, recieve, message)
    print("sent mail")



while True:

    results = list(search(query, num=10, stop=1, pause=2))
    file = open(f"notification.txt", "a")
    if len(results) == 0:
        print("no results.")
    else:
        for j in results:
            print(f"results of '{query}': \n{j}")
            os.system(f'notify-send "results of {query}: \n{j}"')
            file.write(f"{j}\n")

            send_mail(query, j)

    file.close()
    time.sleep(5)
    exit()
