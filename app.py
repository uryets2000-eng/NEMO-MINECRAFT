from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return r'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>NEMO CR | Official Website</title>
<style>
*{box-sizing:border-box}
body{
 margin:0;min-height:100vh;color:#fff;text-align:center;
 font-family:Tahoma,Arial,sans-serif;
 background:
 radial-gradient(ellipse at 15% 15%,#ff4d002c,transparent 42%),
 radial-gradient(ellipse at 85% 25%,#8c00ff35,transparent 43%),#07040c;
}
header{padding:25px 12px 5px}
.logo{font-size:clamp(42px,10vw,70px);font-weight:1000;font-style:italic;
 color:#ff7900;text-shadow:0 0 12px #ff4d00,0 0 28px #ff4d00}
.logo span{display:block;color:#d99aff;
 text-shadow:0 0 12px #a000ff,0 0 28px #9d00ff}
.line{height:3px;width:min(90%,700px);margin:17px auto;
 background:linear-gradient(90deg,#ff7900,#be00ff,#ff7900);
 box-shadow:0 0 12px #a000ff}
.welcome,.panel{
 width:min(92%,760px);margin:20px auto;padding:24px 18px;
 border:2px solid #a52aff;border-radius:20px;background:#0d0816ee;
 box-shadow:0 0 20px #8000ff44,inset 0 0 18px #ff790015
}
h1{font-size:clamp(23px,5vw,34px);color:#e1b4ff;
 text-shadow:0 0 12px #8c00ff;margin:0 0 15px}
p{line-height:2}
.welcome strong{color:#ff9b28}
.cards{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));
 gap:clamp(7px,3vw,22px);width:min(94%,780px);margin:28px auto}
.card{aspect-ratio:1/1;border-radius:50%;border:2px solid #a900ff;
 color:white;background:radial-gradient(circle,#241033,#09050e 72%);
 display:flex;flex-direction:column;justify-content:center;align-items:center;
 gap:10px;cursor:pointer;box-shadow:0 0 13px #9b00ff88;
 transition:.2s;padding:5px}
.card:nth-child(odd){border-color:#ff7900;box-shadow:0 0 14px #ff600088}
.card:active{transform:scale(.94)}
.card .symbol{font-size:clamp(28px,7vw,48px)}
.card b{font-size:clamp(12px,3.3vw,19px)}
.card small{font-size:clamp(9px,2.5vw,12px);color:#d9b5ff}
.panel{display:none}
.panel.show{display:block;animation:appear .25s ease}
@keyframes appear{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:translateY(0)}}
.panel h2{color:#ff9624}
.socials{display:grid;gap:13px;margin:22px auto;max-width:440px}
.social{display:flex;align-items:center;gap:14px;justify-content:center;
 padding:13px 18px;border-radius:13px;color:white;text-decoration:none;
 font-size:18px;font-weight:bold;transition:.2s;border:1px solid #ffffff33}
.social:active{transform:scale(.97)}
.social svg{width:34px;height:34px;flex-shrink:0}
.youtube{background:#ff0033}
.tiktok{background:#111;border:1px solid #fe2c55}
.telegram{background:#229ed9}
.skin-img{display:block;width:min(100%,440px);margin:15px auto;
 border-radius:15px;border:2px solid #a52aff;box-shadow:0 0 20px #9b00ff55}
.close{border:0;border-radius:22px;padding:11px 26px;
 background:linear-gradient(90deg,#ff7900,#a900ff);color:white;
 font-weight:bold;font-size:15px;cursor:pointer;margin-top:10px}
footer{padding:20px 10px;color:#c5a3e8;font-size:12px}
footer b{font-size:21px;color:#ff8a00}
@media(max-width:350px){.cards{gap:4px}.card{gap:6px}}
</style>
</head>
<body>
<header>
 <div class="logo">NEMO <span>CR</span></div>
 <div class="line"></div>
</header>

<section class="welcome">
 <h1>أهلاً وسهلاً بيكم بموقعي 👋</h1>
 <p>نورتوا موقعي، أني <strong>NEMO CR</strong>، وهذا المكان الخاص بي
 وبعالمي وبكل شي أحبه وأشاركه وياكم.</p>
 <p>هنا تكدرون تتعرفون عليّ أكثر، وتشوفون سكني الخاص بماينكرافت،
 وتوصلون لحساباتي وروابطي بكل سهولة.</p>
 <p>أتمنى يعجبكم الموقع وتستمتعون بوجودكم هنا.
 <strong>وجودكم يسعدني كثيراً ❤️</strong></p>
</section>

<div class="cards">
 <button class="card" onclick="showPanel('skin')">
  <span class="symbol">🎮</span><b>سكني</b><small>MY SKIN</small>
 </button>
 <button class="card" onclick="showPanel('about')">
  <span class="symbol">👤</span><b>عني</b><small>ABOUT ME</small>
 </button>
 <button class="card" onclick="showPanel('contact')">
  <span class="symbol">🔗</span><b>التواصل معي</b><small>CONTACT</small>
 </button>
</div>

<section id="skin" class="panel">
 <h2>🎮 سكني في ماينكرافت</h2>
 <p>هذا قسم سكني الخاص بـ NEMO CR.</p>
 <img class="skin-img" src="/static/skin.jpg"
      alt="صورة سكن NEMO CR"
      onerror="this.style.display='none';document.getElementById('skin-note').style.display='block'">
 <p id="skin-note" style="display:none">
  أضف صورة السكن داخل مجلد static باسم skin.png حتى تظهر هنا.
 </p>
 <button class="close" onclick="hidePanels()">رجوع للرئيسية</button>
</section>

<section id="about" class="panel">
 <h2>👤 عني</h2>
 <p>أهلاً بيكم، أني <strong>NEMO CR</strong> 🧡💜</p>
 <p>أني صانع محتوى ماينكرافت، أحب الألعاب وأشارك محتوى
 ماينكرافت وياكم على تيك توك.</p>
 <p>حالياً آخذ فترة استراحة من النشر بسبب الدراسة، لأن الدراسة
 مهمة بالنسبة إلي، وإن شاء الله هاي مو النهاية!
 راح أرجع إلكم من أكمّل هالفترة وأكون جاهز أقدم محتوى جديد وأحلى.</p>
 <p>شكراً لكل شخص تابعني ودعمني، وشكراً لكل شخص ينتظر رجعتي.
 دعمكم يعني إلي هواية، وإن شاء الله الجاي أحلى ويا NEMO CR! 🎮🔥</p>
 <button class="close" onclick="hidePanels()">رجوع للرئيسية</button>
</section>

<section id="contact" class="panel">
 <h2>🔗 تواصلوا وياي</h2>
 <p>تابعوني على حساباتي الرسمية 👇</p>
 <div class="socials">
  <a class="social youtube" href="https://www.youtube.com/@Nemo_CR5" target="_blank" rel="noopener">
   <svg viewBox="0 0 24 24" aria-hidden="true">
    <rect x="1" y="4" width="22" height="16" rx="5" fill="white"/>
    <path d="M10 8l7 4-7 4z" fill="#ff0033"/>
   </svg>
   <span>YouTube</span>
  </a>
  <a class="social tiktok" href="https://www.tiktok.com/@n.e3m3?_r=1&_t=ZS-9AsN1m8lGzw" target="_blank" rel="noopener">
   <svg viewBox="0 0 24 24" aria-hidden="true">
    <path d="M15 2h3c.3 2.3 1.6 3.8 4 4.2v3.2c-2.1 0-3.8-.7-5-1.8v7.1a6.5 6.5 0 1 1-6.5-6.5c.5 0 1 .1 1.5.2v3.5a3.2 3.2 0 1 0 1.8 2.8V2z" fill="#25f4ee" transform="translate(-1 1)"/>
    <path d="M15 2h3c.3 2.3 1.6 3.8 4 4.2v3.2c-2.1 0-3.8-.7-5-1.8v7.1a6.5 6.5 0 1 1-6.5-6.5c.5 0 1 .1 1.5.2v3.5a3.2 3.2 0 1 0 1.8 2.8V2z" fill="#fe2c55" transform="translate(1 0)"/>
    <path d="M15 2h3c.3 2.3 1.6 3.8 4 4.2v3.2c-2.1 0-3.8-.7-5-1.8v7.1a6.5 6.5 0 1 1-6.5-6.5c.5 0 1 .1 1.5.2v3.5a3.2 3.2 0 1 0 1.8 2.8V2z" fill="white"/>
   </svg>
   <span>TikTok</span>
  </a>
  <a class="social telegram" href="https://t.me/osam5643" target="_blank" rel="noopener">
   <svg viewBox="0 0 24 24" aria-hidden="true">
    <circle cx="12" cy="12" r="11" fill="white"/>
    <path d="M5 11.4 18.8 6c.7-.3 1.2.2 1 1l-2.4 11.2c-.2.8-.7 1-1.4.5l-3.8-2.8-1.9 1.8c-.3.3-.6.3-.7-.2l.2-3.9 7.1-6.4c.3-.3-.1-.4-.5-.2l-8.8 5.5-3.8-1.2c-.8-.3-.8-.8 1.2-1.6z" fill="#229ed9"/>
   </svg>
   <span>Telegram</span>
  </a>
 </div>
 <button class="close" onclick="hidePanels()">رجوع للرئيسية</button>
</section>

<footer>
 <div class="line"></div>
 <b>NEMO CR</b>
 <p>MINECRAFT | GAMING | COMMUNITY</p>
</footer>
<script>
function showPanel(id){
 document.querySelectorAll('.panel').forEach(p=>p.classList.remove('show'));
 document.getElementById(id).classList.add('show');
 document.getElementById(id).scrollIntoView({behavior:'smooth',block:'center'});
}
function hidePanels(){
 document.querySelectorAll('.panel').forEach(p=>p.classList.remove('show'));
 window.scrollTo({top:0,behavior:'smooth'});
}
</script>
</body>
</html>'''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
