unit_power = float(input("Unit Power: "))
weight = float(input("Peso: "))
htm = 100
speed = ((unit_power * 2 * htm) / weight) * 1.4
min_speed_kmh = 300
runway_length = (min_speed_kmh / speed) * 1000
print(f"runway: {runway_length:.0f}")
