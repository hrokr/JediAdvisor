import tweepy
import tokens.constants
from random import randint


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


def generate_saying(quotes_file_path, num_today):
    """
    Generates saying for the day
    """
    tags = "#StarWars, #TheCloneWars: #andor, #NAFO, #NAFOfellas, #Ukraine"
    with open(quotes_file_path) as f:
        for (num, saying) in enumerate(f):
            if num == num_today:
                return saying + tags


def get_keys():
    api_key = tokens.constants.API_KEY
    api_key_secret = tokens.constants.API_KEY_SECRET
    access_token = tokens.constants.ACCESS_TOKEN
    access_token_secret = tokens.constants.ACCESS_TOKEN_SECRET

    return (api_key, api_key_secret, access_token, access_token_secret)


def post_saying(api_key, api_key_secret, access_token, access_token_secret, saying):
    """
    Posts saying
    """
    print("Posting the following saying to JediAdvisor twitter account")
    print(saying)
    auth = tweepy.OAuthHandler(api_key, api_key_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True)
    api.update_status(saying)


if __name__ == "__main__":
    key_file_path = "tokens/constants.py"
    quotes_file_path = "../data/CloneWarsSayings.txt"

    num_lines = get_line_count(quotes_file_path)
    num_today = get_todays_number()
    saying = str(generate_saying(quotes_file_path, num_today))
    api_key, api_key_secret, access_token, access_token_secret = get_keys()

    post_saying(api_key, api_key_secret, access_token, access_token_secret, saying)
