import matplotlib.pyplot as plt
data = open('data.txt','r').read().split('\n')
print(data)
plt.plot(data)
plt.ylabel('wild tigers')
plt.show()