echo -e "DONE\nObfuscating pysel.py..."
pyarmor obfuscate --recursive --output /usr/local/bin/pysel/ score.py
chown $cpuser:$cpuser /usr/local/bin/pysel

echo -e 'DONE\nCreating /pysel-static directory...'
mkdir -p /pysel-static
cp static/*.png /pysel-static/
cp static/*.wav /pysel-static/

echo -e 'DONE\nCreating Team ID Changer...'
chmod 777 /usr/local/bin/
echo 'Skills Contestant' > /usr/local/bin/pysel/TEAM

echo 'Ubuntu 16.04 - Using systemd'
cp static/pysel_scoring.service /etc/systemd/system/
systemctl enable pysel_scoring.service
systemctl start pysel_scoring.service
