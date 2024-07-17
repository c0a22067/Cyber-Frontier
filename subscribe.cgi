#!/usr/bin/python3

import cgi
import crypt
import os
import MySQLdb
from http import cookies
import random
import string
from PIL import Image
import io

form = cgi.FieldStorage()
user_name = form.getfirst('user_name')
mail_address = form.getfirst('mail_address')
password = form.getfirst('password')
phone_number = form.getfirst('phone_number')
face_pict_file = form['face_pict']

def get_random_str(n):
    char_data = string.digits + string.ascii_lowercase + string.ascii_uppercase
    return ''.join([random.choice(char_data) for i in range(n)])

# バイナリーデータとしてファイルを読み込む
face_pict_binary = face_pict_file.file.read()

# バイナリーデータを画像に変換
image = Image.open(io.BytesIO(face_pict_binary))

hashed_password = ''

cpass = ''
salt = crypt.mksalt(method=crypt.METHOD_BLOWFISH)
if(password != None and salt != ''):
    cpass = crypt.crypt(password, salt)

connection = MySQLdb.connect(
    host='localhost',
    user='user1',
    passwd='passwordA1!',
    db='booking',
    charset='utf8'
)

cursor = connection.cursor()
sql = "INSERT INTO User_data (name, password, phone_number, mail_address, face_pict) VALUES (%s, %s, %s, %s, %s)"
values = (user_name, cpass, phone_number, mail_address, face_pict_binary)

cursor.execute(sql, values)
connection.commit()

sql = "SELECT user_id FROM User_data WHERE name = %s"
cursor.execute(sql, (user_name,))
rows = cursor.fetchall()

user_id = str(rows[0][0])

connection.close()

session_id = get_random_str(64)

connection = MySQLdb.connect(
    host='localhost',
    user='user1',
    passwd='passwordA1!',
    db='booking',
    charset='utf8'
)

cursor = connection.cursor()

sql = "INSERT INTO Session (`user_id`, `session_id`) VALUES (%s, %s) ON DUPLICATE KEY UPDATE session_id = %s"
cursor.execute(sql, (user_id, session_id, session_id))

connection.commit()

# レスポンスのヘッダーとHTMLの出力
print("Content-Type: text/html")
print("Set-Cookie: user_id=" + user_id)
print("Set-Cookie: session_id=" + session_id)
print()

# HTMLを出力
print('<!DOCTYPE HTML>')
print('<html lang="ja">')
print('<head>')
print('<meta charset="UTF-8">')
print('<title>登録完了｜Cyber Frontier</title>')
print('<meta name="viewport" content="width=device-width, initial-scale=1">')
print('<meta name="description" content="Cyber Frontierの登録完了ページです">')
print('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/vegas/2.5.4/vegas.min.css">')
print('<link rel="stylesheet" href="css/style.css">')
print('</head>')
print('<body>')

print('<header>')
print('<h1 id="logo"><a href="index.html"><img src="images/CF_logo.PNG" alt="遊園地"></a></h1>')
print('<ul id="lang-nav">')
print('<li><a href= "login.html">ログイン</a></li>')
print('<li><a href="mypage.cgi">マイページ</a></li>')
print('</ul>')
print('</header>')

print('<div id="container">')

print('<nav id="header-menu">')
print('<ul>')
print('<li><a href="attraction1_hp.cgi">attraction<i class="fas fa-info-circle"></i></a></li>')
print('<li><a href="shopping.html">shop<i class="fas fa-shopping-basket"></i></a></li>')
print('<li><a href="event.html">event<i class="far fa-calendar-alt"></i></a></li>')
print('<li><a href="mypage.cgi">mypage<i class="fas fa-map-marker-alt"></i></a></li>')
print('</ul>')
print('</nav>')

print('<main>')

print('<section>')
print('<center>')
print('<div id="wrapper">')
print('登録しました。<br>')
print('<form action="mypage.cgi" method="post">')
print('<button type="submit">続ける</button>')
print('<input type="hidden" name="user_name" value="{}">'.format(user_name))
print('<input type="hidden" name="session_id" value="{}">'.format(session_id))
print('</form>')
print('</div>')
print('</center>')
print('</section>')

print('</main>')

print('<div id="footermenu">')
print('<ul>')
print('<li class="title">メニュー</li>')
print('<li><a href="index.html">Home</a></li>')
print('<li><a href="company.html">Company</a></li>')
print('<li><a href="info.html">attraction1_hp.cgi</a></li>')
print('<li><a href="shopping.html">お買い物</a></li>')
print('<li><a href="event.html">イベント</a></li>')
print('<li><a href="access.html">アクセス</a></li>')
print('</ul>')

print('</div>')
print('<!--/#footermenu-->')

print('<footer>')
print('<small>Copyright&copy; <a href="index.html">道の駅</a> All Rights Reserved.</small>')
print('<span class="pr"><a href="https://template-party.com/" target="_blank">《Web Design:Template-Party》</a></span>')
print('</footer>')

print('<!--開閉ブロック-->')
print('<div id="menubar">')

print('<nav>')
print('<ul>')
print('<li><a href="index.html">Home</a></li>')
print('<li><a href="attraction1_hp.cgi">AttractionInfo</a></li>')
print('<li><a href="shopping.html">Shopping</a></li>')
print('<li><a href="event.html">Event</a></li>')
print('<li><a href="mypage.cgi">Mypage</a></li>')
print('</ul>')
print('</nav>')

print('<p class="btn"><a href="contact.html">お問い合わせ</a></p>')

print('<div class="sh">')
print('<!-- 900px未満のメニュー開閉時にのみ表示させたい情報 -->')
print('<p>サンプルテキスト。サンプルテキスト。<br>')
print('サンプルテキスト。サンプルテキスト。<br>')
print('サンプルテキスト。サンプルテキスト。</p>')
print('</div>')
print('<!--/.sh-->')

print('</div>')
print('<!--/#menubar-->')

print('<!--開閉ボタン（ハンバーガーアイコン）-->')
print('<div id="menubar_hdr">')
print('<div>')
print('<span></span><span></span><span></span>')
print('</div>')
print('<p>MENU</p>')
print('</div>')

print('</div>')
print('<!--/#container-->')

print('<!--jQueryの読み込み-->')
print('<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>')

print('<!--スライドショー（vegas）-->')
print('<script src="https://cdnjs.cloudflare.com/ajax/libs/vegas/2.5.4/vegas.min.js"></script>')
print('<script src="js/vegas.js"></script>')

print('<!--パララックス（inview）-->')
print('<script src="https://cdnjs.cloudflare.com/ajax/libs/protonet-jquery.inview/1.1.2/jquery.inview.min.js"></script>')
print('<script src="js/jquery.inview_set.js"></script>')

print('<!--このテンプレート専用のスクリプト-->')
print('<script src="js/main.js"></script>')

print('<!--ページの上部へ戻るボタン-->')
print('<div class="pagetop"><a href="#"><i class="fas fa-angle-double-up"></i></a></div>')

print('</body>')
print('</html>')
