#!/usr/bin/env python3

import cgi
import cgitb

cgitb.enable()

print("Content-Type: text/html\n")
print("""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<title>アトラクションの詳細</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="ここにサイト説明を入れます">
<link rel="stylesheet" href="style.css">
</head>

<body>

<header>
<h1 id="logo"><a href="index.html"><img src="images/CF_logo.PNG" alt="道の駅"></a></h1>
</header>

<div id="container">

<nav id="header-menu">
<ul>
<li><a href="attraction.html">attraction<i class="fas fa-rocket"></i></a></li>
<li><a href="shopping.html">shop<i class="fas fa-shopping-basket"></i></a></li>
<li><a href="event.html">event<i class="far fa-calendar-alt"></i></a></li>
<li><a href="mypage.html">mypage<i class="fas fa-user"></i></a></li>
</ul>
</nav>

<main>

<section>

<h2 class="flag">attraction information<span>Information</span></h2>
<p class="c">横並びブロックを使う場合、ブロック全体を囲んでいる「list-container」タグを入れ忘れないで下さい。<br>
これがないとレイアウトが崩れます。</p>
<p class="c">出現してくるアニメーションは他にも色々ご用意しております。<br>
テンプレート内の<a href="sample_inview.html">sample_inview.htmlをお読み下さい。</a></p>

<div class="list-container">

<div class="list blur">
<figure><a href="template_attraction.cgi"><img src="images/sample6.png" alt=""></a></figure>
<div class="text">
<h4>量子トンネルコースター</h4>
<p>科学の世界とエンターテインメントを融合させた先進的なジェットコースター</p>
<p>まるで小さな粒子がエネルギー障壁を通り抜けるように、ライダーが次々と異なる空間や時間を体験するアトラクション</p>
</div>
<p class="btn"><a href="template_attraction.cgi">詳しくみる</a></p>
</div>

<div class="list blur">
<figure><a href="article.html"><img src="images/sample7.png" alt=""></a></figure>
<div class="text">
<h4>Digital Haunted House</h4>
<p>サイバー空間の悪夢をテーマにした革新的なホラーアトラクション</p>
<p>単なるホラーアトラクションを超えた、最新技術と恐怖の融合が体感できる</p>
</div>
<p class="btn"><a href="article.html">詳しくみる</a></p>
</div>

<div class="list blur">
<figure><a href="article.html"><img src="images/sample8.png" alt=""></a></figure>
<div class="text">
<h4>Like A Maze</h4>
<p>最新のホログラフィック技術とインタラクティブなデジタルエフェクトを駆使し、訪問者に未来的で挑戦的な体験ができる</p>
<p>デジタルと現実が交錯する世界で、挑戦と興奮を体感せよ</p>
</div>
</div>

<div class="list blur">
<figure><a href="article.html"><img src="images/sample9.png" alt=""></a></figure>
<div class="text">
<h4>Matrix Drift Arena2.0</h4>
<p>最新のシミュレーション技術とホログラフィックエフェクトを駆使しバーチャルリアリティの中でドリフトレースが体験できる</p>
<p>技術とスピードが試されるこのアリーナで、最高のドリフトレーサーを目指せ</p>
</div>
</div>

</div>
<!--/.list-container-->

</section>

<section>

<h2>アトラクションのご案内<span>Information</span></h2>

<div class="list2 blur">
<figure><a href="article.html"><img src="images/sample2.png" alt=""></a></figure>
<div class="text">
<h4>Official Store</h4>
<p>Cyber Frontier公式グッズなどが販売中</p>

<p class="btn"><a href="article.html">詳しくみる</a></p>
</div>
</div>

<div class="list2 blur">
<figure><a href="article.html"><img src="images/sample4.png" alt=""></a></figure>
<div class="text">
<h4>Neon Nexus Bistro</h4>
<p>ネオンライトが輝くパークを一望できるレストラン</p>
<p class="btn"><a href="article.html">詳しくみる</a></p>
</div>
</div>

<div class="list2 blur">
<figure><a href=".html"><img src="images/sample3.png" alt=""></a></figure>
<div class="text">
<h4>Circuit City Grill</h4>
<p>時の進みがゆっくりになる不思議なレストラン</p>
</div>
</div>

<div class="list2 blur">
<figure><a href="article.html"><img src="images/sample5.png" alt=""></a></figure>
<div class="text">
<h4>Hyper Bit Theater</h4>
<p>様々なショーが開催されるシアター。開催中のイベントはこちら</p>
</div>
</div>

</section>

</main>

<div id="footermenu">
<ul>
<li class="title">Menu</li>
<li><a href="index.html">Home</a></li>
<li><a href="company.html">Company</a></li>
<li><a href="attraction.html">AttractionInfo</a></li>
<li><a href="shopping.html">Shopping</a></li>
<li><a href="event.html">Event</a></li>
<li><a href="mypage.html">Mypage</a></li>
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
<li><a href="index.html">Home</a></li>
<li><a href="attraction.html">AttractionInfo</a></li>
<li><a href="shopping.html">Shopping</a></li>
<li><a href="event.html">Event</a></li>
<li><a href="mypage.html">Mypage</a></li>
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
<script src="jquery.inview_set.js"></script>

<!--このテンプレート専用のスクリプト-->
<script src="main.js"></script>

<!--ページの上部へ戻るボタン-->
<div class="pagetop"><a href="#"><i class="fas fa-angle-double-up"></i></a></div>

</body>
</html>
""")

