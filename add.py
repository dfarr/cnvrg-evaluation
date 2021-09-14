import sys

a = int(sys.argv[1])
b = int(sys.argv[1])

print("*************************")
print(f"Computing: {a} + {b}")
print("*************************")

with open("output/sum.txt", "w") as f:
    f.write(str(a + b))
