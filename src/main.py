import tokens.constants
from random import sample, randint

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
    with open(quotes_file_path) as f:
        for (num, saying) in enumerate(f):
            if num == num_today:
                print(saying)


def parse_keys(keys):
    api_key = API_key
    api_key_secret = keys[1]
    access_token = keys[2]
    access_token_secret = keys[3]
    print(api_key)
    return(api_key, api_key_secret, access_token, access_token_secret)


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
    # schedule.every().day.at("10:30").do(job)lck

    while 1:
        schedule.run_pending()
        time.sleep(1)
"""


if __name__ == "__main__":
    key_file_path = "tokens/constants.py"
    quotes_file_path = "../data/CloneWarsSayings.txt"
    num_lines = get_line_count(quotes_file_path)

    num_today = get_todays_number()

    saying = generate_saying(quotes_file_path, num_today)
'''
    api_key = tokens.constants.API_KEY
    api_key_secret = tokens.constants.API_KEY_SECRET
    access_token = tokens.constants.ACCESS_TOKEN
    access_token_secret = tokens.constants.ACCESS_TOKEN_SECRET

    print('now to parse the keys')
    auth = tweepy.OAuthHandler(api_key, api_key_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True)
    api.update_status(saying)
    # authenticate(api_key, api_key_secret, access_token, access_token_secret, saying)
    # post_saying(api, saying)
'''
