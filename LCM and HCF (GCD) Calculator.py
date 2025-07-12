def compute_hcf(x, y):
    while y:
        x, y = y, x % y
    return x

def compute_lcm(x, y):
    hcf = compute_hcf(x, y)
    return abs(x * y) // hcf

# Input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

hcf = compute_hcf(a, b)
lcm = compute_lcm(a, b)

print(f"\n HCF (GCD) of {a} and {b} is: {hcf}")
print(f"  LCM of {a} and {b} is: {lcm}")
