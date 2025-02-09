#!/usr/bin/python3

import cgi
import crypt
import os

form = cgi.FieldStorage()
user_name = form.getfirst('user_name')
mail_address = form.getfirst('mail_address')
password = form.getfirst('password')
phone_number = form.getfirst('phone_number')
face_pict = form['face_pict']




print("Content-Type: text/html\n")

htmlText = '''
<!DOCTYPE HTML>
<html lang="ja">
    <head>
        <meta charset="UTF-8">
        <title>登録内容確認｜Cyber Frontier</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="Cyber Frontierの登録内容確認ページです">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/vegas/2.5.4/vegas.min.css">
<link rel="stylesheet" href="css/style.css">

    </head>
    <body>

<header>
<h1 id="logo"><a href="index.html"><img src="images/CF_logo.PNG" alt="遊園地"></a></h1>
<ul id="lang-nav">

<li><a href= "login.html">ログイン</a></li>
<li><a href="mypage.cgi">マイページ</a></li>

</ul>

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
<center>
        <div id="wrapper">
この情報を登録しますか？<br><br>
<font class="login-input">%s</font><br><br>
<font class="login-input">%s</font><br><br>
<font class="login-input">%s</font><br><br>
<font class="login-input">%s</font><br><br>
<font class="login-input">%s</font><br>
<form action="subscribe.html" method="post">
                    <button type="submit">戻る</button><br>
            </form>
<form action="subscribe.cgi" method="post">
<input type="hidden" name="user_name" value="%s">
<input type="hidden" name="mail_address" value="%s">
<input type="hidden" name="password" value="%s">
<input type="hidden" name="phone_number" value="%s">
<input type="hidden" name="face_pict" value="%s">
                    <button type="submit">登録</button>
            </form>

        </div>
        
        </center>

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
'''%(user_name, mail_address, password, phone_number, face_pict, user_name, mail_address, password, phone_number, face_pict)

print(htmlText.encode("utf-8", 'ignore').decode('utf-8'))





