#we have to modify the crontab with python
    #download pip to the VM
    sudo apt-get -y install python3-pip
    #download the required modules (for cron but also for the email and the SQL)
    pip3 install python-crontab
    pip3 install configparser
    pip3 install psycopg2
    pip3 install secure-smtplib
    pip3 install ssl
    pip3 install email-to
    #upload the python file tht modifies the crontab (we can put them in a bucket?)
    gsutil cp -r gs://YOUR-BUCKET-NAME/file.py .
    #upload the python file that runs the queries and sends the email
    gsutil cp -r gs://YOUR-BUCKET-NAME/file.py .