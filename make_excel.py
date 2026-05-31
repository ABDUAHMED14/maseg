import csv
import time
import random
import requests

# بياناتك الحقيقية من UltraMsg
INSTANCE_ID = "instance175934" 
TOKEN = "01g3aic4yw935q7i"
URL = f"https://api.ultramsg.com/{INSTANCE_ID}/messages/chat"

def send_whatsapp(phone_number, text):
    payload = {
        "token": TOKEN,
        "to": phone_number,
        "body": text
    }
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    try:
        response = requests.post(URL, data=payload, headers=headers)
        return response.json()
    except Exception as e:
        return f"Error: {e}"

# ملف الأرقام الصحيحة بعد التعديل
csv_file_path = "customers.csv"

print("🚀 بدء حملة الإرسال الإعلانية بمعدل رسالة كل 25 ثانية تقريباً...")

with open(csv_file_path, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    
    for index, row in enumerate(reader):
        phone = row['Phone'].strip()
        name = row['Name'].strip()
        
        random_code = random.randint(1000, 9999)
        
        # نص رسالتك الإعلانية الاحترافية
        message_body = (
            f"أهلاً يا أستاذ {name}،\n\n"
            f"📢 لأي صاحب بيزنس 👇 (مكاتب – سوبر ماركت – محلات موبايلات – أي نشاط)\n\n"
            f"لسه بتعتمد على جروبات واتساب في إدارة شغلك؟ 🤔\n"
            f"خلي شغلك يبقى احترافي وسيطر عليه بسهولة من مكان واحد!\n\n"
            f"💻 مع موقع خاص بيك تقدر:\n"
            f"✔ تدير شغلك بدل زحمة الواتساب\n"
            f"✔ تعرض منتجاتك أو خدماتك بشكل منظم وجذاب\n"
            f"✔ تستقبل طلبات العملاء بسهولة\n"
            f"✔ يكون ليك صفحة تحكم كاملة تدير منها الموقع بنفسك\n"
            f"✔ تتحكم في كل حاجة بكل سهولة وسلاسة\n"
            f"✔ نظام موثوق وآمن 100%\n\n"
            f"🛠 وكمان:\n"
            f"✔ دعم فني في أي وقت مني شخصيًا 🤝\n\n"
            f"🚀 كبر شغلك وخلي شكلك قدام العملاء احترافي\n\n"
            f"💰 بأقل سعر في السوق والسعر هيصدمك\n\n"
            f"📲 تواصل واتساب:\n"
            f"01080630060\n\n"
            f"ابدأ دلوقتي وخلي شغلك في مستوى تاني 🔥\n\n"
            f"--- \n"
            f"لوقف استقبال هذه الرسائل أرسل (إلغاء). [Ref: {random_code}]"
        )
        
        print(f"[{index + 1}] جاري الإرسال إلى {phone} ({name})...")
        
        # الإرسال الفعلي
        result = send_whatsapp(phone, message_body)
        print(f"النتيجة: {result}")
        
        # ⏱️ تحديد وقت الانتظار (اختر الطريقة التي تفضلها واحذف الأخرى):
        
        # الطريقة الأولى (الموصى بها للحماية): وقت عشوائي متوسطه 25 ثانية
        wait_time = random.randint(20, 30) 
        
        # الطريقة الثانية (إذا كنت تريدها 25 ثانية جامدة وبدون تغيير):
        # wait_time = 25 
        
        print(f"⏳ انتظار {wait_time} ثانية قبل الانتقال للرقم التالي...\n")
        time.sleep(wait_time)

print("✅ تم الانتهاء من إرسال الحملة بالكامل.")
