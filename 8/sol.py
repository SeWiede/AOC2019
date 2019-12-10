import sys
import itertools.Counter

lines = sys.stdin

if len(sys.argv) > 1:
	f = open(sys.argv[1], "r")
	lines = f.readlines()

data = lines[0]


pixels = data.strip()
w, h = 25, 6
layers = [pixels[(x * w * h): (x + 1) * w * h] for x in range(len(pixels) // (h * w))]
counters = [Counter(layer) for layer in layers]

c = min(counters, key=lambda x: x['0'])
print(f'part 1: {c["1"] * c["2"]}')

img = layers[0]
for layer in layers[1:]:
    img = [layer[p] if img[p] == '2' else img[p] for p in range(w * h)]

print('part 2:')
for r in range(h):
    print(''.join(img[r * w:(r + 1) * w]).replace('0', ' ').replace('1', 'x'))

