from instabot import Bot
import re
import argparse

bot = Bot()
bot.login(username="cosmo_vibes2020", password="Zaq12wsx12345", ask_for_code=True)
user_id = bot.get_user_id_from_username("lego")
user_info = bot.get_user_info(user_id)




def get_media_id_from_url(insta_url):
    return bot.get_media_id_from_link(insta_url)


def get_media_comments(media_identificator):
    all_comments = bot.get_media_comments_all(media_identificator)
    return all_comments


def get_mentioned_friends(comm):
    match = re.findall(r'(?:@)([A-Za-z0-9_](?:'
                       r'(?:[A-Za-z0-9_]|(?:\.'
                       r'(?!\.))){0,28}'
                       r'(?:[A-Za-z0-9_]))?)',
                       comm['text']
                       )
    return match


def is_user_exist(mentioned_user):
    existing_user = bot.get_user_id_from_username(mentioned_user)
    return existing_user


def get_liked_users(id_media):
    return bot.get_media_likers(id_media)


url = 'https://www.instagram.com/p/B_nnz3gg7wj/'
media_id = get_media_id_from_url(url)
comments = get_media_comments(media_id)
print(comments)
successful_commentators = []
liked_users = set(get_liked_users(media_id))

for comment in comments:
    mentioned_friends = get_mentioned_friends(comment)
    for user in mentioned_friends:
        if is_user_exist(user):
            print('ok')
            successful_commentators.append((comment['user']['pk'], comment['user']['username']))
            break
print(len(successful_commentators))
for commentator in successful_commentators:
    if commentator[0] not in liked_users:
        successful_commentators.remove(commentator)
print(len(successful_commentators))


'''4110709400 1.khadzhimuradovich
21470092919 iskhakov.13
25471586854 magomedov___80
4161004016 1.abdulaevich
5348505961 1_ahmedovich'''