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

#--------------------------------------------------------------------

plt.title(f"Collatz Conjecture ({iterations} iterations)", family="Arial",
                                fontweight="bold")

for idx, y in enumerate(ys):
    plt.plot(x, y, label=real_number_list[idx])

plt.grid("both", alpha=0.3)
plt.legend()
plt.tight_layout()

plt.show()
