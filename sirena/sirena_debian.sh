virtualenv -p /usr/bin/python3 venv
source venv/bin/activate
venv/bin/pip3 install -r requirements.txt
deactivate
mkdir /etc/sirena
mkdir /var/log/sirena
mv /etc/sirena/sirena.yaml /etc/sirena/sirena.yaml.save
cp /opt/SirenaSmith/sirena/sirena.yaml.example /etc/sirena/sirena.yaml
cp /opt/SirenaSmith/configs/systemd/sirena.service.example /etc/systemd/system/sirena.service
mv /etc/nginx/conf.d/sirena.conf /etc/nginx/conf.d/sirena.conf.save
cp /opt/SirenaSmith/configs/nginx/sirena.conf.example /etc/nginx/conf.d/sirena.conf
chown -R www-data:www-data /opt/SirenaSmith/
chown -R www-data:www-data /var/log/sirena/
chown -R www-data:www-data /etc/sirena/