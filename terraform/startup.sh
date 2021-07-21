sudo apt update
sudo apt install postgresql postgresql-contrib
sudo apt-get install libpq-dev python-dev
sudo apt-get -y install python3-pip
pip3 install python-crontab
pip3 install configparser
pip3 install psycopg2
pip3 install secure-smtplib
pip3 install email-to

gsutil cp -r gs://cli-server-files/config.py .