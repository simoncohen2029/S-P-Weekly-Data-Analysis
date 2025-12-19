import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("SP_Weekly_Data.csv")

df["Date"] = pd.to_datetime(df["Date"])
df["Close"] = df["Close"].str.replace(",", "").astype(float)
df = df.sort_values("Date").reset_index(drop=True)

# graph 1
plt.figure(figsize=(8, 5))

df_beginning = df.iloc[0:29]

plt.plot(df_beginning["Date"], df_beginning["Close"], marker="o", linewidth=2)

plt.ylim(5000, 6200)
plt.yticks(range(5000, 6201, 100))
plt.xticks(df_beginning["Date"][::5])
plt.xlabel("Time (Weeks)")
plt.ylabel("Close Price ($)")
plt.title("S&P 500 Index Close Price (12/13/24 to 7/3/25)")
plt.savefig('SP_Data_12-13-24_to_7-3-25.png')
plt.tight_layout()
plt.show()


#graph 2

plt.figure(figsize=(8, 5))

df_end = df.iloc[29:]

plt.plot(df_end["Date"], df_end["Close"], marker="o", linewidth=2)

plt.ylim(6000, 7000)
plt.yticks(range(6000, 7001, 100))
plt.xticks(df_end["Date"][::5])
plt.xlabel("Time (Weeks)")
plt.ylabel("Close Price ($)")
plt.title("S&P 500 Index Close Price (7/3/25 to 12/8/25)")
plt.savefig('SP_Data_7-3-25_to_12-8-25.png')
plt.tight_layout()
plt.show()
