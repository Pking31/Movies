# %% [markdown]
# ## WordCloud
# Let's analyze the most frequent words in the columns 'title' and 'overview'

# %%
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


# %%
mo=pd.read_csv('movies_dataset.csv')

# %%
#transforming type of columns 
mo['title']=mo['title'].astype(str)
mo['overview']=mo['overview'].astype(str)

# %%
#create the corpus of document
title_corpus=" ".join(mo['title'])
overview_corpus=" ".join(mo['overview'])

# %%
title_wordcloud=WordCloud(stopwords=STOPWORDS,background_color='white').generate(title_corpus)
plt.figure(figsize=(15,7))
plt.imshow(title_wordcloud)
plt.axis('off')
plt.show

# %%
overview_wordcloud=WordCloud(stopwords=STOPWORDS,background_color='white').generate(overview_corpus)
plt.figure(figsize=(15,7))
plt.imshow(overview_wordcloud)
plt.axis('off')
plt.show

# %% [markdown]
# # ML  
# Define a function that receives a title of movie and return a recomendation like a list of title.
# 

# %%
to=mo[['title','overview']]
to['overview']=to['overview'].fillna("")

# %%
tfidf=TfidfVectorizer(stop_words="english")

tfidf_matriz=tfidf.fit_transform(to['overview'])

# %%
def recomendation(title):
   
    coseno=linear_kernel(tfidf_matriz,tfidf_matriz)
    indices=pd.Series(to.index,index=to['title']).drop_duplicates()
    idx=indices[title]
    simi=list(enumerate(coseno[idx]))
    simi=sorted(simi,key=lambda x:x[1],reversed=True)
    simi=simi[1:10]
    movie_index=[i[0] for i in simi]
    lista=to['title'].iloc[movie_index].to_list()[:5]
    return {'lista recomendada': lista}

# %%
recomendation("Toy Story")


