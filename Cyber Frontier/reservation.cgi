#!/usr/bin/python3

import cgi
import MySQLdb
import random
import os
from datetime import datetime, timedelta

def get_random(n):
    return ''.join(str(random.randrange(10)) for _ in range(n))

form = cgi.FieldStorage()
user_id = form.getvalue('user_id', '1')
attraction = form.getvalue('attraction', 'attraction')
book_id = get_random(5)

try:
    connection = MySQLdb.connect(
        host='localhost',
        user='user1',
        passwd='passwordA1!',
        db='booking',
        charset='utf8'
    )
    cursor = connection.cursor()
    
    cursor.execute("SELECT name, email_address FROM User_data WHERE user_id = %s", (user_id,))
    user_data = cursor.fetchone()
    name = user_data[0] if user_data and user_data[0] else ''
    mail = user_data[1] if user_data and user_data[1] else ''


    # 現在時刻を取得
    current_time = datetime.now()

    # book_dateをDATE形式に変換
    book_date = datetime.now()
    book_date = book_date.replace(second=0)

    # 10:00から17:00まで30分間隔で時間を生成
    #テスト中は営業時間を変更して挙動を確認
    #発表時の時刻も考慮すること！
    start_time = book_date.replace(hour=10, minute=0)
    end_time = book_date.replace(hour=20, minute=0)
    time_slots = []

    while start_time <= end_time:
        # 現在時刻と比較して過去の時間は無効化
        if start_time > current_time:
            time_slots.append(start_time)
        start_time += timedelta(minutes=30)

    # 予約可能な時間をHTMLとして生成
    time_slots_html = ""
    for slot in time_slots:
        slot_str = slot.strftime('%Y-%m-%d %H:%M:%S')
        
        # その時間の予約数をカウント
        cursor.execute("SELECT COUNT(*) FROM booking_log WHERE attraction=%s AND book_date=%s", (attraction, slot_str))
        count = cursor.fetchone()[0]
        
        # 同じユーザーが同じ時間に予約しているか確認
        cursor.execute("SELECT COUNT(*) FROM booking_log WHERE user_id=%s AND book_date=%s", (user_id, slot_str))
        user_count = cursor.fetchone()[0]
        
        if count < 5 and user_count == 0:
            time_slots_html += f'<option value="{slot_str}">{slot.strftime("%H:%M")}</option>'
        elif user_count > 0:
            time_slots_html += f'<option value="{slot_str}" disabled>{slot.strftime("%H:%M")} (既に予約済み)</option>'
        else:
            time_slots_html += f'<option value="{slot_str}" disabled>{slot.strftime("%H:%M")} (満員)</option>'
       
   

    print("Content-Type: text/html\n")

    html_content = f"""
<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<title><Cyber Frontier>アトラクション予約ページ</title>
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
    <h2><b><font color = "#000033">アトラクション予約</font></h2></b>
    <hr>
    <br>
    <form action="./reservation_confirmation.cgi" method="post">
        <input type="hidden" name="name" value="{name}">
        <input type="hidden" name="mail" value="{mail}">
        <input type="hidden" name="user_id" value="{user_id}">
        <input type="hidden" name="attraction" value="{attraction}">
        <input type="hidden" name="book_date" value="{book_date}">
        <p><font size="5"><font color = "#000033"><strong>{attraction}</font></strong></font></p>
        <img src="./attraction.png" style="width: 80%; height: auto; margin: 0px 0;border-radius: 10px">
        <label for="time" style="font-size: 1.2em; display: block; margin: 10px 0;">予約時間を選択してください</label>
        <select name="time" id="time" style="padding: 10px; font-size: 1.1em; width: 100%; max-width: 300px; margin: 10px 0;">
            {time_slots_html}
        </select>
        <input type="submit" value="予約" style="padding: 10px 20px; font-size: 1.1em; margin: 20px 0;">
        <br>
        <p><hr></p>
        <p style="color: red;">※アトラクション予約は当日のみ受け付けております。</p>
        <p style="color: red;">※表示されている時間のみご予約が可能です。</p>
    </form>
</section>

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
    print("Content-Type: text/html\n")
    print(f"<html><body><h1>データベースエラー</h1><p>{e}</p></body></html>")

finally:
    if connection:
        connection.close()
