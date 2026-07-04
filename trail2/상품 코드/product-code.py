product_name, product_code = input().split()
product_code = int(product_code)

class info:
    def __init__(self, product_code = 50, product_name = "codetree"):
        self.product_code = product_code
        self.product_name = product_name
    
Info1 = info()
Info2 = info(product_code, product_name)

print(f"product {Info1.product_code} is {Info1.product_name}")

print(f"product {Info2.product_code} is {Info2.product_name}")