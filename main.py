import requests

# بياناتك الخاصة
TOKEN = "8343143091:AAHuA7xDAyqwIExQYn3p1l3OW6rrbaRed7E"
CHAT_ID = "7665460040"

def send_confirmation():
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    
    # رسالة احترافية للتاكيد
    message = (
        "✅ **تأكيد التشغيل السحابي**\n\n"
        "🚀 أهلاً بك! هذا التنبيه يؤكد أن نظام القناص يعمل الآن بنجاح من **GitHub Actions**.\n\n"
        "💻 الحالة: متصل (Online)\n"
        "⏰ التوقيت: جاري المراقبة كل 10 دقائق."
    )
    
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }

    try:
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            print("✅ الرسالة وصلت تليجرام بنجاح!")
        else:
            print(f"❌ فشل: {response.text}")
    except Exception as e:
        print(f"⚠️ خطأ: {e}")

if __name__ == "__main__":
    send_confirmation()
