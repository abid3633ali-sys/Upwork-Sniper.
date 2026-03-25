import requests

TOKEN = "8343143091:AAHua7xDAYqwIExQYn3p1130W6rrbaRed7E"
CHAT_ID = "7665460040"

def send_test():
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    text = "مرحبا يا علي، أنا أعمل الآن من داخل GitHub بكفاءة قوية جداً! 🚀"
    payload = {"chat_id": CHAT_ID, "text": text}
    
    # محاولة الإرسال
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        print("✅ نجحت العملية! الرسالة في طريقها لهاتفك.")
    else:
        print(f"❌ فشل GitHub في الإرسال. الخطأ: {response.text}")

if __name__ == "__main__":
    send_test()
