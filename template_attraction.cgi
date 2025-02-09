#!/usr/bin/env python3

import cgi
import cgitb

cgitb.enable()

print("Content-Type: text/html\n")
print("""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<title>量子トンネルコースター</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="ここにサイト説明を入れます">
<link rel="stylesheet" href="style.css">
<style>
    .detail-img {
        max-width: 300px;  /* 画像の幅を300ピクセルに制限 */
        height: auto;     /* 高さは自動調整 */
    }
    .review-link {
        color: white;     /* リンクの色を白に設定 */
        text-decoration: none;  /* リンクの下線を消す */
    }
    .review-link:hover {
        text-decoration: underline;  /* ホバー時に下線を表示 */
    }
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
}
</style>
</head>

<body>

<header>
<h1 id="logo"><a href="index.html"><img src="images/CF_logo.PNG" alt="道の駅"></a></h1>
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

<article>
<table class="ta1">
<caption>量子トンネルコースター</caption>
<p class="c"><img class="detail-img" src="images/sample6.png" alt=""></p>


<tr>
<th>特徴</th>
<td>コースターのテーマは量子トンネル効果で、コース全体が未来的なデザインで装飾されています。
トンネルやループ、急降下などのコースは、量子の世界をイメージさせる光と音の演出で彩られています。</td>
</tr>
<tr>
<th>体験</th>
<td>通常の物理法則を超えるような急激な加速や減速、方向転換を体験します。これは、量子トンネル効果が物質を通り抜けるようなイメージを再現しています。
いくつかのセクションでは、ライダーは短時間で別の位置に「瞬間移動」するような感覚を味わいます。
</td>
</tr>
<tr>
<th>エンターテインメントと教育</th>
<td>乗車前には、量子トンネル効果についての簡単な説明や、量子力学の基礎知識を提供するインタラクティブな展示があります。
アトラクション内の映像や音声ガイドは、科学的なコンセプトをわかりやすく解説しながら、エンターテインメントとして楽しめる内容になっています。
</td>
</tr>
<tr>
<th>対象年齢</th>
<td>6歳以上</td>
</tr>
<tr>
<th>所要時間</th>
<td>約3分</td>
</tr>
<tr>
<th>利用制限</th>
<td><p>身長117cmに満たない方はご利用になれません。</p>
<p>乗り物に1人で座って安定した姿勢を保てない方はご利用になれません。</p>
<p>高血圧の方、心臓・脊椎・首に疾患のある方、その他アトラクションのご利用により悪化するおそれのある症状をお持ちの方はご利用をご遠慮ください。</p>
<p>妊娠中の方はご利用をご遠慮ください。</p>
<p>高齢の方はご利用をご遠慮ください。</p>
<p>乗り物に酔いやすい方はご利用をご遠慮ください。</p></td>
</tr>
</table>
<center><form method="post" action="./attraction1.cgi"><button type="submit" class="login-btn">レビューを見る</button></form></center>
<br>

<center><form method="post" action="./reservation.cgi"><button type="submit" class="login-btn">予約する</button></form></center>




<h4 class="c"><a href="javascript:history.back()">&lt;&lt; 前のページに戻る</a></h4>

</article>

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
""")


