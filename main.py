from all_telegram_post import all_post_telegram
from icecream import ic


ic.configureOutput(includeContext=True)


if __name__ == '__main__':
    ic(all_post_telegram(limit=10))