from dash import Dash, html

app = Dash() # инициализация приложения. фрейворк - библиотека пайтона и достоточно вызвать одну строку чтобы за нами сделал много

app.layout = [html.Div(children='Hello world!!!')] # определяем пакеты в список добавлен 1 компонент div


if __name__ == '__main__': # 
    app.run(debug=True) #запуск приложения. ebug=True - для показа ошибок