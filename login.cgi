#!/usr/bin/python3

import cgi
import crypt
import os
import MySQLdb
from http import cookies
import random, string
user_id = ""
form = cgi.FieldStorage()
user_name = form.getfirst('user_id')
password = form.getfirst('password')

def get_random_str(n):
	char_data = string.digits + string.ascii_lowercase + string.ascii_uppercase
	return ''.join([random.choice(char_data) for i in range(n)])

connection = MySQLdb.connect(
	host='localhost',
	user='user1',
	passwd='passwordA1!',
	db='booking',
	charset='utf8'
)

cursor = connection.cursor()
sql = "select * from User_data"
cursor.execute(sql)
rows = cursor.fetchall()

hashed_password = ''
message = ''
for row in rows:
	if row[1] == user_name:
		hashed_password = row[3]
		user_id = str(row[0])
		break
connection.close()

cpass = '1'
salt = hashed_password[:29]
if(password != None and salt != ''):
	cpass = crypt.crypt(password, salt)

location = './login.html'

f_login = -1
if (cpass==hashed_password):
	f_login = 0
	location = './mypage.html'
	message = 'ログインに成功しました'
else:
	message = 'ログインに失敗しました'
	location = './login.html'



session_id = get_random_str(64)

connection = MySQLdb.connect(
	host='localhost',
	user='user1',
	passwd='passwordA1!',
	db='booking',
	charset='utf8'
)

cursor = connection.cursor()

sql = "insert into `Session` (`user_id`, `session_id`) values ('"+ user_id +"', '" + session_id + "') on duplicate key update session_id = '" + session_id + "'"

cursor.execute(sql)

connection.commit()

connection.close()

if(f_login == 0):
	print("Conten-Type: text/html")
	print("Set-Cookie: user_id=" + user_id)
	print("Set-Cookie: session_id=" + session_id)

else:
	print("Content-type: text/html")
	print("Set-Cookie: user_id=user?")
	print("Set-Cookie: session_id=abcd1234")

print("Content-Type: text/html\n")

htmlText = '''
<!DOCTYPE HTML>
<html lang="ja">
<head>
<meta charset="UTF-8">
<title>ログイン｜Cyber Frontier</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="Cyber Frontierのログインページです">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/vegas/2.5.4/vegas.min.css">
<link rel="stylesheet" href="css/style.css">
</head>
<body>

<header>
<h1 id="logo"><a href="index.html"><img src="images/CF_logo.PNG" alt="遊園地"></a></h1>
<ul id="lang-nav">
<li><a href="">English</a></li>
<li><a href="">中文</a></li>
</ul>

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

<section>
<center>
<div id="wrapper">
<form action="%s" method="post">
%s<br>
<button type="submit">続ける</button>
</form>
</div>

</center>


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

<!--スライドショー（vegas）-->
<script src="https://cdnjs.cloudflare.com/ajax/libs/vegas/2.5.4/vegas.min.js"></script>
<script src="js/vegas.js"></script>

<!--パララックス（inview）-->
<script src="https://cdnjs.cloudflare.com/ajax/libs/protonet-jquery.inview/1.1.2/jquery.inview.min.js"></script>
<script src="js/jquery.inview_set.js"></script>

<!--このテンプレート専用のスクリプト-->
<script src="js/main.js"></script>

<!--ページの上部へ戻るボタン-->
<div class="pagetop"><a href="#"><i class="fas fa-angle-double-up"></i></a></div>


</body>
</html>
'''%(location, message)

print(htmlText.encode("utf-8", 'ignore').decode('utf-8'))





