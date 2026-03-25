import requests

# بيانات الربط الصحيحة
TOKEN = "8343143091:AAHua7xDAYqwIExQYn3p1130W6rrbaRed7E"
CHAT_ID = "7665460040"

def test_bot():
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": "مرحبا انا اعمل جيداا 🚀\nلقد نجح الربط بين GitHub وتليجرام!"
    }
    
    print("جاري الإرسال...")
    response = requests.post(url, data=payload)
    
    if response.status_code == 200:
        print("✅ وصلت الرسالة! تحقق من هاتفك.")
    else:
        print(f"❌ خطأ {response.status_code}: {response.text}")

if __name__ == "__main__":
    test_bot()
