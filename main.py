import requests

# بياناتك الصحيحة التي نجحت في VS Code
TOKEN = "8343143091:AAHua7xDAYqwIExQYn3p1130W6rrbaRed7E"
CHAT_ID = "7665460040"

def send_test():
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    text = "مرحبا يا علي، أنا أعمل الآن من داخل GitHub بكفاءة! 🚀"
    
    payload = {"chat_id": CHAT_ID, "text": text}
    
    print("⏳ جاري محاولة الإرسال من خوادم GitHub...")
    response = requests.post(url, data=payload)
    
    if response.status_code == 200:
        print("✅ نجحت العملية! تحقق من هاتفك.")
    else:
        print(f"❌ فشل الإرسال. كود الخطأ: {response.status_code}")
        print(f"السبب: {response.text}")

if __name__ == "__main__":
    send_test()
