#!/usr/bin/python3

import cgi
import html
import MySQLdb
import cgitb
cgitb.enable()  # エラーメッセージを表示

def fetch_reviews():
    try:
        connection = MySQLdb.connect(
            host='localhost',
            user='user1',
            passwd='passwordA1!',
            db='booking',
            charset='utf8'
        )
        cursor = connection.cursor()
        cursor.execute("SELECT user_id, attraction, title, rating, comment FROM reviews ORDER BY id DESC")
        rows = cursor.fetchall()
        connection.close()
        return rows
    except MySQLdb.MySQLError as e:
        print("Content-Type: text/html\n")
        print("<html><body>")
        print("<h1>Database connection error</h1>")
        print("<p>{}</p>".format(e))
        print("</body></html>")
        raise

def insert_review(user_id, attraction, title, rating, comment):
    try:
        connection = MySQLdb.connect(
            host='localhost',
            user='user1',
            passwd='passwordA1!',
            db='booking',
            charset='utf8'
        )
        cursor = connection.cursor()
        cursor.execute("INSERT INTO reviews (user_id, attraction, title, rating, comment) VALUES (%s, %s, %s, %s, %s)", (user_id, attraction, title, rating, comment))
        connection.commit()
        connection.close()
    except MySQLdb.MySQLError as e:
        print("Content-Type: text/html\n")
        print("<html><body>")
        print("<h1>Database connection error</h1>")
        print("<p>{}</p>".format(e))
        print("</body></html>")
        raise

form = cgi.FieldStorage()
user_id = form.getfirst('user_id')
attraction = form.getfirst('attraction')
title = form.getfirst('title')
rating = form.getfirst('rating')
comment = form.getfirst('comment')

if user_id and attraction and title and rating and comment:
    insert_review(user_id, attraction, title, rating, comment)

# CGIでHTMLヘッダーを出力
print("Content-Type: text/html\n")

htmlText = '''
<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="utf-8">
<title>道の駅・物産館イメージ 無料ホームページテンプレート tp_bussan2</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="ここにサイト説明を入れます">
<link rel="stylesheet" href="style.css">
<style>
    .review {
        background-color: #0F1A45;
        border: 1px solid #333;
        border-radius: 10px;
        padding: 10px;  /* paddingを減らす */
        margin: 10px auto;  /* marginを減らす */
        box-shadow: 0 0 10px rgba(0,0,0,0.5);
        max-width: 600px;  /* 最大幅を600pxに制限 */
    }
    .review p, .review h2, .review small {
        margin: 5px 0;  /* 各要素の間の余白を減らす */
    }
    .stars {
        color: #FFD700;
        font-size: 1.5em;
    }
    .form-container {
        background-color: #1E1E1E;
        border: 1px solid #333;
        border-radius: 10px;
        padding: 20px;
        margin: 20px auto;  /* センターに配置 */
        box-shadow: 0 0 10px rgba(0,0,0,0.5);
        max-width: 600px;  /* 最大幅を600pxに制限 */
    }
    .form-container h2 {
        color: #00BCD4;
        text-align: center;
    }
    .form-container label {
        display: block;
        margin-top: 10px;
    }
    .form-container input, .form-container textarea, .form-container select {
        width: 100%;
        padding: 10px;
        margin-top: 5px;
        background-color: #333;
        border: 1px solid #555;
        border-radius: 5px;
        color: #E0E0E0;
    }
    .form-container input[type="submit"] {
        background-color: #00BCD4;
        color: #121212;
        cursor: pointer;
    }
    .form-container input[type="submit"]:hover {
        background-color: #00A0B2;
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
<li><a href="attraction.html">施設のご案内<i class="fas fa-info-circle"></i></a></li>
<li><a href="shopping.html">お買い物<i class="fas fa-shopping-basket"></i></a></li>
<li><a href="event.html">イベント<i class="far fa-calendar-alt"></i></a></li>
<li><a href="mypage.html">アクセス<i class="fas fa-map-marker-alt"></i></a></li>
</ul>
</nav>

<main>

<article>

<h2>レビュー</h2>
'''

def rating_to_stars(rating):
    return '★' * int(rating) + '☆' * (5 - int(rating))

reviews = fetch_reviews()
if reviews:
    for review in reviews:
        stars = rating_to_stars(review[3])
        htmlText += f'''
        <div class="review">
            <h2>{html.escape(review[2])}</h2>
            <p><strong>Attraction:</strong> {html.escape(review[1])}</p>
            <p><strong>Rating:</strong> <span class="stars">{stars}</span></p>
            <p><strong>Comment:</strong> {html.escape(review[4])}</p>
            <p><small>Posted by: {html.escape(review[0])}</small></p>
        </div>
        '''
else:
    htmlText += '<p>No reviews found.</p>'

htmlText += '''
<div class="form-container">
    <h2>Post a Review</h2>
    <form method="post" action="/proj/attraction1.cgi">
        <label for="user_id">User ID:</label>
        <input type="text" id="user_id" name="user_id" required>
        
        <label for="attraction">Attraction:</label>
        <select id="attraction" name="attraction" required>
            <option value="量子トンネルコースター">量子トンネルコースター</option>
            <option value="Digital Haunted House">Digital Haunted House</option>
            <option value="Like A Maze">Like A Maze</option>
            <option value="Matrix Drift Arena2.0">Matrix Drift Arena2.0</option>
        </select>
        
        <label for="title">Title:</label>
        <input type="text" id="title" name="title" required>
        
        <label for="rating">Rating (1-5):</label>
        <input type="number" id="rating" name="rating" min="1" max="5" required>
        
        <label for="comment">Comment:</label>
        <textarea id="comment" name="comment" rows="4" required></textarea>
        
        <input type="submit" value="Submit Review">
    </form>
</div>

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
'''

print(htmlText.encode("utf-8", 'ignore').decode('utf-8'))


