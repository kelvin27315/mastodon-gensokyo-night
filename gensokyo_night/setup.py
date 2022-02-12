from os import path

from mastodon import Mastodon

"""
アプリケーションの登録とアカウントへの認証を行う
"""
PATH = path.dirname(path.abspath(__file__)) + "/"


def create_app(file_name: str, api_url: str) -> None:
    """
    アプリケーションを登録する
    """
    Mastodon.create_app(
        client_name="mastodon-gensokyo-night",
        scopes=["write"],
        website="https://github.com/kelvin27315/mastodon-gensokyo-night",
        to_file=PATH + file_name,
        api_base_url=api_url,
    )


def log_in(
    client_file_neme: str, api_url: str, mail: str, password: str, user_file_name: str
) -> None:
    """
    アカウントの認証を通す
    """
    mastodon = Mastodon(client_id=PATH + client_file_neme, api_base_url=api_url)
    mastodon.log_in(mail, password, scopes=["write"], to_file=PATH + user_file_name)


if __name__ == "__main__":
    # gensokyo.town
    create_app("clientcred.secret", "https://gensokyo.town")
    log_in(
        "clientcred.secret",
        "https://gensokyo.town",
        "*****@example.com",
        "*****",
        "usercred.secret",
    )
