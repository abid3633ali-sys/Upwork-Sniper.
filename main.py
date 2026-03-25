import feedparser
import requests
import os

TOKEN = "8343143091:AAHua7xDAYqwIExQYn3p1130W6rrbaRed7E"
CHAT_ID = "7665460040"
RSS_URL = "https://www.upwork.com/ab/feed/jobs/rss?q=Long+form+to+Shorts&sort=recency"
LAST_JOB_FILE = "last_job.txt"

def send_to_telegram(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
    try:
        requests.post(url, data=payload, timeout=10)
    except:
        pass

# إرسال رسالة التأكيد القوية التي طلبتها
send_to_telegram("🚀 **مرحبا يا علي، أنا أعمل الآن من داخل GitHub بكفاءة 100%!**\n\nتم تجاوز قيود الأمان بنجاح.")

# فحص الوظائف
last_sent_id = ""
if os.path.exists(LAST_JOB_FILE):
    with open(LAST_JOB_FILE, "r") as f:
        last_sent_id = f.read().strip()

feed = feedparser.parse(RSS_URL)
if feed.entries:
    latest_job = feed.entries[0]
    if latest_job.id != last_sent_id:
        job_msg = f"🎯 **وظيفة لقطة جديدة!**\n\n📌 {latest_job.title}\n\n🔗 [رابط التقديم فورا]({latest_job.link})"
        send_to_telegram(job_msg)
        with open(LAST_JOB_FILE, "w") as f:
            f.write(latest_job.id)
