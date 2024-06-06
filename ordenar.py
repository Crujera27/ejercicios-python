import random

nums = [random.randint(1, 1000) for _ in range(20)]

print("1. Los 20 números generados:")
print(nums)

nums_ordenados = sorted(nums)

print("\n2. Los 20 números ordenados:")
print(nums_ordenados)
num_biggest = max(nums)
num_smallest = min(nums)
print("\n3. El número mayor es:", num_biggest)
print("   El número menor es:", num_smallest)
media = sum(nums) / len(nums)
print("\n4. La media de los números es:", media)
