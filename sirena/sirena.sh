#getting first arg
GROUP=$1
#creating virtual environment
virtualenv -p /usr/bin/python3 venv
source venv/bin/activate
#installing python libs
venv/bin/pip3 install -r requirements.txt
deactivate
#creating dir for sirena's configuration file
mkdir /etc/sirena
#creating dir for sirena's logs
mkdir /var/log/sirena
#creating sirena's log file
touch /var/log/sirena/sirenasrv.log
#backuping sirena's config file. If it's the first install this command returns error "File does not exist". It's ok
mv /etc/sirena/sirena.yaml /etc/sirena/sirena.yaml.save
#moving example sirena's config to /etc/sirena/sirena.yaml
cp /opt/SirenaSmith/sirena/sirena.yaml.example /etc/sirena/sirena.yaml
#creating systemd daemon
sed 's/SIRENA_GROUP/'$GROUP'/g' /opt/SirenaSmith/configs/systemd/sirena.service.example > /etc/systemd/system/sirena.service
#backuping nginx config. If it's the first install this command returns error "File does not exist". It's ok
mv /etc/nginx/conf.d/sirena.conf /etc/nginx/conf.d/sirena.conf.save
#moving example nginx config to /etc/nginx/conf.d/sirena.conf.save
cp /opt/SirenaSmith/configs/nginx/sirena.conf.example /etc/nginx/conf.d/sirena.conf
#setting privileges for work dirs
chown -R $GROUP:$GROUP /opt/SirenaSmith/
chown -R $GROUP:$GROUP /var/log/sirena/
chown -R $GROUP:$GROUP /etc/sirena/
#nginx configs test
nginx -t
#enable sirena service
systemctl enable sirena