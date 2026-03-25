import feedparser
import requests
import os
from datetime import datetime, timedelta

# --- إعدادات الربط الخاصة بك ---
TOKEN = "8343143091:AAHuA7xDAyqwIExQYn3p1l3OW6rrbaRed7E"
CHAT_ID = "7665460040"

# --- رابط البحث (CapCut, Podcast, Subtitles, Repurpose) ---
RSS_URL = "https://www.upwork.com/ab/feed/jobs/rss?q=(Podcast+to+Shorts+OR+CapCut+OR+Subtitles+OR+Repurpose+OR+Viral+Shorts)&sort=recency"
DB_FILE = "last_job.txt"

def send_telegram(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    try:
        requests.post(url, data=payload, timeout=10)
    except:
        pass

def run_sniper():
    # حساب توقيت الجزائر (GMT+1)
    now_dz = datetime.utcnow() + timedelta(hours=1)
    current_time = now_dz.strftime("%H:%M:%S")

    # 🟢 الخطوة 1: رسالة التأكيد (تصلك فوراً عند التشغيل)
    confirmation_msg = (
        f"✅ **تأكيد:** النظام شغال 100% الآن.\n"
        f"🕒 وقت الفحص: `{current_time}`\n"
        "🔎 يبحث عن: (6 مقاطع، CapCut، بودكاست)"
    )
    send_telegram(confirmation_msg)

    # 🔵 الخطوة 2: المهمة الأساسية (صيد الوظائف)
    feed = feedparser.parse(RSS_URL)
    
    if feed.entries:
        latest_job = feed.entries[0]
        job_id = latest_job.id
        
        last_id = ""
        if os.path.exists(DB_FILE):
            with open(DB_FILE, "r") as f:
                last_id = f.read().strip()

        if job_id != last_id:
            # صيد جديد لم يرسل من قبل
            job_message = (
                "🎯 **صيد جديد ومؤكد!**\n"
                "━━━━━━━━━━━━━━━━━━\n"
                f"📝 **العنوان:** {latest_job.title}\n\n"
                f"🔗 **الرابط:** {latest_job.link}\n"
                "━━━━━━━━━━━━━━━━━━\n"
                "🚀 *أنت سريع! قدم الآن (6 مقاطع في يوم واحد)*"
            )
            send_telegram(job_message)
            
            # حفظ الهوية لمنع التكرار
            with open(DB_FILE, "w") as f:
                f.write(job_id)
    
    print(f"تم الفحص بنجاح في {current_time}")

if __name__ == "__main__":
    run_sniper()
