from mastodon import Mastodon

"""
アプリケーションの登録とアカウントへの認証を行う
"""

if __name__ == "__main__":
    #gensokyo.cloud
    Mastodon.create_app("gensokyo night",
        api_base_url = "https://gensokyo.cloud",
        to_file = "clientcred_cloud.secret"
    )

    mastodon = Mastodon(
        client_id = "clientcred_cloud.secret",
        api_base_url = "https://gensokyo.cloud"
    )

    mastodon.log_in(
        "*****@example.com", "****",
        to_file = "usercred.secret"
    )

    #gensokyo.town
    Mastodon.create_app("gensokyo night",
        api_base_url = "https://gensokyo.town",
        to_file = "clientcred.secret"
    )

    mastodon = Mastodon(
        client_id = "clientcred.secret",
        api_base_url = "https://gensokyo.town"
    )

    mastodon.log_in(
        "*****@example.com", "*****",
        to_file = "usercred.secret"
    )
