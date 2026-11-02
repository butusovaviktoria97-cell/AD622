import dash_ag_grid as dag
from dash import Dash, html, dcc,callback, Input, Output
import pandas as pd
import plotly.express as px
from openpyxl.styles.builtins import output

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')


app = Dash()

app.layout = [
    html.Div(children=['Мое приложение с использованием Dash, отображение графика и панели управления']),
    html.Hr(),
    dcc.RadioItems(options=['pop', 'lifeExp', 'gdpPercap'],value='lifeExp', id='controls-and-radio-item'),
    dag.AgGrid(
        rowData=df.to_dict('records'),
        columnDefs=[{'field': i} for i in df.columns]
    ),
    dcc.Graph(figure={}, id="controls-and-graph"),
]

@callback(
    Output(component_id='controls-and-graph', component_property='figure'),
    Input(component_id='controls-and-radio-item', component_property='value')
)
def update_graph(col_chosen): # для смены данных при нажатии радиокнопки
    fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg')
    return fig

if __name__ == '__main__':
    app.run(debug=True)