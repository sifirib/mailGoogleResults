import time
import os
import smtplib, ssl
port = 465

try:
    from googlesearch import search
except importerror:
    print("no module named 'google' found")


def read_credentials():
    sender = password = ""
    with open("credentials.txt", "r") as f:
        file = f.readlines()
        sender = file[0].strip()
        password = file[1].strip()
    return sender, password

def read_query():
    queries = []
    with open("query.txt", "r") as f:
        file = f.readlines()
        i = 0
        while True:
            try:
                q = str(file[i].strip())
                queries.append(q)
                i += 1
            except:
                return queries
                break

def send_mail():

    context = ssl.create_default_context()
    print("starting to send")
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server: # change gmail with your provider(hotmail, outlook, yandex...)
        server.login(sender, password)
        server.sendmail(sender, recieve, message)
    print("sent mail")


sender, password = read_credentials()
recieve = sender
queries = read_query()


while True:

    subject = "Subject: Results For Queries"
    message = ""
    close = "\nfrom googlescan"
    for query in queries:
        query = (''.join(query)).encode('utf-8')

        results = list(search(query, num=10, stop=1, pause=2))

        if len(results) == 0:
            print("no results.")
        else:
            for j in results:
                print(f"results of '{query}': \n{j}")
                os.system(f'notify-send "results of {query}: \n{j}"')

                message += f"""\nResults for {query}:\n{j}"""


        time.sleep(5)
    message = subject + message + close
    send_mail()
    time.sleep(5)
    exit()
