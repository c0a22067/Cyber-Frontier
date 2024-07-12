#!/usr/bin/env python3

import cgi
import MySQLdb
import random
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from http.cookies import SimpleCookie
import smtplib

def get_random(n):
    return ''.join(str(random.randrange(10)) for _ in range(n))

print("Content-Type: text/html\n")

try:
    form = cgi.FieldStorage()
    name = form.getvalue('name')
    user_id = form.getvalue('user_id')
    attraction = form.getvalue('attraction')
    book_date = form.getvalue('book_date')
    time = form.getvalue('time')
    mail = form.getvalue('mail')
    book_id = get_random(5)

    connection = MySQLdb.connect(
        host='localhost',
        user='user1',
        passwd='passwordA1!',
        db='booking',
        charset='utf8'
    )
    cursor = connection.cursor()
		
    sql = "INSERT INTO booking_log (book_id, user_id, name, attraction, book_date) VALUES ('" + book_id + "', '" + user_id + "', '" + name + "', '" + attraction + "', '" + time + "')"
    cursor.execute(sql)
    connection.commit()

    # メール送信設定
    
    to = mail
    subject = 'Cyber-Frontier <アトラクション予約確認>'
    message = f"""
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>予約確認</title>
</head>
<body style="font-family: Arial, sans-serif; background-color: #f4f4f4; margin: 0; padding: 0;">
    <table width="100%" border="0" cellspacing="0" cellpadding="0">
        <tr>
            <td style="padding: 20px 0;">
                <table width="600" border="0" cellspacing="0" cellpadding="20" style="background-color: #ffffff; margin: auto; border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.1);">
                    <tr>
                        <td style="text-align: center;">
                            <h1 style="color: #333333;">予約確認</h1>
                            <hr style="border: 0; border-top: 1px solid #cccccc;">
                            <p style="color: #555555;">予約ID: <strong>{book_id}</strong></p>
                            <p style="color: #555555;">名前: <strong>{name}</strong></p>
                            <p style="color: #555555;">アトラクション: <strong>{attraction}</strong></p>
                            <p style="color: #555555;">予約時間: <strong>{time[:16]}</strong></p>
                            <hr style="border: 0; border-top: 1px solid #cccccc;">
                            <p style="color: #e74c3c;">※予約時間の5分前までにアトラクションへお越しください。</p>
                            <p style="color: #e74c3c;">※予約のキャンセルは以下にお問い合わせください。</p>
                            <a href="mailto:c0a22109e9@edu.teu.ac.jp" style="color: #3498db; text-decoration: none; font-weight: bold;">お問い合わせ</a>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>

    """

    msg = MIMEMultipart()
    msg['From'] = 'Cyber-Frontier@virtual-machine'
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'html'))

    # SMTPサーバに接続してメール送信
    server = smtplib.SMTP('localhost')
    server.send_message(msg)
    server.quit()

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

<main>

<section style="text-align: center; padding: 20px; max-width: 600px; margin: auto; border: 1px solid #ccc; border-radius: 10px; background-color: #f9f9f9;">
    <h2><b><font color="#000033">アトラクション予約確認</font></b></h2>
    <hr style="border: 0; border-top: 1px solid #cccccc;">
    <br>
    <font color="#000033">
    <p>予約ID: <strong>{book_id}</strong></p>
    <p>名前: <strong>{name}</strong></p>
    <p>アトラクション: <strong>{attraction}</strong></p>
    <p>予約時間: <strong>{time[:16]}</strong></p>
    <hr style="border: 0; border-top: 1px solid #cccccc;">
    <p>確認メールが <strong>{to}</strong> に送信されました。</p>
    </font>
    <p style="color: red;">※予約時間の5分前までにアトラクションへお越しください。<br>
    ※ブラウザの戻る・再読込ボタンは使用しないでください。<br>
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

<p class="btn"><a href="contact.html">お問い合わせ</a></p>

<div class="sh">
<p>※900px未満のメニュー開閉時にのみ表示させたい情報があればここ（shボックスの中）に入れて下さい。<br>
サンプルテキスト。サンプルテキスト。<br>
サンプルテキスト。サンプルテキスト。<br>
サンプルテキスト。サンプルテキスト。</p>
</div>
<!--/.sh-->

</div>
<!--/#menubar-->

<!--開閉ボタン（ハンバーガーアイコン）-->
<div id="menubar_hdr">
<div>
<span></span><span></span><span></span>
</div>
<p>MENU</p>
</div>

</div>
<!--/#container-->

<!--jQueryの読み込み-->
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>

<!--パララックス（inview）-->
<script src="https://cdnjs.cloudflare.com/ajax/libs/protonet-jquery.inview/1.1.2/jquery.inview.min.js"></script>
<script src="js/jquery.inview_set.js"></script>

<!--このテンプレート専用のスクリプト-->
<script src="js/main.js"></script>

<!--ページの上部へ戻るボタン-->
<div class="pagetop"><a href="#"><i class="fas fa-angle-double-up"></i></a></div>

</body>
</html>
    """
    print(html_content.encode("utf-8", 'ignore').decode('utf-8'))

except MySQLdb.Error as e:
    print(f"<html><body><h1>データベースエラー</h1><p>{e}</p></body></html>")
except smtplib.SMTPException as e:
    print(f"<html><body><h1>メール送信エラー</h1><p>{e}</p></body></html>")
except Exception as e:
    print(f"<html><body><h1>一般エラー</h1><p>{e}</p></body></html>")
finally:
    if 'connection' in locals():
        connection.close()

