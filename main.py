import feedparser
import requests
from datetime import datetime

# بيانات الربط
TOKEN = "8343143091:AAHuA7xDAyqwIExQYn3p1l3OW6rrbaRed7E"
CHAT_ID = "7665460040"
RSS_URL = "https://www.upwork.com/ab/feed/jobs/rss?q=Long+form+to+Shorts&sort=recency"

def send_job_to_telegram(title, link, description):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    
    # تنسيق الرسالة بشكل جذاب
    message = (
        "🎯 **صيد جديد على Upwork!**\n"
        "━━━━━━━━━━━━━━━━━━\n"
        f"📌 **الوظيفة:** {title}\n\n"
        f"🔗 **رابط التقديم:**\n{link}\n"
        "━━━━━━━━━━━━━━━━━━\n"
        "🚀 *كن أول المتقدمين للحصول على الأفضلية!*"
    )
    
    payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
    requests.post(url, data=payload)

# فحص الفيد (Feed)
print("🔍 جاري فحص أحدث الوظائف...")
feed = feedparser.parse(RSS_URL)

if feed.entries:
    latest_job = feed.entries[0]
    
    # إرسال أحدث وظيفة موجودة حالياً
    send_job_to_telegram(latest_job.title, latest_job.link, latest_job.description)
    print(f"✅ تم إرسال وظيفة: {latest_job.title}")
else:
    print("📭 لا توجد وظائف جديدة حالياً.")
