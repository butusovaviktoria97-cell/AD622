# import pandas as pd
# import plotly.express as px

# months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август']
# temp= [-8.4, -5.9, 1.7, 9.3, 15.1, 20.7, 23.5, 22.1]
# year = [2026] * len(months)
#
# df = pd.DataFrame(
#     {
#         'Month': months,
#         'Temperature': temp,
#         'Year': year
#
#     }
# )
# fig = px.bar(df, x='Month', y='Temperature',color='Month',animation_frame='Year', title="Средняя температура в Нижнем Новгороде", labels={"Month": "Месяц", "Temperature": "Температура"})
# fig.update_layout(yaxis_range=[-10, 25], xaxis_range=["Январь", "Август"])
#
# fig.show()

import dash_ag_grid as dag
from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px


app = Dash()

app.layout = [
    html.H1(children=['Мой первый дашборд']),
    html.Hr(),
]
x_values = [1, 2, 3, 4, 5]
y_values = [1,4,9,16,25]

df = pd.DataFrame({'X': x_values, 'Y': y_values })
fig_line_chart = px.line( df, x='X', y='Y',title="График функции y=x2", labels={"X": "Значение X", "Y": "Значение Y"})

app.layout.append(dcc.Graph(figure=fig_line_chart))

if __name__ == '__main__':
    app.run(debug=True)





