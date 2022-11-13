#Instalando a biblioteca WorldCloud
!pip install wordcloud -q

# Importando os pacotes necessários
import numpy as np
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

data_rj = '/content/drive/MyDrive/portfolio/ciencia_de_dados/trabalho_3/listings.csv'

df = pd.read_csv(data_rj)
#Primeiras linhas da tabela
df.head()

# Quantidade de valores ausentes
print("Valores ausentes para name: ", df.name.isnull().sum())

# Eliminando as colunas com valores ausentes
name = df.dropna(subset=['name'], axis=0)['name']

# Concatenando as palavras
all_name = " ".join(s for s in name)

print("Quantidade de Palavras: {}".format(len(all_name)))

# Lista de stopword
stopwords = set(STOPWORDS)
stopwords.update(["da", "meu", "em", "você", "de", "ao", "os"])
# Gerando uma wordcloud
wordcloud = WordCloud(stopwords=stopwords,
                      background_color="black").generate(all_name)

# Mostrando a imagem final
fig, ax = plt.subplots(figsize=(12,6))
ax.imshow(wordcloud, interpolation='bilinear')

plt.tight_layout()

# Endereço local da imagem
sing_image = np.array(Image.open("/content/drive/MyDrive/portfolio/ciencia_de_dados/trabalho_3/redentor.jpg"))
   
# Gerando uma wordcloud
wordcloud3 = WordCloud(stopwords=stopwords,
                      background_color="black",
                      width=1000, height=1000, max_words=500,
                      mask=sing_image, max_font_size=200,
                      min_font_size=.5, contour_width=3, contour_color='steelblue').generate(all_name)
 
# Mostrando a imagem final
fig, ax = plt.subplots(figsize=(10,10))
ax.imshow(wordcloud3, interpolation='bilinear')
ax.set_axis_off()
 
plt.imshow(wordcloud3);
wordcloud3.to_file("/content/drive/MyDrive/portfolio/ciencia_de_dados/trabalho_3/cristo_redentor.png")
