import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

def sieve(n):
    is_prime = bytearray([1]) * (n + 1)
    is_prime[0] = is_prime[1] = 0
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            is_prime[i*i::i] = bytearray(len(is_prime[i*i::i]))
    return is_prime

K = 100 
size = 2 * K + 1
grid = np.zeros((size, size), dtype=int)

is_prime = sieve(size * size + 10)

x, y = K, K 
grid[y][x] = 1
num = 2
dx, dy = 1, 0   
steps = 1        
turned = 0      

while num <= size * size:
    for _ in range(steps):
        x += dx
        y += dy
        if 0 <= x < size and 0 <= y < size:
            grid[y][x] = num
        num += 1
        if num > size * size:
            break
    dx, dy = dy, -dx
    turned += 1
    if turned == 2:
        turned = 0
        steps += 1

prime_mask = np.vectorize(lambda v: 1 if v > 1 and is_prime[v] else 0)(grid)

fig, ax = plt.subplots(figsize=(9, 9), dpi=150)

ax.imshow(1 - prime_mask, cmap='gray', vmin=0, vmax=1, interpolation='nearest')

ax.set_title(f'Prime numbers in the square spiral (layers $k = 0$ to $k = {K}$)',
             fontsize=13, pad=12)
ax.set_xticks([])
ax.set_yticks([])


ax.plot(K, K, 'r+', markersize=8, markeredgewidth=1.5)
plt.savefig("spiral_primes.png", dpi=400, bbox_inches='tight', pad_inches=0)
