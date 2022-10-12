import pandas as pd

df = pd.read_csv('C:/Users/paulg/Documents/Coding/Witzig/CSV to Excel/iss_data.csv')

#df.to_excel(r'C:/Users/paulg/Documents/Coding/Witzig/CSV to Excel/iss_data.xlsx', index = None, header=True)

for i in range(len(df)):
    print(f"[{df['lattitude'][i]},{df['longitude'][i]}]")
    
with open('C:/Users/paulg/Documents/Coding/Witzig/CSV to Excel/iss_data.txt', 'w+') as f:
    for i in range(len(df)):
        f.write(f"[{df['lattitude'][i]},{df['longitude'][i]}]\n")    