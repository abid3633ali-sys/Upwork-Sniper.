import feedparser
import requests
import os
from datetime import datetime, timedelta

# بيانات الربط الخاصة بك
TOKEN = "8343143091:AAHuA7xDAyqwIExQYn3p1l3OW6rrbaRed7E"
CHAT_ID = "7665460040"
# الكلمات المفتاحية لتخصصك (فيديوهات قصيرة وفيروسية)
RSS_URL = "https://www.upwork.com/ab/feed/jobs/rss?q=(Podcast+to+Short+OR+Long+form+to+Shorts+OR+Viral+Video+OR+Hormozi)&sort=recency"
DB_FILE = "last_job.txt"

def send_telegram(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print(f"❌ خطأ في الإرسال: {e}")

def run_sniper():
    # حساب الوقت الحالي بتوقيت الجزائر (GMT+1)
    now_dz = datetime.utcnow() + timedelta(hours=1)
    current_time = now_dz.strftime("%H:%M:%S")

    # --- رسالة التأكيد (ستصلك في كل مرة يعمل فيها النظام) ---
    confirmation_msg = f"✅ **تأكيد التشغيل:** النظام يعمل الآن بكفاءة من خوادم GitHub.\n🕒 الوقت الحالي: `{current_time}`"
    send_telegram(confirmation_msg)
    print(f"✅ تم إرسال رسالة التأكيد في {current_time}")

    # --- فحص وظائف Upwork ---
    feed = feedparser.parse(RSS_URL)
    if feed.entries:
        latest_job = feed.entries[0]
        job_id = latest_job.id
        
        last_sent_id = ""
        if os.path.exists(DB_FILE):
            with open(DB_FILE, "r") as f:
                last_sent_id = f.read().strip()

        if job_id != last_sent_id:
            job_message = (
                "🎯 **صيد جديد!**\n"
                "━━━━━━━━━━━━━━━━━━\n"
                f"🎬 **الوظيفة:** {latest_job.title}\n"
                f"🔗 **الرابط:** {latest_job.link}\n"
                "━━━━━━━━━━━━━━━━━━"
            )
            send_telegram(job_message)
            with open(DB_FILE, "w") as f:
                f.write(job_id)
    else:
        print("📭 لا توجد وظائف جديدة حالياً.")

if __name__ == "__main__":
    run_sniper()
