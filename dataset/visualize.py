import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('realistic_machine_downtime_data.csv')


sns.set(style="whitegrid")


plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Temperature', y='Run_Time', hue='Downtime_Flag', palette='coolwarm', alpha=0.7)
plt.title('Temperature vs Run Time (Downtime Flag)')
plt.xlabel('Temperature (°C)')
plt.ylabel('Run Time (hours)')
plt.legend(title='Downtime Flag', labels=['No Downtime (0)', 'Downtime (1)'])
plt.show()


plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='Downtime_Flag', y='Temperature', palette='coolwarm')
plt.title('Temperature Distribution for Downtime and No Downtime')
plt.xlabel('Downtime Flag')
plt.ylabel('Temperature (°C)')
plt.xticks([0, 1], ['No Downtime (0)', 'Downtime (1)'])
plt.show()


plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='Downtime_Flag', y='Run_Time', palette='coolwarm')
plt.title('Run Time Distribution for Downtime and No Downtime')
plt.xlabel('Downtime Flag')
plt.ylabel('Run Time (hours)')
plt.xticks([0, 1], ['No Downtime (0)', 'Downtime (1)'])
plt.show()


sns.pairplot(df, hue='Downtime_Flag', palette='coolwarm', vars=['Temperature', 'Run_Time'])
plt.suptitle('Pair Plot of Temperature and Run Time with Downtime Flag', y=1.02)
plt.show()


corr_matrix = df[['Temperature', 'Run_Time', 'Downtime_Flag']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap of Features')
plt.show()

