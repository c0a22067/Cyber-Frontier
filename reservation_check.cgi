#!/usr/bin/env python3
import cgi
import MySQLdb
import random
import os
from http.cookies import SimpleCookie
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

cookie_string = os.environ.get('HTTP_COOKIE', '')
cookie = SimpleCookie()
cookie.load(cookie_string)

def get_random(n):
    return ''.join(str(random.randrange(10)) for _ in range(n))

print("Content-Type: text/html\n")
html_content = f"""
<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<title><Cyber Frontier>アトラクション予約確認ページ</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="マイページ画面">
<link rel="stylesheet" href="./style.css">
</head>

<body>

<header>
<h1 id="logo"><a href="index.html"><img src="./logo.png" alt="Cyber Frontier"></a></h1>
</header>

<div id="container">

<nav id="header-menu">
<ul>
<li><a href="info.html">attraction<i class="fas fa-info-circle"></i></a></li>
<li><a href="shopping.html">shop<i class="fas fa-shopping-basket"></i></a></li>
<li><a href="event.html">event<i class="far fa-calendar-alt"></i></a></li>
<li><a href="access.html">mypage<i class="fas fa-map-marker-alt"></i></a></li>
</ul>
</nav>
"""

try:
    name = ""
    user_id = ""
    attraction = ""
    book_date = ""
    time = ""
    mail = ""
    book_id = ""
    f_login = -1
    session_id_s = ""

    for key, morsel in cookie.items():
        if key == "user_id":
            user_id = morsel.value
        elif key == "session_id":
            session_id_s = morsel.value

    connection = MySQLdb.connect(
        host='localhost',
        user='root',
        passwd='passwordA1!',
        db='booking',
        charset='utf8'
    )
    cursor = connection.cursor()

    # セッションIDのチェックとログイン状態の確認
    sql = f"SELECT session_id FROM Session WHERE user_id = '{user_id}'"
    cursor.execute(sql)
    rows = cursor.fetchall()
    session_id = ''
    for row in rows:
        session_id = row[0]
    if session_id == session_id_s:
        f_login = 0

    # ログイン状態が正常な場合、予約情報を取得
    if f_login == 0:
        cursor2 = connection.cursor()
        sql2 = f"SELECT * FROM booking_log WHERE user_id = '{user_id}'"
        cursor2.execute(sql2)
        rows2 = cursor2.fetchall()
        if rows2:
            html_content += f"""
            <main>
            <section style="text-align: center; padding: 20px; max-width: 600px; margin: auto; border: 1px solid #ccc; border-radius: 10px; background-color: #f9f9f9;">
            <h2><b><font color="#000033">アトラクション予約確認</font></b></h2>
            <hr style="border: 0; border-top: 1px solid #cccccc;">
            """
            for row2 in rows2:
                name = row2[2]
                attraction = row2[3]
                book_date = row2[4]
                book_id = row2[0]
                html_content += f"""
                <br>
                <font color="#000033">
                <p>予約ID: <strong>{book_id}</strong></p>
                <p>名前: <strong>{name}</strong></p>
                <p>アトラクション: <strong>{attraction}</strong></p>
                <p>予約時間: <strong>{book_date}</strong></p>
                <hr style="border: 0; border-top: 1px solid #cccccc;">
                </font> 
                """
            html_content += """
            <p style="color: red;">※予約時間の5分前までにアトラクションへお越しください。<br>
           ※予約のキャンセルは以下にお問い合わせください。</p>

            <a href="mailto:c0a22109e9@edu.teu.ac.jp" style="color: #007BFF; text-decoration: none; font-weight: bold;">お問い合わせ</a>
            </section>
            <br>
            <div style="text-align: center;">
            <br>
                <a href="mypage.cgi" style="color: #FFFFFF; text-decoration: none; font-weight: bold;">マイページへ</a>
                <br>
                <br>
                <a href="index.html" style="color: #FFFFFF; text-decoration: none; font-weight: bold;">トップページへ</a>
            </div>
            </main>
            <div id="footermenu">
            <ul>
            <li class="title">メニュー</li>
            <li><a href="index.html">ホーム</a></li>
            <li><a href="company.html">運営会社</a></li>
            <li><a href="info.html">施設のご案内</a></li>
            <li><a href="shopping.html">お買い物</a></li>
            <li><a href="event.html">イベント</a></li>
            <li><a href="access.html">アクセス</a></li>
            </ul>
            <ul>
            <li class="title">メニュー見出し</li>
            <li><a href="#">サンプルメニューサンプルメニュー</a></li>
            <li><a href="#">サンプルメニュー</a></li>
            <li><a href="#">サンプルメニュー</a></li>
            <li><a href="#">サンプルメニュー</a></li>
            </ul>
            <ul>
            <li class="title">メニュー見出し</li>
            <li><a href="#">サンプルメニューサンプルメニュー</a></li>
            <li><a href="#">サンプルメニュー</a></li>
            <li><a href="#">サンプルメニュー</a></li>
            <li><a href="#">サンプルメニュー</a></li>
            </ul>
            <ul>
            <li class="title">メニュー見出し</li>
            <li><a href="#">サンプルメニューサンプルメニュー</a></li>
            <li><a href="#">サンプルメニュー</a></li>
            <li><a href="#">サンプルメニュー</a></li>
            <li><a href="#">サンプルメニュー</a></li>
            </ul>
            </div>
            <!--/#footermenu-->

            <footer>
            <small>Copyright&copy; <a href="index.html">道の駅</a> All Rights Reserved.</small>
            <span class="pr"><a href="https://template-party.com/" target="_blank">《Web Design:Template-Party》</a></span>
            </footer>

            <!--開閉ブロック-->
            <div id="menubar">

            <nav>
            <ul>
            <li><a href="index.html">ホーム</a></li>
            <li><a href="info.html">施設のご案内</a></li>
            <li><a href="shopping.html">お買い物</a></li>
            <li><a href="event.html">イベント</a></li>
            <li><a href="access.html">アクセス</a></li>
            </ul>
            </nav>
            </div>
            <!--/開閉ブロック-->
            </body>
            </html>
            """
        else:
            html_content += "<p>予約情報が見つかりませんでした。</p>"

    else:
        html_content += "<p>ログインしていません。</p>"

except Exception as e:
    html_content += f"<p>エラーが発生しました: {str(e)}</p>"

finally:
    if 'connection' in locals():
        connection.close()

print(html_content)
