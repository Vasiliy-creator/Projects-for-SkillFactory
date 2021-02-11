#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter
from itertools import combinations


# In[2]:


data = pd.read_csv('movie_bd_v5.csv')
data.sample(5)


# In[54]:


data.describe()


# # Предобработка

# In[3]:


answers = {} # создадим словарь для ответов

# тут другие ваши предобработки колонок например:

#the time given in the dataset is in string format.
#So we need to change this in datetime format
# ...


# In[4]:


# к заданиям начиная с 6-го
data['profit'] = data.revenue - data.budget


# In[6]:


data.head(2)


# In[7]:


# для заданий, где нужны конкретные актёры
data_act = data
data_act['actors'] = data_act.cast.str.split('|')
data_act = data_act.explode('actors')


# In[8]:


data_act.head(2)


# In[9]:


# для заданий, где нужны конкретные жанры
data_genr = data
data_genr['clear_genre'] = data_genr.genres.str.split('|')
data_genr = data_genr.explode('clear_genre')


# In[11]:


data_genr.head(2)


# In[12]:


# для заданий, где нужны конкретные актёры и жанры
data_act_genr = data_act
data_act_genr['clear_genre'] = data_act_genr.genres.str.split('|')
data_act_genr = data_act_genr.explode('clear_genre')


# In[14]:


data_act_genr.head(2)


# In[52]:


# для заданий, где нужны конкретный режиссер и жанр
data_dir_genr = data_genr
data_dir_genr['clear_dir'] = data_dir_genr.director.str.split('|')
data_dir_genr = data_dir_genr.explode('clear_dir')


# In[56]:


data_dir_genr.head(5)


# In[16]:


# для заданий, где нужны конкретные компании
data_comp = data
data_comp['company'] = data_comp.production_companies.str.split('|')
data_comp = data_comp.explode('company')


# In[17]:


data_comp.head(2)


# In[18]:


# для заданий, где нужны конкретные месяцы
data_month = data
data_month['release_date'] = data_month.release_date.str.split('/')
data_month['month'] = data_month.release_date.apply(lambda x: x[0])


# In[19]:


data_month.head(2)


# In[94]:


# для заданий, где нужны конкретный режиссер и месяц
data_month_dir = data_month
data_month_dir['clear_dir'] = data_month_dir.director.str.split('|')
data_month_dir = data_month_dir.explode('clear_dir')


# In[95]:


data_month_dir.head(2)


# # 1. У какого фильма из списка самый большой бюджет?

# Использовать варианты ответов в коде решения запрещено.    
# Вы думаете и в жизни у вас будут варианты ответов?)

# In[20]:


answers


# In[21]:


# в словарь вставляем номер вопроса и ваш ответ на него
# Пример: 
#answers['1'] = '2. Spider-Man 3 (tt0413300)'
# запишите свой вариант ответа
answers['1'] = 'Pirates of the Caribbean: On Stranger Tides (tt1298650)'
# если ответили верно, можете добавить комментарий со значком "+"
#+


# In[8]:


# тут пишем ваш код для решения данного вопроса:


# ВАРИАНТ 2

# In[22]:


data[data.budget==data.budget.max()].original_title


# In[10]:


# можно добавлять разные варианты решения


# # 2. Какой из фильмов самый длительный (в минутах)?

# In[24]:


# думаю логику работы с этим словарем вы уже поняли, 
# по этому не буду больше его дублировать
answers['2'] = 'Gods and Generals (tt0279111)'


# In[23]:


# здесь детальные данные об актёрах не нужны и можно считать агрегированно
# поэтому используется data_1
data[data.runtime==data.runtime.max()]


# # 3. Какой из фильмов самый короткий (в минутах)?
# 
# 
# 
# 

# In[61]:


data[data.runtime==data.runtime.min()]


# In[25]:


answers['3'] = 'Winnie the Pooh (tt1449283)'


# # 4. Какова средняя длительность фильмов?
# 

# In[62]:


data.runtime.mean()


# In[27]:


answers['4'] = 110


# # 5. Каково медианное значение длительности фильмов? 

# In[63]:


data.runtime.median()


# In[29]:


answers['5'] = 107


# # 6. Какой самый прибыльный фильм?
# #### Внимание! Здесь и далее под «прибылью» или «убытками» понимается разность между сборами и бюджетом фильма. (прибыль = сборы - бюджет) в нашем датасете это будет (profit = revenue - budget) 

# In[19]:


# лучше код получения столбца profit вынести в Предобработку что в начале


# In[64]:


data[data.profit==data.profit.max()]


# In[30]:


answers['6'] = 'Avatar (tt0499549)'


# In[36]:


answers


# # 7. Какой фильм самый убыточный? 

# In[65]:


data[data.profit==data.profit.min()]


# In[33]:


answers['7'] = 'The Lone Ranger (tt1210819)'


# # 8. У скольких фильмов из датасета объем сборов оказался выше бюджета?

# In[66]:


len(data[data.profit >0])


# In[35]:


answers['8'] = 1478


# # 9. Какой фильм оказался самым кассовым в 2008 году?

# In[67]:


films_2008 = data[(data.release_year==2008)]


# In[68]:


films_2008[films_2008.revenue==films_2008.revenue.max()]


# In[37]:


answers['9'] = 'The Dark Knight (tt0468569)'


# # 10. Самый убыточный фильм за период с 2012 по 2014 г. (включительно)?
# 

# In[41]:


films_12_14 = data[(data.release_year>=2012)&                   (data.release_year<=2014)]


# In[42]:


films_12_14[films_12_14.profit==films_12_14.profit.min()]


# In[39]:


answers['10'] = 'The Lone Ranger (tt1210819)'


# In[40]:


answers


# # 11. Какого жанра фильмов больше всего?

# In[34]:


# эту задачу тоже можно решать разными подходами, попробуй реализовать разные варианты
# если будешь добавлять функцию - выноси ее в предобработку что в начале


# In[43]:


#1-й способ
data_genr.clear_genre.describe()


# In[44]:


# 2-й способ
data_genr.clear_genre.value_counts()


# ВАРИАНТ 3

# In[ ]:


'''В данном варианте сначала создаётся словарь c жанрами, 
    затем упорядочивается по значениям'''


# In[75]:


# создаётся словарь
genr_dict = {}
for i in data_genr.clear_genre:
    if i in genr_dict:
        genr_dict[i]+=1
    else:
        genr_dict[i]=1


# In[76]:


'''ниже из существующего словаря создаётся словарь, упорядоченный по значениям'''
sorted_values = sorted(genr_dict.values())
sorted_dict = {}

for i in sorted_values:
    for k in genr_dict.keys():
        if genr_dict[k]==i:
            sorted_dict[k] = genr_dict[k]
            break


# In[77]:


# словарь, упорядоченный по значениям:
sorted_dict


# In[45]:


answers['11'] = 'Drama'


# # 12. Фильмы какого жанра чаще всего становятся прибыльными? 

# In[46]:


#детализированно:
data_genr[data_genr.profit>0].    clear_genre.value_counts()


# In[47]:


answers['12'] = 'Drama'


# # 13. У какого режиссера самые большие суммарные кассовые сборы?

# In[48]:


data.groupby('director')[['budget']].sum()        .sort_values('budget',ascending=False)


# In[49]:


answers['13'] = 'Peter Jackson'


# # 14. Какой режисер снял больше всего фильмов в стиле Action?

# In[63]:


# используется df с очищеными жанрами и режиссёрами

data_dir_genr[data_dir_genr.clear_genre.str.contains('Action')]        .clear_dir.value_counts()


# In[61]:


answers['14'] = 'Robert Rodriguez'


# In[62]:


answers


# # 15. Фильмы с каким актером принесли самые высокие кассовые сборы в 2012 году? 

# В заданиях 15-16 используется data_act с очищенными актёрами

# In[83]:


# фильмы 2012:
data_act_2012 = data_act[data_act.release_year==2012]
# актёры и их выручка:
data_act_2012.groupby('actors')[['revenue']]    .sum().sort_values('revenue',ascending=False)


# In[64]:


answers['15'] = 'Chris Hemsworth'


# # 16. Какой актер снялся в большем количестве высокобюджетных фильмов?

# In[65]:


data_act[data_act.budget>data_act.budget.mean()]    .groupby('actors')[['imdb_id']].count()    .sort_values('imdb_id', ascending=False).head(15)


# In[66]:


# 2-й способ
data_act[data_act.budget>data_act.budget.mean()]    .actors.value_counts().head(15)


# In[73]:


answers['16'] = 'Matt Damon'


# In[83]:


answers


# # 17. В фильмах какого жанра больше всего снимался Nicolas Cage? 

# в задаче используется df c очищенными актёрами и жанрами data_act_genr

# In[76]:


data_act_genr[data_act_genr.actors=='Nicolas Cage']    .clear_genre.value_counts()


# In[78]:


answers['17'] = 'Action'


# # 18. Самый убыточный фильм от Paramount Pictures

# In[ ]:


В этой и 20-й задаче используется df c очищенными студиями data_comp


# In[107]:


data_comp_paramaunt = data_comp[data_comp.company=='Paramount Pictures']
data_comp_paramaunt[data_comp_paramaunt.profit==data_comp_paramaunt.profit.min()]


# In[79]:


answers['18'] = 'K-19: The Widowmaker (tt0267626)'


# # 19. Какой год стал самым успешным по суммарным кассовым сборам?

# In[80]:


data.groupby('release_year')[['revenue']].sum().sort_values('revenue', ascending = False)


# In[81]:


answers['19'] = 2015


# # 20. Какой самый прибыльный год для студии Warner Bros?

# In[82]:


# Warner Bros записан по-разному, поэтому ищется вхождение слова Warn
data_comp[data_comp.company.str.contains('Warn')]    .groupby('release_year')[['profit']]    .sum().sort_values('profit', ascending = False)


# In[84]:


answers['20'] = 2014


# # 21. В каком месяце за все годы суммарно вышло больше всего фильмов?

# В задачах 21-23 используется df с месяцами data_month

# In[91]:


data_month.head(2)


# In[85]:


# 1-й способ
data_month.month.value_counts()


# In[87]:


# 2-й способ
data_month.groupby('month').imdb_id.count().sort_values()


# In[88]:


answers['21'] = 'Сентябрь'


# # 22. Сколько суммарно вышло фильмов летом? (за июнь, июль, август)

# In[145]:


len(data_month.query('month in ["6", "7", "8"]'))


# In[89]:


answers['22'] = 450


# # 23. Для какого режиссера зима – самое продуктивное время года? 

# Используется df, где чистые режиссёры и месяцы

# In[96]:


winter = data_month_dir.query('month in ["12","1", "2"]')
winter.head(5)


# In[97]:


winter.groupby('clear_dir')[['original_title']].count().sort_values('original_title')


# In[98]:


answers['23'] = 'Peter Jackson'


# # 24. Какая студия дает самые длинные названия своим фильмам по количеству символов?

# В этой задаче и в 25 используется df data_comp, где перечислены конкретные компании

# In[190]:


data_comp['f_length'] = data_comp.original_title.apply(lambda x: len(x))


# In[196]:


data_comp.groupby('company')[['f_length']].max().sort_values('f_length')


# In[101]:


answers['24'] = 'Four By Two Productions'


# # 25. Описание фильмов какой студии в среднем самые длинные по количеству слов?

# In[107]:


data_comp['overview_length'] = data_comp.overview.apply(lambda x: len(x))


# In[108]:


data_comp.head(2)


# In[109]:


data_comp.groupby('company')[['overview_length']]    .mean().sort_values('overview_length')


# In[110]:


answers['25'] = 'Midnight Picture Show'


# # 26. Какие фильмы входят в 1 процент лучших по рейтингу? 
# по vote_average

# In[112]:


# функция quantile ниже вычисляет 99-й квантиль
border = np.quantile(data.vote_average, 0.99)
border


# In[113]:


last_quartile = data[data.vote_average>=border].original_title


# In[114]:


last_quartile


# In[116]:


answers['26'] = 'Inside Out, The Dark Knight, 12 Years a Slave'


# In[129]:


answers


# # 27. Какие актеры чаще всего снимаются в одном фильме вместе?
# 

# In[125]:


data=pd.read_csv('movie_bd_v5.csv')
data['cast'] = data.cast.apply(lambda x:x.split('|'))

''' Функция combinations() модуля itertools (используется ниже) 
    возвращает итератор со всеми возможными комбинациями 
    элементов входной последовательности'''

data['comb'] = data.cast.apply(lambda x: list(combinations(x,2)))


# In[126]:


# в столбце comb - списки, содержащие комбинации актёров по 2
data.comb


# In[ ]:


# разделение по элементам списка
data = data.explode('comb')


# In[128]:


data.comb


# In[122]:


''' Метод most_common класса Counter- 
    возвращает список из n наиболее распространенных элементов 
    и их количество от наиболее распространенных до наименее'''
Counter(data.comb).most_common()


# In[130]:


answers['27'] = 'Daniel Radcliffe & Rupert Grint'


# ВАРИАНТ 2

# # Submission

# In[131]:


# в конце можно посмотреть свои ответы к каждому вопросу
answers


# In[132]:


# и убедиться что ни чего не пропустил)
len(answers)

