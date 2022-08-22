import os

# import schedule
# jimport time
import tweepy
from random import sample, randint


def get_keys():
    keys = open("../tokens/jedi_tokens.txt", "r").read().splitlines()

    return keys


def get_line_count(file) -> int:
    """
    Calculates the number of lines in file.
    """

    with open(file) as f:
        line_count = sum(1 for _ in f)
    return line_count


def get_todays_number():
    """
    Generates random number for today
    """
    todays_num = randint(0, 128)
    return todays_num


def get_todays_saying(num_today):
    """
    Generates saying for the day
    """
    with open(file) as f:
        for (num, saying) in enumerate(f):
            if num == num_today:
                print(saying)


"""
 def authenticate(api_key, api_key_secret, access_token, access_token_secret, saying):
    Authenticates identity to Twitter

    auth = tweepy.OAuthHandler(api_key, api_key_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True)
    api.update_status(saying)
"""


def post_saying(api, saying):
    """
    Posts saying
    """
    pass


"""
def job():
    print("I'm working...")

    schedule.every(2).minutes.do(job)
    # schedule.every().hour.do(job)
    # schedule.every().day.at("10:30").do(job)

    while 1:
        schedule.run_pending()
        time.sleep(1)
"""


if __name__ == "__main__":
    file = "../data/CloneWarsSayings.txt"

    num_lines = get_line_count(file)
    print(f"There are {num_lines} sayings in the file")

    num_today = get_todays_number()
    saying = get_todays_saying(num_today)

    keys = get_keys()

    api_key = keys[0]
    api_key_secret = keys[1]
    access_token = keys[2]
    access_token_secret = keys[3]

    print(keys[0])

    auth = tweepy.OAuthHandler(api_key, api_key_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True)
    api.update_status(saying)
    # authenticate(api_key, api_key_secret, access_token, access_token_secret, saying)
    # post_saying(api, saying)
