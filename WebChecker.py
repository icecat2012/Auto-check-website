import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import webbrowser
from datetime import datetime

def sendgmail(sender_email, sender_key, receiver_name, To_email, receiver_name2, cc_email, titlee, msg_content):
    try:
        sender_name = 'Auto_web_watcher'
        pure_text = ''
        html_text = msg_content
        
        message = MIMEMultipart('alternative')
        message['From'] = sender_name + ' <' + sender_email + '>'
        
        if len(To_email) > 0:   
            for tmp_num in range(len(To_email)) :
                if tmp_num == 0:
                    message['To'] = receiver_name[0] + ' <' + To_email[0] + '>'
                else :
                    message['To'] += ', ' + receiver_name[tmp_num] + ' <' + To_email[tmp_num] + '>'
        else :
            message['To'] = ''
            
        if len(cc_email) > 0:
            for tmp_num in range(len(cc_email)) :
                if tmp_num == 0:
                    message['Cc'] = receiver_name2[0] + ' <' + cc_email[0] + '>'
                else :
                    message['Cc'] += ', ' + receiver_name2[tmp_num] + ' <' + cc_email[tmp_num] + '>'
        else :
            message['Cc'] = ''
            
        message['Subject'] = titlee

        # Record the MIME types of both parts - text/plain and text/html.
        part1 = MIMEText(pure_text, 'plain')
        part2 = MIMEText(html_text, 'html')

        # Attach parts into message container.
        # According to RFC 2046, the last part of a multipart message, in this case
        # the HTML message, is best and preferred.
        message.attach(part1)
        message.attach(part2)

        msg_full = message.as_string()

        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(sender_email, sender_key)
        server.sendmail(sender_email, (To_email + cc_email), msg_full)
        server.quit()
        return 0
    except Exception as e:
        print(e)
    return -1

def check_website(url, max_request = 5, max_time=5):
    try:
        requests.adapters.DEFAULT_RETRIES = max_request
        s = requests.session()
        s.keep_alive = False
        r = s.get(url, timeout = max_time)
    except Exception as e:
        print(e)
        return -1
    if r.status_code == requests.codes.ok:
        return 0
    
    return 1

def main():
    sender_email = "YourEmail@gmail.com"
    sender_key = "itsexamplenotreal" # fill in application passwords : https://support.google.com/mail/answer/185833?hl=en
    Target_website = 'https://icecat2012.github.io/' # change to your target website
    Check_period_sec = 1200 #min 10 sec
    Receiver_email_list = ['ReceiverEmail@gmail.com']
    Receiver_name_list = ['FROM_BOT'] # you can fill in what you want
    email_title = 'Your website got some problems!'
    Youtube_alarm = "https://www.youtube.com/watch?v=SkgTxQm9DWM&ab_channel=BufuSounds"

    while True:
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print(dt_string)    

        ans = check_website(Target_website)
        if ans == 0:
            print('ok')
        else:
            msg = "Please check the website. {}".format(dt_string)
            ans = sendgmail(sender_email, sender_key, Receiver_name_list, Receiver_email_list, [''], [''], email_title, msg)

            # Open Youtube to wake you UP!
            #webbrowser.open(Youtube_alarm)

            # If fail to send a mail
            #if ans != 0:
            #    webbrowser.open(Youtube_alarm)
        
        c = datetime.now() - now
        while c.total_seconds()<Check_period_sec:
            c = datetime.now() - now
            time.sleep(10)
        
if __name__ == '__main__':
    main()
