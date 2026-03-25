mport requests

# بيانات الربط الخاصة بك
TOKEN = "8343143091:AAHua7xDAYqwIExQYn3p1130W6rrbaRed7E"
CHAT_ID = "7665460040"

def test_bot():
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    message = "مرحبا انا اعمل جيداا 🚀"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    
    print("جاري محاولة إرسال الرسالة...")
    response = requests.post(url, data=payload)
    
    if response.status_code == 200:
        print("✅ تم الإرسال بنجاح! تحقق من تليجرام.")
    else:
        print(f"❌ فشل الإرسال. خطأ رقم: {response.status_code}")
        print(f"السبب: {response.text}")

if __name__ == "__main__":
    test_bot()
