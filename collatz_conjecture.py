import matplotlib.pyplot as plt

temp = []
x = []
ys = []

real_number_list = []

number_list = input("Enter some starting values: ").split()
iterations = int(input("Enter the number of iterations: "))

for u in number_list:
    u = int(u)
    real_number_list.append(u)

for num in real_number_list:
    for i in range(1, iterations+1):

        r = num % 2
        if r == 1:     #odd
            num = (3*num) + 1
        else:          #even
            num /= 2

        x.append(i)
        temp.append(num)

    ys.append(temp)
    temp = []

x = list(set(x))

# to find longest sequence and peak
peak = 0
lengths = []

for y in ys:
    for y_value in y:
        if y_value > peak:
            peak = y_value

    length = 0

    for end in y:
        if end == 4:
            break
        length += 1

    lengths.append(length)

largest = lengths[0]

for length in lengths:
    if length > largest:
        largest = length
        largest_index = lengths.index(length)
    else:
        largest_index = lengths.index(lengths[0])

print(f"{real_number_list[largest_index]} terminated last")
print(f"{int(peak)} was the highest value reached")

#--------------------------------------------------------------------

plt.title(f"Collatz Conjecture ({iterations} iterations)", family="Tahoma",
                                fontweight="bold")

for idx, y in enumerate(ys):
    plt.plot(x, y, label=real_number_list[idx])

plt.grid("both", alpha=0.3)
plt.xlabel("Iteration")
plt.ylabel("Value")
plt.ylim(0, 1.05*peak)

plt.legend()
plt.tight_layout()

plt.show()
