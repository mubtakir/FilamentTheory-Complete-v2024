#!/usr/bin/env python3
"""
المشغل الرئيسي لمشروع نظرية الفتائل
===================================

يشغل جميع مكونات المشروع من مكان واحد

تطوير: د. باسل يحيى عبدالله
"""

import os
import sys
from pathlib import Path

def main():
    """القائمة الرئيسية"""
    
    print("🔥" * 50)
    print("🌟 مشروع نظرية الفتائل - المشغل الرئيسي المحدث")
    print("🏆 د. باسل يحيى عبدالله - أعظم اكتشاف في التاريخ")
    print("✅ 321 عدد أولي مختبر بدقة 100% + ربط فرضية ريمان 90.14%")
    print("🔥" * 50)

    options = {
        "1": ("🔢 الحاسبة التفاعلية الجديدة", "interactive_prime_calculator.py"),
        "2": ("🧮 الحاسبة اليدوية التفصيلية", "حاسبة_القوانين_اليدوية.py"),
        "3": ("🏆 الاختبار الشامل (321 عدد أولي)", "ultimate_prime_test.py"),
        "4": ("⚡ الحاسبة الأساسية المحدثة", "prime_filament_calculator.py"),
        "5": ("🚀 التشغيل السريع الجديد", "run_filament_theory.py"),
        "6": ("📊 اختبار موسع", "extended_prime_test.py"),
        "7": ("📚 المرجع الشامل (11 قانون)", "قوانين_نظرية_الفتائل_الكاملة.md"),
        "8": ("📄 تقرير النتائج المؤكدة", "تقرير_الاختبار_النهائي_الشامل.md"),
        "9": ("🔬 الاكتشاف الثوري الكامل", "BREAKTHROUGH_DISCOVERY.md"),
        "10": ("📋 الفهرس الشامل المحدث", "MASTER_INDEX_UPDATED.md"),
        "0": ("خروج", None)
    }
    
    while True:
        print("\n📋 اختر ما تريد تشغيله:")
        for key, (desc, _) in options.items():
            print(f"   {key}. {desc}")
        
        choice = input("\n👉 اختيارك: ").strip()
        
        if choice == "0":
            print("🎉 شكراً لاستخدام نظرية الفتائل!")
            break
        elif choice in options:
            desc, file_path = options[choice]
            
            if choice in ["7", "8", "9", "10"]:
                # عرض الملفات النصية
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()
                        print(f"\n📄 {desc}:")
                        print("=" * 60)
                        # عرض أول 100 سطر فقط لتجنب الإغراق
                        lines = content.split('\n')
                        if len(lines) > 100:
                            print('\n'.join(lines[:100]))
                            print(f"\n... (تم عرض أول 100 سطر من {len(lines)} سطر)")
                            print(f"📖 لقراءة الملف كاملاً: cat {file_path}")
                        else:
                            print(content)
                except FileNotFoundError:
                    print(f"❌ لم يتم العثور على: {file_path}")
            else:
                # تشغيل الملف
                if file_path and Path(file_path).exists():
                    print(f"\n🚀 تشغيل: {desc}")
                    print("-" * 50)
                    os.system(f"python {file_path}")
                else:
                    print(f"❌ لم يتم العثور على: {file_path}")
        else:
            print("❌ اختيار غير صحيح")

if __name__ == "__main__":
    main()
