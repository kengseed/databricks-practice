# Databricks notebook source
print("echo")


# COMMAND ----------

import random
import matplotlib.pyplot as plt

# Generate a list of random numbers
random_numbers = [random.randint(1, 100) for _ in range(100)]

# Plot a histogram of the random numbers
plt.hist(random_numbers, bins=10)
plt.xlabel('Number')
plt.ylabel('Frequency')
plt.title('Histogram of Random Numbers')
plt.show()

# COMMAND ----------

print ("hello cmd 3")
