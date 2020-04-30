import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Use seaborn to draw plot (needs to be plotted in Matplotlib)
sns.set(style="whitegrid")

# Get parameters from CSV file
Kpdata = pd.read_csv('Kpvalues.csv')
TLdata = pd.read_csv('TLvalues.csv')
TIdata = pd.read_csv('TIvalues.csv')
Taudata = pd.read_csv('Tauvalues.csv')
print(Taudata)

sns.boxplot(x="Control Mode", y=r'$K_p$', hue="Motion", data=Kpdata, palette="Set1")
plt.show()

sns.boxplot(x="Control Mode", y=r'$T_L$', hue="Motion", data=TLdata, palette="Set1")
plt.show()

sns.boxplot(x="Control Mode", y=r'$T_I$', hue="Motion", data=TIdata, palette="Set1")
plt.show()

sns.boxplot(x="Control Mode", y=r'$\tau$', hue="Motion", data=Taudata, palette="Set1")
plt.show()

print("Ready")