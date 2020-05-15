cd /opt/
sudo git clone https://github.com/crow1011/SirenaSmith.git
cd SirenaSmith/sirena/
sudo virtualenv -p /usr/bin/python3 venv
source venv/bin/activate
sudo venv/bin/pip3 install -r requirements.txt
sudo mv sirena.yaml.example sirena.yaml

sudo mkdir /var/log/sirena
sudo chown -R www-data:www-data /opt/SirenaSmith/
sudo chown -R www-data:www-data /var/log/sirena/