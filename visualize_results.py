#!/usr/bin/env python3
"""
تصور نتائج نظرية الفتائل للأعداد الأولية
Visualize Filament Theory Prime Results
"""

import matplotlib.pyplot as plt
import numpy as np
import json

# إعداد الخط العربي
plt.rcParams['font.family'] = ['DejaVu Sans']

def load_and_visualize():
    """تحميل وتصور النتائج"""
    
    # البيانات من النتائج
    primes = [2, 3, 5, 7, 11]
    frequencies = [1.91e55, 2.86e55, 4.77e55, 6.68e55, 1.05e56]
    cavity_depths = [1.189, 1.316, 1.495, 1.627, 1.821]
    
    zeta_zeros = [14.134725, 21.022040, 25.010858]
    zeta_accuracies = [88.84, 87.56, 94.01]
    
    # إنشاء المخططات
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
    
    # المخطط 1: ترددات الرنين مقابل الأعداد الأولية
    ax1.plot(primes, np.array(frequencies)/1e55, 'bo-', linewidth=2, markersize=8)
    ax1.set_xlabel('Prime Numbers / الأعداد الأولية')
    ax1.set_ylabel('Resonance Frequency (×10⁵⁵ Hz)')
    ax1.set_title('Filament Resonance Frequencies\nترددات الرنين الفتائلية')
    ax1.grid(True, alpha=0.3)
    
    # إضافة قيم على النقاط
    for i, (p, f) in enumerate(zip(primes, frequencies)):
        ax1.annotate(f'{f/1e55:.2f}', (p, f/1e55), 
                    textcoords="offset points", xytext=(0,10), ha='center')
    
    # المخطط 2: أعماق الحفر الفتائلية
    ax2.bar(primes, cavity_depths, color='green', alpha=0.7, width=0.8)
    ax2.set_xlabel('Prime Numbers / الأعداد الأولية')
    ax2.set_ylabel('Cavity Depth / عمق الحفرة')
    ax2.set_title('Filament Cavity Depths\nأعماق الحفر الفتائلية')
    ax2.grid(True, alpha=0.3)
    
    # إضافة قيم على الأعمدة
    for i, (p, d) in enumerate(zip(primes, cavity_depths)):
        ax2.text(p, d + 0.02, f'{d:.3f}', ha='center', va='bottom')
    
    # المخطط 3: دقة التنبؤ لأصفار زيتا
    colors = ['red', 'orange', 'green']
    bars = ax3.bar(range(len(zeta_zeros)), zeta_accuracies, color=colors, alpha=0.7)
    ax3.set_xlabel('Zeta Zero Index / رقم صفر زيتا')
    ax3.set_ylabel('Prediction Accuracy (%) / دقة التنبؤ')
    ax3.set_title('Zeta Zeros Prediction Accuracy\nدقة التنبؤ بأصفار زيتا')
    ax3.set_xticks(range(len(zeta_zeros)))
    ax3.set_xticklabels([f'#{i+1}\n{z:.3f}' for i, z in enumerate(zeta_zeros)])
    ax3.grid(True, alpha=0.3)
    
    # إضافة قيم الدقة
    for i, acc in enumerate(zeta_accuracies):
        ax3.text(i, acc + 1, f'{acc:.1f}%', ha='center', va='bottom')
    
    # المخطط 4: العلاقة بين العدد الأولي وعمق الحفرة
    ax4.scatter(primes, cavity_depths, s=100, c='purple', alpha=0.7)
    
    # خط الاتجاه
    z = np.polyfit(primes, cavity_depths, 1)
    p_trend = np.poly1d(z)
    ax4.plot(primes, p_trend(primes), "r--", alpha=0.8, linewidth=2)
    
    ax4.set_xlabel('Prime Numbers / الأعداد الأولية')
    ax4.set_ylabel('Cavity Depth / عمق الحفرة')
    ax4.set_title('Prime vs Cavity Depth Correlation\nالعلاقة بين العدد الأولي وعمق الحفرة')
    ax4.grid(True, alpha=0.3)
    
    # إضافة معادلة الخط
    ax4.text(0.05, 0.95, f'y = {z[0]:.4f}x + {z[1]:.4f}', 
             transform=ax4.transAxes, bbox=dict(boxstyle="round", facecolor='wheat'))
    
    plt.tight_layout()
    plt.savefig('filament_prime_analysis.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    # إحصائيات إضافية
    print("📊 تحليل إحصائي للنتائج:")
    print(f"متوسط دقة أصفار زيتا: {np.mean(zeta_accuracies):.2f}%")
    print(f"معامل الارتباط (العدد الأولي - عمق الحفرة): {np.corrcoef(primes, cavity_depths)[0,1]:.4f}")
    print(f"معدل نمو تردد الرنين: {(frequencies[-1]/frequencies[0])**(1/(len(frequencies)-1)):.2f}")

if __name__ == "__main__":
    load_and_visualize()
