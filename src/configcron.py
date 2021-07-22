from crontab import CronTab

cron = CronTab(tabfile='/etc/crontab', user='sevenke')  # system users cron
# cron  = CronTab(user=True)  # current users cron
# cron  = CronTab(user='username')  # other users cron
for job in cron:
    print(job)

job = cron.new(command='cd /home/sevenke && sudo -u postgres python3 mailservice.py', comment='send mail once a day')
job.minute.every(1)
cron.write()

#Install ron before executing this file: sudo apt install cron
#Enable cron: sudo systemctl enable cron
#Save this to root, startup script command: sudo python3 /home/sevenke/configcron.py
