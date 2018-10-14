# python3 setup
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.bash_profile
echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
source ~/.bash_profile
pyenv install 3.6.6
pyenv global 3.6.6
pyenv rehash
pip install --upgrade pip
pip install pytest
## aws-sam-cli install
pip install aws-sam-cli

# httpd.conf
sudo cp /home/vagrant/dev/centos72/local.conf /etc/httpd/conf.d/
sudo systemctl restart httpd

# nodejs setup
curl -L git.io/nodebrew | perl - setup
echo 'export PATH=$HOME/.nodebrew/current/bin:$PATH' >> ~/.bash_profile
source ~/.bash_profile
nodebrew install-binary v10.9.0
nodebrew use v10.9.0

# DynamoDB setup
mkdir ~/dynamo
cd ~/dynamo
wget https://s3-ap-northeast-1.amazonaws.com/dynamodb-local-tokyo/dynamodb_local_latest.tar.gz
tar -zxvf dynamodb_local_latest.tar.gz
rm dynamodb_local_latest.tar.gz
## aaronshaf/dynamodb-admin install
npm install dynamodb-admin -g