# mailGoogleResults
###### This script ensures that your predetermined query is sent to you as soon as it is published on the internet.This script ensures that your predetermined query is sent to you as soon as it is published on the internet.
------------
##### You can set a cron job to run it often as you want. 
A simple cron job configuration, say terminal:

`crontab -e`

Add a new line to set a job like follow command to the bottom line:

`*/30 * * * * /usr/bin/python3 ~/Desktop/projects/python/googleScan/googlescan.py`

(This job will run googlescan.py 1 time in 30 minutes.)

[Cron Job Commands](https://phoenixnap.com/kb/set-up-cron-job-linux "More commands")

##### NOTE: 
You should [turn on](https://myaccount.google.com/lesssecureapps) less secure apps setting for your google account to connect your email with this script.

And using 2-factor authentication will cause problem connecting to your gmail account.
