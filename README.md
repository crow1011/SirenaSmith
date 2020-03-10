-------------
Sirena в статусе разработки. Стабильной версии пока нет
-------------

Sirena - это масшстабируемая система оповещения из разных источников.
Главная цель sirena - создание гибкой и надежной системы оповещения.
Sirena
-------------
Sirena может принимать данные:

-  Агентной отправкой;

- HTTP POST

- TCP/UDP(планируется);

Sirena собрана из:


- Python3;

- Flask;

- virtualenv;

- Gunicorn;

- Nginx;

- systemd.

Install Sirena
-------------

    cd /opt
    sudo git clone https://github.com/crow1011/SirenaSmith.git
    cd SirenaSmith/
    sudo cp sirena.conf.example sirena.conf
    sudo virtualenv -p /usr/bin/python3 venv
    cd /opt/SirenaSmith/venv/bin
    sudo ./pip3 install -r ../../requirements.txt
    sudo chown -R www-data:www-data /opt/SirenaSmith/



Systemd sirena service
-------------

    sudo nano /etc/systemd/system/sirena.service

и вставить этот конфиг:

    [Unit]
    Description=Gunicorn instance to serve sirena
    After=network.target


    [Service]
    User=www-data
    Group=www-data
    WorkingDirectory=/opt/SirenaSmith
    Environment="PATH=/opt/SirenaSmith/venv/bin"
    ExecStart=/opt/SirenaSmith/venv/bin/gunicorn --workers 3 --bind unix:sirena.sock -m 007 wsgi:app

    [Install]
    WantedBy=multi-user.target
после этого:

    systemctl enable sirena
    systemctl daemon-reload
Nginx conf
-------------
sudo nano /etc/nginx/conf.d/sirena.conf
и вставить этот конфиг:

    upstream sirena {
    server unix:/opt/SirenaSmith/sirena.sock;}

    server {
    listen       80;
    server_name  srv1.sirena.lab;

    location / {
      proxy_pass      http://sirena;}
    }

__server_name__ - это адрес, который будет указан агенту для отправки. Изменяйте это значение по своему усмотрению.

Config Sirena Srv
-------------
Отредактируйте /opt/SirenaSmith/sirena.conf

    [server]
    token = 123456 - токен для подтверждения агента. Токен установленный у агентов должен быть 
    аналогичным. Из этого токена будет вычислен md5 hash и сверен с md5 hash, который прислал агент.

    ip = 127.0.0.1 - оставить как есть, параметр пропадет в будующих версиях. sirenasrv работает на 
    socket.
    port = 5000 - оставить как есть, параметр пропадет в будующих версиях. sirenasrv работает на socket.

    [tg]
    bottoken = указать токен бота ТГ.

    chatid = указать ваш  tg chatid. для запроса chat_id можно:
    cd /opt/SirenaSmith
    source venv/bin/activate
    python3 TGetchatid.py
    Это простой слушатель отвечающий на команду /start вашим chat_id
    когда получите chat_id:
    deactivate

    [proxy]
    для неудачников предусмотрено использование tor-proxy для tg-bot
    proxy=True
    ip = 127.0.0.1
    port = 9050






Install sirena-agent zabbix
-------------
отредактируйте /opt/SirenaSmith/clients/zabbix/srnzabbix.conf
скопируйте /opt/SirenaSmith/clients/zabbix/* в папку с zabbix-скриптами
настройте действие на zabbix
агент принимает 1 параметр - само сообщение. 

для запуска 

    service sirena start



