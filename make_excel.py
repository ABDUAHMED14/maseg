import csv
import random

# قائمة ببعض الأسماء الوهمية للتنويع
first_names = ["أحمد", "محمد", "محمود", "علي", "عمر", "مصطفى", "كريم", "خالد", "إبراهيم", "يوسف", "هاني", "أيمن"]
last_names = ["أمين", "الخطيب", "سعيد", "منصور", "صالح", "عزت", "شاكر", "حسن", "فوزي", "عبد الله"]

# أكواد شبكات المحمول في مصر
prefixes = ["10", "11", "12", "15"]

print("⏳ جاري توليد 1000 رقم واسم عشوائي...")

# إنشاء ملف CSV متوافق تماماً مع سكريبت الإرسال
with open('customers.csv', mode='w', newline='', encoding='utf-8') as file:
    fieldnames = ['Phone', 'Name']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    # كتابة الهيدر (رأس الجدول)
    writer.writeheader()
    
    # توليد 1000 سطر
    for i in range(1, 1001):
        # اختيار شبكة عشوائية
        prefix = random.choice(prefixes)
        # توليد باقي الرقم (7 أرقام عشوائية)
        rest_of_number = "".join([str(random.randint(0, 9)) for _ in range(8)])
        # تركيب الرقم بالصيغة الدولية لمصر
        full_phone = f"20{prefix}{rest_of_number}"
        
        # تركيب اسم عشوائي
        full_name = f"{random.choice(first_names)} {random.choice(last_names)}"
        
        # كتابة السطر في الملف
        writer.writerow({'Phone': full_phone, 'Name': full_name})

print("✅ تم إنشاء ملف 'customers.csv' بنجاح ويحتوي على 1000 رقم جاهز!")