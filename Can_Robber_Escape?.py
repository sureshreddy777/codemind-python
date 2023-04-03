def can_escape(n, degrees):
    odd_degrees = sum(1 for d in degrees if d % 2 != 0)
    return "YES" if odd_degrees == 0 or odd_degrees == 2 else "NO"

n = int(input())
degrees = list(map(int, input().split()))

print(can_escape(n, degrees))