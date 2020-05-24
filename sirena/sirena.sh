GROUP=$1

virtualenv -p /usr/bin/python3 venv
source venv/bin/activate
venv/bin/pip3 install -r requirements.txt
deactivate
mkdir /etc/sirena
mkdir /var/log/sirena
touch /var/log/sirena/sirenasrv.log
mv /etc/sirena/sirena.yaml /etc/sirena/sirena.yaml.save
cp /opt/SirenaSmith/sirena/sirena.yaml.example /etc/sirena/sirena.yaml
cp /opt/SirenaSmith/configs/systemd/sirena.service.example /etc/systemd/system/sirena.service
sed 's/SIRENA_GROUP/nginx/g' /etc/systemd/system/sirena.service
mv /etc/nginx/conf.d/sirena.conf /etc/nginx/conf.d/sirena.conf.save
cp /opt/SirenaSmith/configs/nginx/sirena.conf.example /etc/nginx/conf.d/sirena.conf
chown -R $GROUP:$GROUP /opt/SirenaSmith/
chown -R $GROUP:$GROUP /var/log/sirena/
chown -R $GROUP:$GROUP /etc/sirena/
nginx -t