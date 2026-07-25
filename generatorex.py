def my_generator(n):
    value = 0
    
    while value < n:
        yield value
        value += 1
        
for v in my_generator(10):
    print(v)     # 0 1 2 3 4 5 6 7 8 9
    

# ---------------------------------------
def gen2():
    name = "Manish"
    for i in name:
        yield i
        
for ch in gen2():
    print(ch)     # M a n i s h