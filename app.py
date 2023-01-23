from dash import Dash, dcc, html, Input, Output

from dash import Dash, html, dcc
import numpy as np
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

app = Dash(__name__)
# df = px.data.gapminder().query("continent == 'Oceania'")
df = pd.read_csv(r'sm_hist.csv', encoding='ISO-8859-1', delimiter=',')
df2 = pd.read_csv(r'sbc_zona.csv', encoding='ISO-8859-1', delimiter=',')

df3 = pd.read_csv(r'smg18_actual.csv', encoding='ISO-8859-1', delimiter=',')
# df2 = pd.read_csv(r'esperanza_de_vidaestado.csv',encoding='ISO-8859-1',delimiter=',')
# df = pd.DataFrame({
#     "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
#     "Amount": [4, 1, 2, 2, 4, 5],
#     "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
# })

# fig = px.bar(df, x="AÑO", y="EDAD_MED", barmode="group")
# months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
#           'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


# fig2 = px.line(df, x='AÑO', y="T_BRU_NAT").update_traces(line=dict(color = 'rgba(50,50,50,0.4)'))
# fig3 = px.line(df, x='AÑO', y="T_BRU_MOR").update_traces(line=dict(color = 'rgba(50,50,50,0.4)'))
# fig4 = px.line(df, x='AÑO', y="EDAD_MED").update_traces(line=dict(color = 'rgba(50,50,50,0.4)'))

# figx = go.Figure(data=fig.data + fig2.data + fig3.data + fig4.data)
# #
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
app.layout = html.Div([

    html.Div(
        className="wrapper",
        children=[
            html.Div(
                className="column1",
                children=[
                    html.H1("CONASAMI"),
                    dcc.Dropdown(id='dropdown', options=[
                        {'label': 'Salario mínimo histórico', 'value': 'A'},
                        {'label': 'Evolución del salario mínimo general', 'value': 'B'},
                        {'label': 'Canasta básica urbana cubierta por el salario mínimo', 'value': 'C'}],
                                 value='A'),
                    # dcc.Checklist(['New York City', 'Montreal', 'San Francisco'], ['Montreal'],inline=True)

                ]

            ),
            html.Div(
                className="column2",
                children=[
                    dcc.Graph(id='graph-court')
                ]
            ),
            html.Div(
                className="column3",
                children=[

                ]
            ),
            html.Div(
                className="column4",
                children=[
                   html.Footer(
                       children=[
                           html.A("contacto@good1.cloud", href='mailto:contacto@good1.cloud', target="_blank")
                       ]
                   )
                ]
            )
        ]
    ),

])


# Histórico', 'Saslario mínimo', 'Indicadores IMSS'], 'Histórico
def create_figure():
    # fig = px.bar(df, x='anio', y="sm_pa", color="NPSM", color_discrete_sequence=["#691c32", "#bc955c"],
    #              labels=dict(sm_pa="Salario mínimo (Pesos diarios)", anio="Año", NPSM="NPSMxxx"))
    # fig.update_traces(showlegend=False)
    # fig.update_layout(hovermode=False)
    # fig.update_layout(
    #
    #     hoverlabel_align='right',
    #     title={
    #         'text': "Salario mínimo en México 1976 - 2022 <br> Pesos de septiembre de 2022",
    #         'y': 0.9,
    #         'x': 0.5,
    #         'xanchor': 'center',
    #         'yanchor': 'top',
    #     })

    # layout = go.Layout(title="TITULO",
    #                    xaxis=dict(title="titulo x"),
    #                    yaxis=dict(title="titulo y"))
    rounded_data = df.round({"sm_pa": 2})
    data = px.bar(rounded_data, x='anio', y="sm_pa", color="NPSM", color_discrete_sequence=["#691c32", "#bc955c"],
                  labels=dict(sm_pa="Salario mínimo (Pesos diarios)", anio="Año", NPSM="NPSM"))

    # data = px.line(df, x='anio', y="sm_pa", color="NPSM", color_discrete_sequence=["#691c32", "#bc955c"],
    #               labels=dict(sm_pa="Salario mínimo (Pesos diarios)", anio="Año", NPSM="NPSMxxx"))

    fig = go.Figure(data=data)
    fig.update_traces(showlegend=False)
    return fig


def create_figure2():
    # layout = go.Layout(title="TITULO",
    #                    xaxis=dict(title="titulo x"),
    #                    yaxis=dict(title="titulo y"))
    rounded_data = df2.round({"SBC": 2})
    concat_day = pd.to_datetime(df2[['year', 'month']].assign(DAY=1))

    # new_salary_280 = df2[df2["SBC"] < 280].index.tolist()
    # print(new_salary_280)
    data = px.line(rounded_data, x=concat_day, y="SBC", color="Zona",
                   color_discrete_sequence=["#bc955c", "#235b4e"],
                   labels={
                       "x": "Año",
                       "SBC": "Pesos diarios",

                   })

    # data = px.line(df, x='anio', y="sm_pa", color="NPSM", color_discrete_sequence=["#691c32", "#bc955c"],
    #               labels=dict(sm_pa="Salario mínimo (Pesos diarios)", anio="Año", NPSM="NPSMxxx"))
    fig = go.Figure(data=data)

    return fig
def create_figure3():
    # layout = go.Layout(title="TITULO",
    #                    xaxis=dict(title="titulo x"),
    #                    yaxis=dict(title="titulo y"))
    rounded_data = df3.round({"SMG": 2})
    # new_salary_280 = df2[df2["SBC"] < 280].index.tolist()
    # print(new_salary_280)
    data = px.line(rounded_data, x="fecha", y="SMG", color="zona",
                   color_discrete_sequence=["#235b4e","#bc955c"],
                   labels={
                       "SMG": "Porcentaje",
                       "fecha": "Año",

                   })

    # data = px.line(df, x='anio', y="sm_pa", color="NPSM", color_discrete_sequence=["#691c32", "#bc955c"],
    #               labels=dict(sm_pa="Salario mínimo (Pesos diarios)", anio="Año", NPSM="NPSMxxx"))
    fig = go.Figure(data=data)

    return fig

@app.callback(Output('graph-court', 'figure'),
              [Input('dropdown', 'value')])
def update_figure(selected_value):
    if selected_value == 'A':

        fig = create_figure()

    elif selected_value == 'B':
        fig = create_figure2()
    else:
        fig = create_figure3()
    # agrega otro trazo
    # fig.add_trace(go.Scatter(x=[x], y=[y], marker=dict(size=15, color='green'), mode='markers'))

    return fig


# data = [trazo1]
# app.layout = html.Div([
#     html.Div(
#         className="app-header",
#         children=[
#             html.Div('Plotly Dash', className="app-header--title")
#         ]
#     ),
#     html.Div(
#         children=html.Div([
#             html.H5('Overview'),
#             html.Div('''
#                 This is an example of a simple Dash app with
#                 local, customized CSS.
#             '''),
# dcc.Graph(
#         id='example-graph',
#         figure=fig
#     )
#         ])
#     )
# ])
app.run_server(debug=True)
