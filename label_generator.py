import pandas as pd

date='5/11/2024'


df = pd.read_csv('tatoeba_en_ja.csv')
filtered_row = df.loc[100:110]

labels = []
gloss=[]

for index, row in filtered_row.iterrows():
    label = f"# ::id ja:{index} ::date {date} \n# ::snt {row['ja']}\n# ::gls {row['en']}\n \n"
    gloss.append(f"{row['en']}\n")
    labels.append(label)

def write_to_txt(lst, filepath):
    with open(filepath,'w') as file:
        for item in lst:
            file.write(item)
write_to_txt(labels, 'labels.txt')
write_to_txt(gloss, "en_gloss.txt")