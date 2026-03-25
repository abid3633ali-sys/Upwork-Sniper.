import feedparser
import requests
import os

# بياناتك
TOKEN = "8343143091:AAHua7xDAYqwIExQYn3p1130W6rrbaRed7E"
CHAT_ID = "7665460040"
RSS_URL = "https://www.upwork.com/ab/feed/jobs/rss?q=Long+form+to+Shorts&sort=recency"
LAST_JOB_FILE = "last_job.txt"

def send_to_telegram(title, link):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    message = f"🎯 **صيد جديد على Upwork!**\n\n📌 {title}\n\n🔗 [رابط التقديم]({link})"
    payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
    requests.post(url, data=payload)

# قراءة آخر ID
last_sent_id = ""
if os.path.exists(LAST_JOB_FILE):
    with open(LAST_JOB_FILE, "r") as f:
        last_sent_id = f.read().strip()

# فحص الوظائف
feed = feedparser.parse(RSS_URL)
if feed.entries:
    latest_job = feed.entries[0]
    
    if latest_job.id != last_sent_id:
        send_to_telegram(latest_job.title, latest_job.link)
        # حفظ المعرف الجديد
        with open(LAST_JOB_FILE, "w") as f:
            f.write(latest_job.id)
        print(f"✅ أرسلت لك وظيفة جديدة: {latest_job.title}")
    else:
        print("😴 لا توجد وظائف جديدة.")
