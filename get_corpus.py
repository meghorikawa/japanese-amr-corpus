'''
This is the python script run to compile the parallel corpus
of english and japanese from the HuggingFace tatoeba dataset.

Citataion:

J. Tiedemann, 2012, Parallel Data, Tools and Interfaces in OPUS.
In Proceedings of the 8th International Conference on Language
Resources and Evaluation (LREC 2012)

'''

from datasets import load_dataset
import pandas as pd

dataset = load_dataset("tatoeba", lang1="en", lang2="ja",trust_remote_code=True)

en_ja_pairs=dataset['train']

id_list = []
en_list=[]
ja_list=[]

for item in en_ja_pairs:
  translation = item['translation']
  id_list.append(item['id'])
  en_list.append(translation['en'])
  ja_list.append(translation['ja'])



df = pd.DataFrame(list(zip(id_list, ja_list, en_list)), columns=['id', 'ja', 'en'])

df.to_csv('tatoeba_en_ja.csv', index=False)