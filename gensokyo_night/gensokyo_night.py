import datetime
from os import environ, path
from typing import List

import pandas as pd
from mastodon import Mastodon

PATH = path.dirname(path.abspath(__file__))
if __name__ == "__main__":
    user_cred = environ.get("USER_CRED")
    mastodon = Mastodon(
        access_token=user_cred,
        api_base_url="https://gensokyo.town",
    )


def read_csv(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(PATH + file_path)
    return df


def sample_characters(df: pd.DataFrame) -> List[str]:
    """pd.DataFrameからキャラクタ名ランダムに抽出"""
    sample_1 = df[df["label"] == 1].sample(3)
    sample_2 = df[df["label"] == 2].sample(1)
    samples = pd.concat([sample_1, sample_2])
    character_names: List[str] = samples["name"].tolist()
    return character_names


def post_toot(np_sample: List[str]) -> None:
    """投稿する文章を作成、投稿"""
    today = datetime.date.today() + datetime.timedelta(days=1)

    text = "次回:" + str(today.month) + "月" + str(today.day) + "日のお題は\n"
    for i in np_sample:
        text += "・" + str(i) + "\n"
    text += "です。各種投稿形式に応じて以下のタグを使い分けてくさだい。\n#幻想郷深夜のお絵描き一本勝負\n#幻想郷深夜の東方MMD一本勝負\n#幻想郷深夜の物書き一本勝負"

    mastodon.status_post(text)


def main() -> None:
    file_path = "/../character.csv"
    characters = read_csv(file_path)
    character_names = sample_characters(characters)
    post_toot(character_names)


if __name__ == "__main__":
    main()
