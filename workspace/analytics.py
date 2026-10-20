from typing import Any, Dict, List, Optional
import time

"""
DevPulse AI - Python Algorithmic Analysis Demo
Demonstrates data processing, statistics, and algorithm simulation.
"""
import time
import math
import random

def calculate_analytics(data):
    total = sum(data)
    n = len(data)
    mean = total / n
    variance = sum((x - mean) ** 2 for x in data) / n
    std_dev = math.sqrt(variance)
    return {
        "count": n,
        "sum": total,
        "mean": round(mean, 2),
        "std_dev": round(std_dev, 2),
        "min": min(data),
        "max": max(data)
    }

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

if __name__ == "__main__":
    print("🚀 DevPulse AI Engine - Running Python Environment")
    print("-" * 50)
    
    # Generate dataset
    random.seed(42)
    sample_data = [random.randint(10, 100) for _ in range(25)]
    print(f"📊 Raw Dataset ({len(sample_data)} samples):")
    print(sample_data[:10], "... [truncated]")
    
    # Calculate stats
    stats = calculate_analytics(sample_data)
    print("\n📈 Descriptive Statistics:")
    for k, v in stats.items():
        print(f"   • {k.capitalize()}: {v}")
        
    # Sort
    start_t = time.perf_counter()
    sorted_data = quick_sort(sample_data)
    dur = (time.perf_counter() - start_t) * 1000
    print(f"\n⚡ QuickSort completed in {dur:.3f} ms:")
    print("   Sorted:", sorted_data[:10], "...")
    print("\n✅ Execution successful!")
