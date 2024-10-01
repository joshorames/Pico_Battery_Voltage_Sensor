import machine
import time

# Define the ADC pin
adc_pin = machine.ADC(26)  # GP26

# Resistor values
R1 = 3300  # 3.3kΩ
R2 = 1000  # 1kΩ

def read_battery_voltage():
    #error
    error=
    # Read ADC value (0 to 65535)
    adc_value = adc_pin.read_u16()  # 16-bit ADC reading
    # Calculate the input voltage at the ADC pin
    voltage_at_adc = (adc_value / 65535) * 3.3
    # Calculate the actual battery voltage
    battery_voltage = voltage_at_adc * (R1 + R2) / R2
    return battery_voltage

try:
    while True:
        battery_voltage = read_battery_voltage()
        print(f"Battery Voltage: {battery_voltage:.2f} V")
        time.sleep(1)

except KeyboardInterrupt:
    print("Exiting...")
