import unittest
from datetime import date, timedelta
from unittest.mock import Mock

import mastodon
import pandas as pd
from gensokyo_night import gensokyo_night as gn

TOMORROW_STR = "{dt.month}月{dt.day}日".format(dt=date.today() + timedelta(days=1))


class TestGensokyoNight(unittest.TestCase):
    def setUp(self) -> None:
        # gn.mastodon をmockするので、元のが定義されていたら退避
        self.original_mastodon = gn.mastodon if hasattr(gn, "mastodon") else None
        gn.mastodon = Mock(spec=mastodon.Mastodon)

    def tearDown(self) -> None:
        gn.mastodon = self.original_mastodon

    def test_sample_characters(self) -> None:
        characters = pd.DataFrame(
            {
                "name": [
                    "博麗 靈夢 (旧作)",
                    "霧雨 魔理沙 (旧作)",
                    "十六夜 咲夜",
                    "魂魄 妖夢",
                    "東風谷 早苗",
                    "稗田 阿求",
                ],
                "label": [2, 2, 1, 1, 1, 1],
            }
        )
        character_names = gn.sample_characters(characters)
        self.assertEqual(4, len(character_names))

    def test_post_toot(self) -> None:
        gn.post_toot(["霧雨 魔理沙", "十六夜 咲夜", "魂魄 妖夢", "博麗 靈夢 (旧作)"])
        gn.mastodon.toot.assert_called_once_with(
            "次回:"
            + TOMORROW_STR
            + "のお題は\n"
            + "・霧雨 魔理沙\n"
            + "・十六夜 咲夜\n"
            + "・魂魄 妖夢\n"
            + "・博麗 靈夢 (旧作)\n"
            + "です。各種投稿形式に応じて以下のタグを使い分けてくさだい。\n"
            + "#幻想郷深夜のお絵描き一本勝負\n"
            + "#幻想郷深夜の東方MMD一本勝負\n"
            + "#幻想郷深夜の物書き一本勝負"
        )
