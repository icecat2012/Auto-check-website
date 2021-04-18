# Auto check website : webpage watcher
The program will automatically check a website every 20 minutes. If the webpage return code is not 'ok', the process will send an alarm email or open a Youtube page. Users can customize the checking period.

## How to run it
1. Download WebChecker.py
2. Apply a google application password for email service. See https://support.google.com/mail/answer/185833?hl=en or https://www.learncodewithmike.com/2020/02/python-email.html
4. Edit the 'sender_email', 'sender_key', 'Target_website', and 'Receiver_email_list' in the main function.
5. (Optional) If you would like to open a Youtube page as an alarm when the webpage cannot be accessed, please uncomment line 97 'webbrowser.open(Youtube_alarm)'. Remind: turn the volume up of your computer.
6. Run WebChecker.py
