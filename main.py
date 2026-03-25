import feedparser
import requests
import os

# بيانات الربط الخاصة بك
TOKEN = "8343143091:AAHua7xDAYqwIExQYn3p1130W6rrbaRed7E"
CHAT_ID = "7665460040"

# رابط البحث المخصص (Long form to Shorts)
RSS_URL = "https://www.upwork.com/ab/feed/jobs/rss?q=Long+form+to+Shorts&sort=recency"
LAST_JOB_FILE = "last_job.txt"

def send_to_telegram(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
    requests.post(url, data=payload)

# 1. إرسال رسالة التأكيد (لأنك طلبت التأكد من الكفاءة)
confirmation_msg = "✅ مرحبا يا علي، أنا أعمل الآن من داخل GitHub بكفاءة قوية! نظام الصيد مفعل الآن كل 8 دقائق. 🚀"
send_to_telegram(confirmation_msg)

# 2. فحص وظائف Upwork
last_sent_id = ""
if os.path.exists(LAST_JOB_FILE):
    with open(LAST_JOB_FILE, "r") as f:
        last_sent_id = f.read().strip()

feed = feedparser.parse(RSS_URL)
if feed.entries:
    latest_job = feed.entries[0]
    # التأكد من أنها وظيفة جديدة لم ترسل من قبل
    if latest_job.id != last_sent_id:
        job_message = f"🎯 **وظيفة جديدة مكتشفة!**\n\n📌 {latest_job.title}\n\n🔗 [اضغط هنا للتقديم]({latest_job.link})"
        send_to_telegram(job_message)
        
        # حفظ المعرف الجديد في الذاكرة
        with open(LAST_JOB_FILE, "w") as f:
            f.write(latest_job.id)
