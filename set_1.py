import math
def savings(gross_pay, tax_rate, expenses):
    tax_rate_applied = math.floor(gross_pay * (1 - tax_rate))
    take_home_pay = tax_rate_applied - expenses
    return take_home_pay

def material_waste(total_material, material_units, num_jobs, job_consumption):
    remaining_material = total_material - (num_jobs * job_consumption)
    return f"{remaining_material} {material_units}"

def interest(principal, rate, periods):
    final_value = math.floor(principal * (1 + (rate * periods)))
    return final_value

print(savings(500000, 0.12, 200000))
print(savings(1000000, 0.20, 500000))

print(material_waste(100, "kg", 4, 10))
print(material_waste(500, "L", 10, 25))

print(interest(100000, 0.05, 10))
print(interest(500000, 0.02, 5))