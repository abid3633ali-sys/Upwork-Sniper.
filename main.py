import requests

# بياناتك الصحيحة
TOKEN = "8343143091:AAHua7xDAYqwIExQYn3p1130W6rrbaRed7E"
CHAT_ID = "7665460040"

def send_test():
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    # الرسالة التي طلبتها
    text = "مرحبا يا علي، أنا أعمل بكفاءة قوية من داخل GitHub 🚀"
    
    payload = {
        "chat_id": CHAT_ID,
        "text": text
    }
    
    print("⏳ جاري محاولة إرسال الرسالة من خوادم GitHub...")
    response = requests.post(url, data=payload)
    
    if response.status_code == 200:
        print("✅ نجحت العملية! تفقد هاتفك الآن.")
    else:
        print(f"❌ فشل الإرسال من GitHub. كود الخطأ: {response.status_code}")
        print(f"السبب: {response.text}")

if __name__ == "__main__":
    send_test()
