import feedparser
import requests
import time

# بيانات الربط الخاصة بك
TOKEN = "8343143091:AAHuA7xDAyqwIExQYn3p1l3OW6rrbaRed7E"
CHAT_ID = "7665460040"

# رابط البحث المخصص (Long form to Shorts)
RSS_URL = "https://www.upwork.com/ab/feed/jobs/rss?q=Long+form+to+Shorts&sort=recency"

def send_to_telegram(title, link, description):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    message = f"🎯 **صيد جديد على Upwork!**\n\n📌 **الوظيفة:** {title}\n\n🔗 **رابط التقديم:**\n{link}"
    payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print(f"❌ خطأ في الإرسال: {e}")

last_job_id = None
print("🚀 القناص بدأ المراقبة الآن.. سأخبرك فور ظهور وظيفة جديدة.")

while True:
    try:
        feed = feedparser.parse(RSS_URL)
        if feed.entries:
            latest_job = feed.entries[0]
            # التأكد من أن الوظيفة جديدة ولم نرسلها من قبل
            if latest_job.id != last_job_id:
                send_to_telegram(latest_job.title, latest_job.link, latest_job.description)
                last_job_id = latest_job.id
                print(f"✅ أرسلت لك وظيفة جديدة: {latest_job.title}")
    except Exception as e:
        print(f"⚠️ تنبيه: {e}")
   
    # يفحص كل دقيقة واحدة (60 ثانية)
    time.sleep(60) 