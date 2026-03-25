mport requests
import sys

# بياناتك
TOKEN = "8343143091:AAHua7xDAYqwIExQYn3p1130W6rrbaRed7E"
CHAT_ID = "7665460040"

def send_final_test():
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID, 
        "text": "🔥 نداء من GitHub: هل تسمعني يا علي؟ النظام متصل الآن!"
    }
    
    print(f"📡 محاولة الاتصال بتليجرام...")
    try:
        response = requests.post(url, data=payload, timeout=15)
        print(f"📬 حالة الرد من تليجرام: {response.status_code}")
        print(f"💬 نص الرد: {response.text}")
        
        if response.status_code == 200:
            print("✅ مبروك! الرسالة وصلت لهاتفك الآن.")
        else:
            print("❌ تليجرام استلم الطلب ولكنه رفض إرساله. راجع الـ Token.")
            
    except Exception as e:
        print(f"🚨 خطأ فني أثناء الاتصال: {e}")
        sys.exit(1)

if __name__ == "__main__":
    send_final_test()
