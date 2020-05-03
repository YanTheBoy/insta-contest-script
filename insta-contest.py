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


def get_user_followers(id_user):
    followers = bot.get_user_followers(id_user)
    return followers


def create_winners_set(contest_winners):
    winners = []
    for winner in contest_winners:
        winners.append(winner[1])
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
    media_id = get_media_id_from_url(post_url)
    comments = get_media_comments(media_id)

    successful_commentators = []
    for comment in comments:
        mentioned_friends = get_mentioned_friends(comment)
        for user in mentioned_friends:
            if is_user_exist(user):
                successful_commentators.append((comment['user']['pk'], comment['user']['username']))
                break

    liked_users = set(get_liked_users(media_id))
    for commentator in successful_commentators:
        if commentator[0] not in liked_users:
            successful_commentators.remove(commentator)

    user_followers = set(get_user_followers(user_id))
    for commentator in successful_commentators:
        if commentator[0] not in user_followers:
            successful_commentators.remove(commentator)

    print('Winners of the instagram contest: ')
    print(*create_winners_set(successful_commentators), sep=',')
