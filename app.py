from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_feather('western_cape_rentals_processed.ftr')
df.fillna(0, inplace=True)

df = df[(df['bedrooms'] <= 4) &
        (df['bedrooms'] > 1.5) &
        (df['parking_spaces'] >= 1) &
        (df['rental_term'] == 'monthly') &
        (df['price'] <= 15000) &
        (df['price'] > 5000) &
        (df['location'] == 'De Velde')]

fig = px.box(df, x='bedrooms', y='price', color='address')

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == "__main__":
    app.run_server(debug=True)