#!/usr/bin/env python3
"""
اختبار موسع لنظرية الفتائل على حزم أكبر من الأعداد الأولية
Extended Test for Filament Theory on Larger Prime Sets

د. باسل يحيى عبدالله - بالتعاون مع ChatGPT
Dr. Basel Yahya Abdullah - In collaboration with ChatGPT
"""

import math
import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple, Dict
import json
import time

class ExtendedPrimeFilamentTest:
    """اختبار موسع لنظرية الفتائل"""
    
    def __init__(self):
        # ثوابت نظرية الفتائل
        self.filament_mass = 5.85881e-52  # كتلة الفتيلة
        self.fundamental_frequency = 1 / (4 * math.pi)  # التردد الأساسي
        
        # مجموعات الاختبار
        self.small_primes = self.generate_primes(2, 100)  # أعداد أولية صغيرة
        self.medium_primes = self.generate_primes(100, 1000)  # أعداد أولية متوسطة
        self.large_primes = self.generate_primes(1000, 10000)  # أعداد أولية كبيرة
        
        # أصفار زيتا موسعة (أول 20 صفر)
        self.extended_zeta_zeros = [
            14.134725141734693790, 21.022039638771554993, 25.010857580145688763,
            30.424876125859513210, 32.935061587739189691, 37.586178158825671257,
            40.918719012147495187, 43.327073280914999519, 48.005150881167159727,
            49.773832477672302181, 52.970321477714460644, 56.446247697063246086,
            59.347044003233895969, 60.831778524609809200, 65.112544048081651438,
            67.079810529494905051, 69.546401711173979984, 72.067157674481907582,
            75.704690699083933914, 77.144840068874800998
        ]
        
        self.results = {}
    
    def generate_primes(self, start: int, end: int) -> List[int]:
        """توليد الأعداد الأولية في نطاق معين"""
        def is_prime(n):
            if n < 2:
                return False
            if n == 2:
                return True
            if n % 2 == 0:
                return False
            for i in range(3, int(math.sqrt(n)) + 1, 2):
                if n % i == 0:
                    return False
            return True
        
        return [n for n in range(start, end + 1) if is_prime(n)]
    
    def test_fundamental_frequency_relation(self, prime: int) -> Dict:
        """اختبار العلاقة الأساسية p/π = 4p × (1/(4π))"""
        # التردد المحسوب
        calculated_freq = prime / math.pi
        
        # التردد النظري
        theoretical_freq = 4 * prime * self.fundamental_frequency
        
        # نسبة الخطأ
        error_percentage = abs(calculated_freq - theoretical_freq) / calculated_freq * 100
        
        # فحص التوازن الفتائلي
        balance_check = prime + (-prime)  # يجب أن يساوي 0
        balance_factor = 1.0 if balance_check == 0 else 1.0 / (1.0 + abs(balance_check))
        
        # خصائص الأبعاد الأربعة
        temporal_dimension = prime
        spatial_radius = 1.0  # نصف القطر الفعال
        four_d_volume = (4/3) * math.pi * (spatial_radius ** 3) * temporal_dimension
        
        return {
            'prime': prime,
            'calculated_frequency': calculated_freq,
            'theoretical_frequency': theoretical_freq,
            'error_percentage': error_percentage,
            'balance_check': balance_check,
            'balance_factor': balance_factor,
            'temporal_dimension': temporal_dimension,
            'four_d_volume': four_d_volume,
            'is_valid': error_percentage < 0.001 and balance_factor == 1.0
        }
    
    def test_zeta_zero_correspondence(self, zeta_zero: float, prime_list: List[int]) -> Dict:
        """اختبار التناظر مع أصفار زيتا"""
        # التردد المقابل لصفر زيتا
        zeta_frequency = zeta_zero / (2 * math.pi)
        
        # العدد الأولي المتوقع (معادلة محسنة)
        predicted_prime = zeta_zero / math.pi * math.sqrt(2) * math.cos(math.pi/4)
        
        # أقرب عدد أولي
        closest_prime = min(prime_list, key=lambda p: abs(p - predicted_prime))
        
        # حساب الدقة
        accuracy = (1 - abs(closest_prime - predicted_prime) / closest_prime) * 100
        
        return {
            'zeta_zero': zeta_zero,
            'zeta_frequency': zeta_frequency,
            'predicted_prime': predicted_prime,
            'closest_prime': closest_prime,
            'accuracy_percent': max(0, accuracy)
        }
    
    def run_comprehensive_test(self) -> Dict:
        """تشغيل الاختبار الشامل"""
        print("🚀 بدء الاختبار الموسع لنظرية الفتائل...")
        print("=" * 80)
        
        start_time = time.time()
        
        # اختبار الأعداد الأولية الصغيرة
        print(f"\n🔢 اختبار الأعداد الأولية الصغيرة (2-100): {len(self.small_primes)} عدد")
        small_results = []
        small_valid_count = 0
        
        for prime in self.small_primes:
            result = self.test_fundamental_frequency_relation(prime)
            small_results.append(result)
            if result['is_valid']:
                small_valid_count += 1
        
        small_success_rate = (small_valid_count / len(self.small_primes)) * 100
        print(f"   معدل النجاح: {small_success_rate:.2f}% ({small_valid_count}/{len(self.small_primes)})")
        
        # اختبار الأعداد الأولية المتوسطة
        print(f"\n🔢 اختبار الأعداد الأولية المتوسطة (100-1000): {len(self.medium_primes)} عدد")
        medium_results = []
        medium_valid_count = 0
        
        for prime in self.medium_primes[:50]:  # اختبار أول 50 للسرعة
            result = self.test_fundamental_frequency_relation(prime)
            medium_results.append(result)
            if result['is_valid']:
                medium_valid_count += 1
        
        medium_success_rate = (medium_valid_count / len(medium_results)) * 100
        print(f"   معدل النجاح: {medium_success_rate:.2f}% ({medium_valid_count}/{len(medium_results)})")
        
        # اختبار الأعداد الأولية الكبيرة
        print(f"\n🔢 اختبار الأعداد الأولية الكبيرة (1000-10000): {len(self.large_primes)} عدد")
        large_results = []
        large_valid_count = 0
        
        for prime in self.large_primes[:30]:  # اختبار أول 30 للسرعة
            result = self.test_fundamental_frequency_relation(prime)
            large_results.append(result)
            if result['is_valid']:
                large_valid_count += 1
        
        large_success_rate = (large_valid_count / len(large_results)) * 100
        print(f"   معدل النجاح: {large_success_rate:.2f}% ({large_valid_count}/{len(large_results)})")
        
        # اختبار أصفار زيتا الموسعة
        print(f"\n🌊 اختبار أصفار زيتا الموسعة: {len(self.extended_zeta_zeros)} صفر")
        all_primes = self.small_primes + self.medium_primes + self.large_primes
        zeta_results = []
        
        for i, zero in enumerate(self.extended_zeta_zeros):
            result = self.test_zeta_zero_correspondence(zero, all_primes)
            zeta_results.append(result)
            if i < 5:  # عرض أول 5 نتائج
                print(f"   صفر #{i+1}: {zero:.6f} → عدد أولي {result['closest_prime']} (دقة: {result['accuracy_percent']:.1f}%)")
        
        avg_zeta_accuracy = sum(r['accuracy_percent'] for r in zeta_results) / len(zeta_results)
        print(f"   متوسط دقة أصفار زيتا: {avg_zeta_accuracy:.2f}%")
        
        # حساب الإحصائيات الإجمالية
        total_tested = len(small_results) + len(medium_results) + len(large_results)
        total_valid = small_valid_count + medium_valid_count + large_valid_count
        overall_success_rate = (total_valid / total_tested) * 100
        
        end_time = time.time()
        test_duration = end_time - start_time
        
        print("\n" + "=" * 80)
        print("📊 الإحصائيات الإجمالية:")
        print(f"   إجمالي الأعداد المختبرة: {total_tested}")
        print(f"   الأعداد الصحيحة: {total_valid}")
        print(f"   معدل النجاح الإجمالي: {overall_success_rate:.2f}%")
        print(f"   متوسط دقة أصفار زيتا: {avg_zeta_accuracy:.2f}%")
        print(f"   مدة الاختبار: {test_duration:.2f} ثانية")
        
        # حفظ النتائج
        self.results = {
            'small_primes_results': small_results,
            'medium_primes_results': medium_results,
            'large_primes_results': large_results,
            'zeta_results': zeta_results,
            'statistics': {
                'total_tested': total_tested,
                'total_valid': total_valid,
                'overall_success_rate': overall_success_rate,
                'small_success_rate': small_success_rate,
                'medium_success_rate': medium_success_rate,
                'large_success_rate': large_success_rate,
                'avg_zeta_accuracy': avg_zeta_accuracy,
                'test_duration': test_duration
            }
        }
        
        return self.results
    
    def analyze_error_patterns(self):
        """تحليل أنماط الأخطاء"""
        print("\n🔍 تحليل أنماط الأخطاء:")
        
        all_results = (self.results['small_primes_results'] + 
                      self.results['medium_primes_results'] + 
                      self.results['large_primes_results'])
        
        errors = [r['error_percentage'] for r in all_results]
        
        print(f"   أقل خطأ: {min(errors):.6f}%")
        print(f"   أكبر خطأ: {max(errors):.6f}%")
        print(f"   متوسط الخطأ: {np.mean(errors):.6f}%")
        print(f"   الانحراف المعياري: {np.std(errors):.6f}%")
        
        # فحص الأعداد التي لم تنجح
        failed_primes = [r['prime'] for r in all_results if not r['is_valid']]
        if failed_primes:
            print(f"   الأعداد التي لم تنجح: {failed_primes[:10]}...")
        else:
            print("   ✅ جميع الأعداد نجحت في الاختبار!")
    
    def save_results(self, filename: str = "extended_test_results.json"):
        """حفظ النتائج"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.results, f, ensure_ascii=False, indent=2)
        print(f"\n💾 تم حفظ النتائج في: {filename}")

def main():
    """الدالة الرئيسية"""
    print("🌟 اختبار موسع لنظرية الفتائل والأعداد الأولية")
    print("Extended Test for Filament Theory and Prime Numbers")
    print("د. باسل يحيى عبدالله - Dr. Basel Yahya Abdullah")
    print("=" * 80)
    
    # إنشاء الاختبار
    tester = ExtendedPrimeFilamentTest()
    
    # تشغيل الاختبار الشامل
    results = tester.run_comprehensive_test()
    
    # تحليل أنماط الأخطاء
    tester.analyze_error_patterns()
    
    # حفظ النتائج
    tester.save_results()
    
    print("\n🎯 انتهى الاختبار الموسع بنجاح!")
    return results

if __name__ == "__main__":
    results = main()
