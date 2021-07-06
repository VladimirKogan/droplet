git clone https://github.com/VladimirKogan/droplet.git
sudo mv droplet/twitter.py .
sudo mv droplet/tg.py .
sudo mv droplet/bot.py .
sudo apt-get update
sudo apt-get install -y unzip xvfb libxi6 libgconf-2-4
sudo apt-get install -y default-jdk
sudo curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add
sudo echo "deb [arch=amd64]  http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
sudo apt-get -y update
sudo apt-get -y install google-chrome-stable
sudo mkdir drivers
cd drivers
sudo mkdir driver241
sudo mkdir driver242
sudo mkdir driver243
sudo mkdir driver244
sudo mkdir driver245
sudo mkdir driver246
cd
wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
sudo mv chromedriver drivers/driver241/chromedriver
sudo chown root:root drivers/driver241/chromedriver
sudo chmod +x drivers/driver241/chromedriver
sudo rm chromedriver_linux64.zip

wget https://chromedriver.storage.googleapis.com/2.42/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
sudo mv chromedriver drivers/driver242/chromedriver
sudo chown root:root drivers/driver242/chromedriver
sudo chmod +x drivers/driver242/chromedriver
sudo rm chromedriver_linux64.zip

wget https://chromedriver.storage.googleapis.com/2.43/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
sudo mv chromedriver drivers/driver243/chromedriver
sudo chown root:root drivers/driver243/chromedriver
sudo chmod +x drivers/driver243/chromedriver
sudo rm chromedriver_linux64.zip

wget https://chromedriver.storage.googleapis.com/2.44/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
sudo mv chromedriver drivers/driver244/chromedriver
sudo chown root:root drivers/driver244/chromedriver
sudo chmod +x drivers/driver244/chromedriver
sudo rm chromedriver_linux64.zip

wget https://chromedriver.storage.googleapis.com/2.45/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
sudo mv chromedriver drivers/driver245/chromedriver
sudo chown root:root drivers/driver245/chromedriver
sudo chmod +x drivers/driver245/chromedriver
sudo rm chromedriver_linux64.zip

wget https://chromedriver.storage.googleapis.com/2.46/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
sudo mv chromedriver drivers/driver246/chromedriver
sudo chown root:root drivers/driver246/chromedriver
sudo chmod +x drivers/driver246/chromedriver
sudo rm chromedriver_linux64.zip
sudo apt install -y python3-pip
pip3 install selenium
pip3 install telebot
python3 twitter.py 'elonmusk' 3
