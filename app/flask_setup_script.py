# FLASK APP
# Thomas Instructions:
# https://github.com/InsightDataScience/flask-sample-app

# EC2 instance hosting app:
ssh -i "Connor-Dibble-IAM-keypair.pem" ubuntu@ec2-44-231-212-226.us-west-2.compute.amazonaws.com

# Clone repo with template:
# git clone https://github.com/InsightDataScience/flask-sample-app
. venv/bin/activate # activate python virtual environment
git clone https://github.com/cdibble/Smoke-Stack
cd flask-sample-app
sudo apt-get install python3-venv
python3 -m venv venv #--without-pip # create python vitrual environment from wtihin flask-sample-app

# pip3 install Flask # install Flask in virtual env.
# sudo apt install python3-flask
sudo apt-get install libpq-dev
cd ~/Smoke-Stack/app # use the following to ensure install in virtual env.
/home/ubuntu/Smoke-Stack/venv/bin/python3 -m pip install matplotlib
/home/ubuntu/Smoke-Stack/venv/bin/python3 -m pip install Flask
/home/ubuntu/Smoke-Stack/venv/bin/python3 -m pip install flask_restful
/home/ubuntu/Smoke-Stack/venv/bin/python3 -m pip install psycopg2
/home/ubuntu/Smoke-Stack/venv/bin/python3 -m pip install seaborn
/home/ubuntu/Smoke-Stack/venv/bin/python3 -m pip install pandas

/home/ubuntu/Smoke-Stack/venv/bin/python3 -m pip install matplotlib
/home/ubuntu/Smoke-Stack/venv/bin/python3 -m pip install Flask
/home/ubuntu/Smoke-Stack/venv/bin/python3 -m pip install flask_restful
/home/ubuntu/Smoke-Stack/venv/bin/python3 -m pip install psycopg2
/home/ubuntu/Smoke-Stack/venv/bin/python3 -m pip install seaborn
/home/ubuntu/Smoke-Stack/venv/bin/python3 -m pip install pandas

export FLASK_APP=hello.py # export FLASK_APP variable
flask run --host=0.0.0.0 # launch FLASK App

# http://ubuntu@ec2-44-231-212-226.us-west-2.compute.amazonaws.com:5000

####### Run Smoke-Stack App #######
# See tutorial: https://flask.palletsprojects.com/en/1.1.x/tutorial/database/
python3 -m venv venv #--without-pip 
. venv/bin/activate
git clone https://github.com/cdibble/Smoke-Stack
# scp -i "Connor-Dibble-IAM-keypair.pem" /Users/Connor/Documents/Graduate\ School/Dibble_Research/Github_repos/Smoke-Stack/app/AIS_Pings_App.py ubuntu@ec2-44-231-212-226.us-west-2.compute.amazonaws.com:/home/ubuntu/Smoke-Stack/app/
# scp -i "Connor-Dibble-IAM-keypair.pem" /Users/Connor/Documents/Graduate\ School/Dibble_Research/Github_repos/Smoke-Stack/app/templates/port_index.html ubuntu@ec2-44-231-212-226.us-west-2.compute.amazonaws.com:/home/ubuntu/Smoke-Stack/app/templates/
# scp -i "Connor-Dibble-IAM-keypair.pem" /Users/Connor/Documents/Graduate\ School/Dibble_Research/Github_repos/Smoke-Stack/app/templates/home.html ubuntu@ec2-44-231-212-226.us-west-2.compute.amazonaws.com:/home/ubuntu/Smoke-Stack/app/templates/
# scp -i "Connor-Dibble-IAM-keypair.pem" /Users/Connor/Documents/Graduate\ School/Dibble_Research/Github_repos/Smoke-Stack/app/templates/template.html ubuntu@ec2-44-231-212-226.us-west-2.compute.amazonaws.com:/home/ubuntu/Smoke-Stack/app/templates/


export FLASK_APP=AIS_Pings_App
# export FLASK_ENV=development
# export APP_SETTINGS="config.DevelopmentConfig"
# export DATABASE_URL="postgresql://10.0.0.14:5432/pings_db"
flask run --host=0.0.0.0

# to run on Port 80
sudo su - # switch to user su
. venv/bin/activate
export FLASK_APP=AIS_Pings_App.py
nohup flask run --host=0.0.0.0 --port=80 &
http://ec2-44-231-212-226.us-west-2.compute.amazonaws.com:80/home


# PostgreSQL
# Determining missing Ports 
create table ports_written_in_sd as select distinct "PORT_NAME" from pings_final_in_port_with_visitsubgroup_noudf;
create table ports_not_written_in_sd as select distinct "PORT_NAME" from pings_commercial;
select * from ports_not_written_in_sd where "PORT_NAME" not in (select * from ports_written_in_sd);