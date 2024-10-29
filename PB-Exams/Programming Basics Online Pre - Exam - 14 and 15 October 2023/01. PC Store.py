price_for_cpu = float(input())
price_for_gpu = float(input())
price_for_ram = float(input())
number_of_ram = int(input())
percentage_discount = float(input())
lev = 1.57

price_for_cpu_lv = price_for_cpu * lev
price_for_gpu_lv = price_for_gpu * lev
price_for_ram_lv = price_for_ram * lev
total_price_ram = price_for_ram_lv * number_of_ram
cpu_discount = price_for_cpu_lv - price_for_cpu_lv * percentage_discount
gpu_discount = price_for_gpu_lv - price_for_gpu_lv * percentage_discount
total_price = cpu_discount + gpu_discount + total_price_ram

print(f"Money needed - {total_price:.2f} leva.")
