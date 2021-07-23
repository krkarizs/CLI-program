sudo apt update
sudo apt-get -y install postgresql
sudo apt-get -y install libpq-dev python-dev
sudo apt-get -y install python3-pip
pip3 install python-crontab
pip3 install configparser
yes | pip3 install psycopg2
pip3 install secure-smtplib
pip3 install email-to
gsutil cp gs://cli-server-filez/config.py /home/sevenke/config.py
gsutil cp gs://cli-server-filez/query.py /home/sevenke/query.py
gsutil cp gs://cli-server-filez/main.py /home/sevenke/main.py
gsutil cp gs://cli-server-filez/database.ini /home/sevenke/database.ini
gsutil cp gs://cli-server-filez/weatherconfig.ini /home/sevenke/weatherconfig.ini
gsutil cp gs://cli-server-filez/mailconfig.ini /home/sevenke/mailconfig.ini
gsutil cp gs://cli-server-filez/mailservice.py /home/sevenke/mailservice.py
gsutil cp gs://cli-server-filez/weather.py /home/sevenke/weather.py
gsutil cp gs://cli-server-filez/create_tables.py /home/sevenke/create_tables.py
sudo systemctl restart postgresql
sudo -u postgres createdb workplace
sudo -u postgres yes | pip3 install psycopg2
sudo -u postgres python3 /home/sevenke/create_tables.py
sudo -u postgres pip3 install python-crontab
sudo python3 /home/sevenke/cronconfig.py
sudo echo 'cd /home/sevenke && sudo -u postgres python3 main.py' &>>/etc/bash.bashrc 