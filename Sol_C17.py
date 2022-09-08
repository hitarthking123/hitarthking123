import matplotlib.pyplot as plt

Age = [19, 18, 28, 33, 32, 31, 46, 37, 37, 60, 25, 62, 23, 56, 27, 19, 52, 23, 56]

Medical_Expenditure = [16884, 1725, 4449, 21984, 3866, 3756, 8240, 7281, 6406, 28923, 2721, 27808, 1826, 11090, 39611, 1837, 10797, 2395, 10602]

BMI = [27.9, 33.77, 33, 22.705, 28.88, 25.74, 33.44, 27.74, 29.83, 25.84, 26.22, 26.29, 34.4, 39.82, 42.13, 24.6, 30.78, 23.845, 40.3]

New_Age=[]

for i in range(len(Age)):
    if BMI[i] <=30:
        New_Age.append(Age[i])

plt.xlabel("Age")
plt.ylabel("Count")
plt.hist(New_Age)
plt.show()

plt.xlabel("BMI")
plt.ylabel("Medical Expenditure")
plt.scatter(BMI, Medical_Expenditure)
plt.show()

plt.xlabel("BMI")
plt.ylabel("Medical Expenditure")
plt.bar(BMI, Medical_Expenditure)
plt.show()
