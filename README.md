# insta-contest-script
The simple script for instagram contest. Based on Instabot
# How to install
Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:
```bash
$ pip install -r requirements.txt
```
Create .env file in local folder and put there your instagram account login and password.
```text
INSTAGRAM_LOGIN=insta_login
INSTAGRAM_PASSWORD=insta_password
```
Run insta-contest.py for getting winners with 'contest url' and 'username' parameters:
```bash
$ python3 insta-contest.py https://www.instagram.com/p/B_nnz3gg7wj/ djakam_style
Contest winners: 
```


# Project Goals
The code is written for educational purposes on online-course for web-developers [DEVMAN.org](https://devman.org)
