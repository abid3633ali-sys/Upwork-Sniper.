import feedparser
import requests
import os

TOKEN = "8343143091:AAHua7xDAYqwIExQYn3p1130W6rrbaRed7E"
CHAT_ID = "7665460040"
# غيرنا البحث هنا إلى كلمة Video لجلب نتائج جديدة فوراً
RSS_URL = "https://www.upwork.com/ab/feed/jobs/rss?q=Video&sort=recency"
LAST_JOB_FILE = "last_job.txt"

def send_to_telegram(title, link):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    message = f"✅ **تأكيد التشغيل: القناص يعمل!**\n\n📌 {title}\n\n🔗 [رابط الوظيفة]({link})"
    payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
    requests.post(url, data=payload)

# فحص سريع وإرسال بغض النظر عن الذاكرة للتجربة
feed = feedparser.parse(RSS_URL)
if feed.entries:
    latest_job = feed.entries[0]
    send_to_telegram(latest_job.title, latest_job.link)
    print("🚀 تم إرسال رسالة التأكيد بنجاح!")
