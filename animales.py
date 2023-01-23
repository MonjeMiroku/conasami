import plotly
from plotly.offline import plot
import plotly.graph_objs as go
import pandas as pd
import plotly.express as px
animales = ['jirafas', 'monmos', 'perres']

df = pd.read_csv(r'Ingreso_laboral.csv',encoding='ISO-8859-1',delimiter=',')

# fig = go.Figure([
#     go.Bar(x=df['trim'], y=df['ingreso'],marker_color="red", name="trazo1")
# ])
# fig = go.Figure(go.Scatter(x=df['trim'], y=[10,20,30,100,1400,1600], marker_color="blue", name="trazo2"))
fig = px.line(df,x="trim",y="ingreso" ,color="s1_02")
fig2 = px.line(df,x="trim",y="area")

fig3= [fig,fig2]

fig3.update_layout(
    title="Ingresos Laborales por Trimestre",
    xaxis_tickfont_size=30,
    yaxis=dict(
        title="Trimestre",
        titlefont_size=14,
        tickfont_size=14,
    ),
    legend=dict(
        x=2,
        y=1.0,
        bgcolor='rgba(255,255,255,0)',
        bordercolor='rgba(2255,255,255,0)'
    )
)
fig.show()