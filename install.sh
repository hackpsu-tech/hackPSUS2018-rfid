#!/bin/bash

DIR=/usr/local/src

git clone git@github.com:hackpsu-tech/hackPSUS2018-rfid.git $DIR

SERVICE=/lib/systemd/system/rfid.service


echo "[Unit]
Description=RFID scanning application
After=multi-user.target

[Service]
Type=simple
ExecStart=/usr/bin/bash $DIR/wrapper.sh
WorkingDirectory=$PWD

[Install]
WantedBy=multi-user.target" > $SERVICE

chmod 644 $SERVICE

echo "#!/bin/bash
git pull origin master

python app.py" > $DIR/wrapper.sh

systemctl daemon-reload
systemctl enable rfid.service
systemctl start rfid.service


