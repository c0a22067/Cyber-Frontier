#!/usr/bin/python3

import MySQLdb
import cgi
from http.cookies import SimpleCookie
import os
cookie_string = os.environ.get('HTTP_COOKIE', '')

# フォームデータを取得
form = cgi.FieldStorage()
logout_requested = form.getvalue('logout')

user_name =""
phone_number=""
email_address=""
user_id = ""
session_id = ""
session_id_s = ""
info = ['ユーザ名','電話番号','メールアドレス']
user_info = []

cookie = SimpleCookie()
cookie.load(cookie_string)

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
sql = "select session_id from Session where user_id ='" + user_id + "'"
cursor.execute(sql)
rows = cursor.fetchall()
session_id = ''
for row in rows:
 session_id = row[0]
f_login = -1
if(session_id == session_id_s):
 f_login = 0

comments = ''
if(f_login == 0):
 cursor = connection.cursor()
 sql = "select * from User_data"
 cursor.execute(sql)
 rows2 = cursor.fetchall()
 for row2 in rows2:
  if(str(row2[0]) == user_id):
    user_name = row2[1]
    phone_number=row2[4]
    email_address=row2[2]
    user_info = [user_name,phone_number,email_address]
    comments = row2[1] + 'さんこんにちは'
    login = '<form method="post" action="mypage.cgi"><input type="hidden" name="logout" value="1"><button type="submit" class="login-btn">ログアウト</button></form>'
else:
 comments = 'ゲストさんこんにちは'
 login = '<form method="post" action="./login.html"><button type="submit" class="login-btn">ログイン</button></form>'
if logout_requested:
    cookie['user_id'] = ''
    cookie['user_id']['expires'] = 'Thu, 01 Jan 1970 00:00:00 GMT'
    cookie['session_id'] = ''
    cookie['session_id']['expires'] = 'Thu, 01 Jan 1970 00:00:00 GMT'
    print(cookie.output())
    print("Set-Cookie: session_id=abcd1234")
    
    # JavaScriptを使用して自動的にリダイレクトする
    print("Content-Type: text/html\n")
    print('<html><head><script>window.location.replace("mypage.cgi");</script></head><body></body></html>')


    

print("Content-Type: text/html\n")
connection.close()

htmlText = '''
<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<title>Cyber Frontierのマイページ</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="マイページ画面">
<link rel="stylesheet" href="css/style.css">
</head>
<style>
/* ログインボタンのスタイル */
button.login-btn {
    background-color: #007bff; /* ボタンの背景色 */
    color: white; /* ボタンの文字色 */
    border: none; /* ボーダーをなしにする */
    padding: 10px 20px; /* 上下左右の余白 */
    font-size: 16px; /* 文字サイズ */
    cursor: pointer; /* カーソルをポインターに変更 */
    border-radius: 5px; /* ボタンの角を丸める */
}

button.login-btn:hover {
    background-color: #0056b3; /* ホバー時の背景色 */


</style>

<body>

<header>
<h1 id="logo"><a href="index.html"><img src="images/CF_logo.PNG" alt="Cyber-Frontier"></a></h1>
</header>

<div id="container">

<nav id="header-menu">
<ul>
<li><a href="attraction1_hp.cgi">attraction<i class="fas fa-rocket"></i></a></li>
<li><a href="shopping.html">shop<i class="fas fa-shopping-basket"></i></a></li>
<li><a href="event.html">event<i class="fas fa-calendar-alt"></i></a></li>
<li><a href="mypage.cgi">mypage<i class="fas fa-user"></i></i></a></li>
</ul>
</nav>

<main>

<section>

<h2>mypage</h2>

<h2>%s</h2>
<p></p>
<div class="login"><center>%s</center></div>
<br>
''' % (comments, login)

if f_login == 0:  # ログインしている場合のみ会員情報を表示
    htmlText += '''
    <p><center>このページでは会員情報を確認できます。</center></p>

    <table class="ta1">
    <caption>会員情報</caption>
    '''
    for i, j in zip(info, user_info):
        htmlText += '''
        <tr>
        <th>%s</th>
        <td>%s</td>
        </tr>
        ''' % (i, j)
    htmlText += '''
    </table>
    <br>
    <p><center>こちらから、予約アトラクションを確認できます。</center></p>
    <center><form method="post" action="./reservation_check.cgi"><button type="submit" class="login-btn">予約確認</button></form></center>
    '''

htmlText += '''
</section>

</main>

<div id="footermenu">
<ul>
<li class="title">menu</menu></li>
<li><a href="index.html">Home</a></li>
<li><a href="company.html">Company</a></li>
<li><a href="attraction.html">AttractionInfo</a></li>
<li><a href="shopping.html">shopping</a></li>
<li><a href="event.html">event</a></li>
<li><a href="mypage.cgi">Mypage</a></li>
</ul>
<ul>
<li class="title">attraction</li>
<li><a href="#">DEGITAL HONTET HOUSE</a></li>
<li><a href="#">LIKE A MAZE</a></li>
<li><a href="#">量子トンネルコースター</a></li>
<li><a href="#">MATRIX DRIFT ARENA</a></li>
</ul>
<ul>
<li class="title">event</li>
<li><a href="event.html">Cyber Treasure Hunter</a></li>
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
<li><a href="index.html">Home</a></li>
<li><a href="attraction1_hp.cgi">AttractionInfo</a></li>
<li><a href="shopping.html">Shoping</a></li>
<li><a href="event.html">Event</a></li>
<li><a href="mypage.cgi">Mypage</a></li>
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
'''

print(htmlText.encode("utf-8", 'ignore').decode('utf-8'))
