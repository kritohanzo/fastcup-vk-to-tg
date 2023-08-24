#!/bin/sh
cd ..
pip install -r requirements.txt
cp systemd/script.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable script.service
sudo systemctl start script.service