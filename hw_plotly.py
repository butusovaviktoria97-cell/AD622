import plotly.express as px

#Задача 1
# df = px.data.gapminder()
# df = df[df['country'] == 'Canada']
#
# fig = px.bar(df, x= 'year', y='pop', title='Динамика численности населения Канады за период с 1952 по 2007 ')
# fig.update_traces(texttemplate='%{y:,}', textposition='outside')
#
# fig.show()

#Задача 2
df = px.data.tips()
fig = px.sunburst(df, path=['day', 'time','smoker' ],values='total_bill',color='day', color_discrete_sequence=px.colors.qualitative.Pastel, title='Распределение чеков по структуре чаевых')
labels={'day': 'День недели',
        'time': 'Время суток',
        'total_bill': 'Сумма счёта'}
fig.update_layout(margin=dict(t=50, r=25, l=25, b=25))

fig.show()
