## setup instructions for cloud9

* log in to the AWS console using the link in the Event Engine dashboard
* Navigate to the Cloud9 Service and create a new environment (select m4.large instance type)
* connect to cloud9, open preferences, and disable "AWS managed temporary credentials" 
under Preferences -> AWS Settings -> Credentials
* Open a terminal
* paste in linux credentials from the Event Engine dashboard
* Install taskcat:
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py --user
sudo rm /usr/bin/pip
pip install taskcat --user
```
* get lab assets:
```
git clone https://github.com/taskcat/workshop.git
cp -r workshop/content/lab_assets/start/* ./ 
rm -rf workshop
sudo ln -s ./ /workshop
```
