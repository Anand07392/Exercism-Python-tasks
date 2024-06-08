def is_criticality_balanced(temperature, neutrons_emitted):
    ne=temperature*neutrons_emitted
    if temperature<800 and neutrons_emitted>500 and ne<500000:
        return True
    else:
        return False


def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = voltage * current
    efficiency_percentage = (generated_power / theoretical_max_power) * 100
    if efficiency_percentage >= 80:
        return 'green'
    elif 60 <= efficiency_percentage < 80:
        return 'orange'
    elif 30 <= efficiency_percentage < 60:
        return 'red'
    else:
        return 'black'
        
    
def fail_safe(temperature, neutrons_produced_per_second, threshold):
    product = temperature * neutrons_produced_per_second
    lower_bound = 0.9 * threshold
    upper_bound = 1.1 * threshold
    if product < lower_bound:
        return 'LOW'
    elif lower_bound <= product and product<= upper_bound:
        return 'NORMAL'
    else:
        return 'DANGER'
