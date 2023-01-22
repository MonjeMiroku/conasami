from dash import Dash, dcc, html, Input, Output

from dash import Dash, html, dcc

import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

app = Dash(__name__)
# df = px.data.gapminder().query("continent == 'Oceania'")
df = pd.read_csv(r'ind_dem_proyecciones.csv',encoding='ISO-8859-1',delimiter=',')
df2 = pd.read_csv(r'esperanza_de_vidaestado.csv',encoding='ISO-8859-1',delimiter=',')
# df = pd.DataFrame({
#     "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
#     "Amount": [4, 1, 2, 2, 4, 5],
#     "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
# })

# fig = px.bar(df, x="AÑO", y="EDAD_MED", barmode="group")
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


fig = px.scatter(df, x='AÑO', y="RAZ_DEP",  title="Esperanza de vida Indem proyecciones 1950-2050").update_traces(line=dict(color='firebrick', width=4))
fig2 = px.scatter(df, x='AÑO', y="T_BRU_NAT").update_traces(line=dict(color = 'rgba(50,50,50,0.4)'))
fig3 = px.scatter(df, x='AÑO', y="T_BRU_MOR").update_traces(line=dict(color = 'rgba(50,50,50,0.4)'))
fig4 = px.scatter(df, x='AÑO', y="EDAD_MED").update_traces(line=dict(color = 'rgba(50,50,50,0.4)'))

figx = go.Figure(data=fig.data + fig2.data + fig3.data + fig4.data)
#
# fig.data[0].update(mode='lines')

# fig.add_trace(go.Bar(
#     x=months,
#     y=[19, 14, 22, 14, 16, 19, 15, 14, 10, 12, 12, 16],
#     mode='lines+markers',
#     name='Secondary Product',
#     marker_color='lightsalmon'
# ))


# fig = make_subplots(rows=1, cols=2)
# fig.add_trace(go.Scatter(df,x='AÑO',y='EDAD_MED', mode="lines"), row=1, col=1)
#
# fig.add_trace(go.Bar(df,x='AÑO',y='EDAD_MED', mode="bars"), row=1, col=2)


# trazo1 = px.line(df, x='AÑO',y='EDAD_MED',title="Esperanza de vida")
# trazo2 = px.line(df2, x='AÑO',
#                  y='T_BRU_MOR',
#                  mode='lines+markers',
#                  name="Esperanza de vida")
#
# trazo3 = px.line(df2, x='AÑO',
#                  y='RAZ_DEP',
#                  mode='lines+markers',
#                  name="EDAD MEDIANA")

# data = [trazo1]
app.layout = html.Div(children=[
    html.H1(children='CONASAMI'),

    dcc.Graph(
        id='example-graph',
        figure=figx
    ),
dcc.Graph(
        id='example-graph',
        figure=fig
    ),
dcc.Graph(
        id='example-graph',
        figure=fig2
    ),
dcc.Graph(
        id='example-graph',
        figure=fig3
    ),
dcc.Graph(
        id='example-graph',
        figure=fig4
    )

])
app.run_server(debug=True)