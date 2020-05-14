from instabot import Bot
import re
import argparse
from dotenv import load_dotenv
import os


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='Enter url of instagram post')
    parser.add_argument('nickname', help='Enter nickname of instagram account')
    return parser.parse_args()


def get_mentioned_friends(comm):
    pattern = re.compile(r'''
                (?:@) ([A-Za-z0-9_](?:
                (?:[A-Za-z0-9_]|
                (?:\.(?!\.))){0,28}
                (?:[A-Za-z0-9_]))?)
              ''', re.X)
    match = re.findall(pattern, comm['text'])
    return match


def get_winners_names(contest_winners):
    winners = [name for __, name in contest_winners]
    return set(winners)


if __name__ == '__main__':
    load_dotenv()
    username = os.getenv('INSTAGRAM_LOGIN')
    password = os.getenv('INSTAGRAM_PASSWORD')
    bot = Bot()
    bot.login(username=username, password=password, ask_for_code=True)
    user_nickname = parse_args().nickname
    post_url = parse_args().url

    user_id = bot.get_user_id_from_username(user_nickname)
    media_id = bot.get_media_id_from_link(post_url)
    comments = bot.get_media_comments_all(media_id)

    successful_commentators = set()
    for comment in comments:
        mentioned_friends = get_mentioned_friends(comment)
        for user in mentioned_friends:
            if bot.get_user_id_from_username(user):
                successful_commentators.add((comment['user']['pk'], comment['user']['username']))
                break
    liked_users = set(bot.get_media_likers(media_id))
    successful_commentators = {(user_id, __) for user_id, __ in successful_commentators if str(user_id) in liked_users}

    followers = set(bot.get_user_followers(user_id))
    successful_commentators = {(user_id, __) for user_id, __ in successful_commentators if str(user_id) in followers}

    print('Winners of the instagram contest: ')
    print(*get_winners_names(successful_commentators), sep=',')
