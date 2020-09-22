# mailGoogleResults
###### This script ensures that your predetermined query is sent to you as soon as it is published on the internet.This script ensures that your predetermined query is sent to you as soon as it is published on the internet.
------------
##### You can set a cron job to run it often as you want. 
A simple cron job configuration:

`crontab -e`

Add a new line to set a job like this to the bottom line:

`*/30 * * * * /usr/bin/python3 ~/Desktop/projects/python/googleScan/googlescan.py`

(This job will run googlescan.py 1 time in 30 minutes.)

[More Commands](https://phoenixnap.com/kb/set-up-cron-job-linux "More commands")


