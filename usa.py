import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas as pd


app = dash.Dash()
app.config.suppress_callback_exceptions = True

data = {'x': [1, 2, 3, 1, 2, 3], 'y': [4, 1, 2, 6, 1, 4], 'name': ["USA", "USA", "USA", "CAN", "CAN", "CAN"]}
df= pd.DataFrame(data)
variable_indicators = df["name"].unique()

app.layout = html.Div([
 	dcc.Dropdown(
		id="variable_choice",
		options=[{"label": i, "value": i} for i in variable_indicators]
		),

	html.Div([

		], id="example-graph")
])

@app.callback(
    Output("example-graph", "children"),
    [Input("variable_choice", "value")],
    [State("example-graph", "children")])

def update_graph_1(variable_name, children):
	dff = df[df["name"]==variable_name]
	if variable_name:
		if children:
			children[0]["props"]["figure"] = {"data": [dict(x=dff.x, y=dff.y, type="bar")]}
		else:
			children.append(
				dcc.Graph(
					figure={"data": [dict(x=dff.x, y=dff.y, type="bar")]})
						)
	return children

if __name__ == '__main__':
    app.run_server(debug=True)