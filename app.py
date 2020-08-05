from flask import Flask, render_template

# 初期化、templatesが同じディレクトリにあることをFlaskに知らせる
app = Flask(__name__)

# ルートデコレータ：index関数の実行を開始すべきURLを指定。
@app.route('/')

# index関数：first_app.htmlというHTMLファイル（templatesフォルダにある）を表示するだけ
def index():
    return render_template('first_app.html')

# このスクリプトがPythonインタプリタで直接実行された場合（if __name__ == '__main__':）
if __name__ == '__main__':
    # run()：使ってサーバー上のアプリケーションだけを実行
    app.run()