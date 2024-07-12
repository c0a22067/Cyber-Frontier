#!/usr/bin/env python3

import cgi
import cgitb

cgitb.enable()

print("Content-Type: text/html\n")
print("""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<title>道の駅・物産館イメージ 無料ホームページテンプレート tp_bussan2</title>
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
</style>
</head>

<body>

<header>
<h1 id="logo"><a href="index.html"><img src="images/sample9.png" alt="道の駅"></a></h1>
</header>

<div id="container">

<nav id="header-menu">
<ul>
<li><a href="attraction.html">施設のご案内<i class="fas fa-info-circle"></i></a></li>
<li><a href="shopping.html">お買い物<i class="fas fa-shopping-basket"></i></a></li>
<li><a href="event.html">イベント<i class="far fa-calendar-alt"></i></a></li>
<li><a href="mypage.html">アクセス<i class="fas fa-map-marker-alt"></i></a></li>
</ul>
</nav>

<main>

<article>

<h2>詳細ページ</h2>

<p class="c"><img class="detail-img" src="images/sample6.png" alt=""></p>

<table class="ta1">
<caption>量子トンネルコースター</caption>
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

<p class="c"><a class="review-link" href="attraction1.cgi">レビューを見る</a></p>

<p class="c"><a href="javascript:history.back()">&lt;&lt; 前のページに戻る</a></p>

</article>

</main>

<div id="footermenu">
<ul>
<li class="title">メニュー</li>
<li><a href="index.html">ホーム</a></li>
<li><a href="company.html">運営会社</a></li>
<li><a href="attraction.html">施設のご案内</a></li>
<li><a href="shopping.html">お買い物</a></li>
<li><a href="event.html">イベント</a></li>
<li><a href="mypage.html">アクセス</a></li>
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
<li><a href="attraction.html">施設のご案内</a></li>
<li><a href="shopping.html">お買い物</a></li>
<li><a href="event.html">イベント</a></li>
<li><a href="mypage.html">アクセス</a></li>
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

