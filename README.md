# mastodon-gensokyo-night

Mastodonの東方インスタンス[gensokyo.town](https://gensokyo.town)で動いているbot、幻想郷深夜の創作一本勝負([@gensokyo_night@gensokyo.town](https://gensokyo.town/@gensokyo_night))のプログラムです。

動いてた（インスタンス: gensokyo.cloud), アカウント: @gensokyo_night[at]gensokyo.cloud）

## 企画について

投稿する形式に応じて[#幻想郷深夜のお絵描き一本勝負, #幻想郷深夜の東方MMD一本勝負, #幻想郷深夜の物書き一本勝負]のタグを使い分けて投稿してください。</br>
作品の制作時間についての決まりは無く、どのくらいの時間をかけて製作しても構いませんし、いつ投稿しても構いません。


## 環境
- パッケージ管理ツール
  - [Poetry](https://python-poetry.org/)
- 言語
  - Python
- lint/format
  - [pysen](https://github.com/pfnet/pysen)
- 実行環境 & CI環境
  - GitHub Actions

### 依存パッケージ install
```shell
poetry install
```

### Test
```shell
# poetry環境に入っている場合
python -m unittest
# poetry環境に入っていない場合
poetry run python -m unittest
```

### Python lint/format
#### Python lint
```shell
# poetry環境に入っている場合
pysen run lint
# poetry環境に入っていない場合
poetry run pysen run lint
```

#### Python format
```shell
# poetry環境に入っている場合
pysen run format
# poetry環境に入っていない場合
poetry run pysen run format
```
