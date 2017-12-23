from mastodon import Mastodon
import pandas as pd
import datetime

if __name__ == "__main__":
    mastodon_cloud = Mastodon(
        client_id = "clientcred_cloud.secret",
        access_token = "usercred_cloud.secret",
        api_base_url = "https://gensokyo.cloud"
    )
    mastodon = Mastodon(
            client_id = "clientcred.secret",
            access_token = "usercred.secret",
            api_base_url = "https://gensokyo.town"
    )


#CSVからキャラクタ名ランダムに抽出し
df = pd.read_csv("charactor.csv")
sample_1 = df[df['label'] == 1].sample(3)
sample_2 = df[df['label'] == 2].sample(1)
sample = pd.concat([sample_1, sample_2])
del sample['label']
np_sample = sample.values

#今日の日付けを取得し、日を1つ進める
today = datetime.date.today() + datetime.timedelta(days=1)

#投稿する文章を作成、投稿
sent = "次回:" + str(today.month) + '月' + str(today.day) + "日のお題は\n"
for i in np_sample:
    sent += '・' + str(i) + '\n'
sent = sent.replace('[\'','')
sent = sent.replace('\']','')
sent += "です。各種投稿形式に応じて以下のタグを使い分けてくさだい。\n#幻想郷深夜のお絵描き一本勝負\n#幻想郷深夜の東方MMD一本勝負\n#幻想郷深夜の物書き一本勝負"

mastodon_cloud.toot(sent)
mastodon.toot(sent)
