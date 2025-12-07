def celsius_a_fahrenheit(celsius):
    return celsius*9/5+32
    
temp_c=float(input("Ingrese temperatura en celsius:"))
temp_f=celsius_a_fahrenheit(temp_c)
print(f"{temp_c}°c={temp_f:.2f}°f")
