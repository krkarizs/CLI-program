sudo apt update
sudo apt-get -y install postgresql
sudo apt-get -y install libpq-dev python-dev
sudo apt-get -y install python3-pip
pip3 install python-crontab
pip3 install configparser
yes | pip3 install psycopg2
pip3 install secure-smtplib
pip3 install email-to
gsutil cp gs://cli-server-files/config.py /home/sevenke
gsutil cp gs://cli-server-files/query.py /home/sevenke
gsutil cp gs://cli-server-files/main.py /home/sevenke
gsutil cp gs://cli-server-files/database.ini /home/sevenke
gsutil cp gs://cli-server-files/weatherconfig.ini /home/sevenke
gsutil cp gs://cli-server-files/mailconfig.ini /home/sevenke
gsutil cp gs://cli-server-files/mailservice.py /home/sevenke
gsutil cp gs://cli-server-files/weather.py /home/sevenke
gsutil cp gs://cli-server-files/create_tables.py /home/sevenke

sudo systemctl restart postgresql
sudo -u postgres createdb workplace
sudo -u postgres yes | pip3 install psycopg2
sudo -u postgres python3 /home/sevenke/create_tables.py