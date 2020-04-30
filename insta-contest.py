from instabot import Bot
import re

bot = Bot()
bot.login(username="cosmo_vibes2020", password="Zaq12wsx12345", ask_for_code=True)
user_id = bot.get_user_id_from_username("lego")
user_info = bot.get_user_info(user_id)


def get_media_id_from_url(insta_url):
    return bot.get_media_id_from_link(insta_url)


def get_media_comments(media_id):
    comments = bot.get_media_comments_all(media_id)
    return comments


def get_mantioned_friends(comm):
    match = re.findall(r'(?:@)([A-Za-z0-9_](?:'
                       r'(?:[A-Za-z0-9_]|(?:\.'
                       r'(?!\.))){0,28}'
                       r'(?:[A-Za-z0-9_]))?)',
                       comment['text']
                       )
    return match


def is_user_exist(users):
    for user in users:
        user_id = Bot.get_user_id_from_username(user)
        print(user_id)  # true or false

url = 'https://www.instagram.com/p/B_nhd7MBb8F/'
media_id = get_media_id_from_url(url)
comments = get_media_comments(media_id)
for comment in comments:
    pass
mentioned_friends = get_mantioned_friends(comments)
for friends in mentioned_friends:

exist_users = is_user_exist()