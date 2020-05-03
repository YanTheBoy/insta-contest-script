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
2020-05-03 19:38:27,251 - INFO - Instabot version: 0.117.0 Started
2020-05-03 19:38:27,267 - INFO - Recovery from /home/elijah/Documents/projects/insta-contest-script/config/cosmo_vibes2020_uuid_and_cookie.json: COOKIE True - UUIDs True - TIMING, DEVICE and ...
- user-agent=Instagram 117.0.0.28.123 Android (28/9.0; 420dpi; 1080x1920; OnePlus; ONEPLUS A3003; OnePlus3; qcom; en_US; 180322800)
2020-05-03 19:38:32,161 - INFO - Logged-in successfully as 'username'!
636
Getting followers of 9467967026: 17894it [01:10, 252.57it/s]
Winners of the instagram contest: 
__devotion_1,vacok221,shama_lokot,axmedow444,sofitik07,awen1002,columbiec_01,_ibragimov500_,ahmed_asadulaev,ocmanovvv.official,magomedov.303,islam00768,xamza.60,magomedbegov13,vazi.20,davud0518,_alkhamatov,_z_a_m_i_r_500
```
# Project Goals
The code is written for educational purposes on online-course for web-developers [DEVMAN.org](https://devman.org)
