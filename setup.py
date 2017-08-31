#! -*- coding: utf-8 -*-

from mastodon import Mastodon

url = "https://gensokyo.cloud"

Mastodon.create_app("application name",
    api_base_url = url,
    to_file = "cred.txt"
)

mastodon = Mastodon(
    client_id = "cred.txt",
    api_base_url = url
)

mastodon.log_in(
    "****",
    "****",
    to_file = "auth.txt"
)
