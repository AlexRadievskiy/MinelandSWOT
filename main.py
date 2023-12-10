import pandas as pd
import plotly.express as px

# Чтение данных для первого графика
df_orders = pd.read_csv('data_orders.csv')

# Создание интерактивного bubble chart для заказов
fig_orders = px.scatter(df_orders, x='sales', y='cost', size='sales', text='name', hover_name='name',
                        size_max=60, title='Bubble Chart of Products')
fig_orders.update_traces(textposition='top center')

# Отображение первого графика
fig_orders.show()

# Чтение данных
df_first_order = pd.read_csv('data_first_order_after_reg.csv')

# Создание столбчатого графика
fig_first_order = px.bar(df_first_order, x='days_to_first_purchase', y='number_of_players',
                         text='average_spend', title='Number of Players and Average Spend by Days to First Purchase')

# Настройка внешнего вида графика
fig_first_order.update_traces(texttemplate='%{text:.2f}', textposition='inside')
fig_first_order.update_layout(xaxis_title='Days to First Purchase',
                              yaxis_title='Number of Players',
                              xaxis=dict(tickmode='linear'))

# Отображение графика
fig_first_order.show()