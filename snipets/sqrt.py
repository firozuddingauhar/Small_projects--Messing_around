# def sqrt(n):
#     if n < 0: return "Value Error: math domain error"
#     if n == 0: return 0 
#     s = 1
#     for i in range(1,1000):
#         s = (s + float(n/s))*1.0/2.0
#     return s
def sqrt_recursive(n, low, high):
    if low > high:
        return None
    if n == 0 or n == 1:
        return n
    mid = (low + high) // 2
    mid_squared = mid * mid
    if mid_squared == n:
        return mid
    elif mid_squared < n:
        return sqrt_recursive(n, mid + 1, high)
    else:
        return sqrt_recursive(n, low, mid - 1)
n = int(input("Enter a perfect square : "))
print("Square root of", n, ":", sqrt_recursive(n, 1, n))