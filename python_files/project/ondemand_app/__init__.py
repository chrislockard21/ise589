import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from lib import *

# Creates a Dash app using a Flask server
app = dash.Dash(__name__)

# Sets up data object and cleans missing values and string dates
oda_data = Data()
oda_data.dataframe_filled(oda_data._csv_path)
oda_data.convert_str_date_column(oda_data.dataframe, 'CreateDate')

# Returns a pandas dataframe of all product tracks
# Only reports tracks that have occured in the most current month eliminating
# double counting of months (i.e. if it is 2018, January of 2017 will not be
# considered)
product_total_by_month = product_total_tracks_monthly(oda_data.dataframe)

# Time tuple to evaluate data based on 'Days back'
times = (1, 7, 30, 365)

# Stores keys from the product dataframe
ordered_product_list = [
    product_total_by_month[key]
    for key in product_total_by_month
]

# Stores all months with appropriate numbers
month_dict = {
    '1': 'January', '2': 'February', '3': 'March',
    '4': 'April', '5': 'May', '6': 'June',
    '7': 'July', '8': 'August', '9': 'September',
    '10': 'October', '11': 'November', '12': 'December'
}

# Current month
month = dt.datetime.now().month

# Initializes empty lists to store the data based on the current month
ordered_current_month = []
x_axis = []

# This section will evaluate and store the monthly data based on the current
# month that is being considered (i.e. if it is October, than October will
# be the first month processed and later plotted)
if month == 12:

    for key, value in month_dict.items():
        x_axis.append(value)

elif month == 1:
    ordered_product_list.reverse()

    for key, value in month_dict.items():
        x_axis.append(value)
    x_axis.reverse()

else:
    k = 12 - month

    for n in range(month + 1, month + k + 1):
        ordered_current_month.append(product_total_by_month['set ' + str(n)])
        x_axis.append(month_dict[str(n)])

    for n in range(1, month + 1):
        ordered_current_month.append(product_total_by_month['set ' + str(n)])
        x_axis.append(month_dict[str(n)])

# Initializes empty product lists (these are the products plotted)
sas_ue = []
soda = []
ext_web = []
other = []
viya = []

# Appends dictionary value (number of tracks) to each appropriate product
# list based on the key
for dict in ordered_current_month:
    sas_ue.append(dict['SAS University Edition Basic vApp'])
    soda.append(dict['SAS OnDemand for Academics'])
    ext_web.append(dict['External Web'])
    other.append(dict['Other'])
    viya.append(dict['SAS Viya Trial'])

# Packs the lists to be ploted with plotly
data = [
    sets_to_pack(x_axis, sas_ue, 'SAS UE'),
    sets_to_pack(x_axis, soda, 'SODA'),
    sets_to_pack(x_axis, ext_web, 'SAS Profile'),
    sets_to_pack(x_axis, other, 'Other'),
    sets_to_pack(x_axis, viya, 'Viya'),
]

# List containing all elements to be rendered in the apps header
header_elements = [
    html.Div([
        html.Div([
            html.Pre('\n\n\n'),
            html.H1(
                'Educational Technologies Support Tracks Information Site'
            )
        ], className='col-md-12 text-center'),
    ], className='row'),
    html.Pre('\n'),
    html.Div([
        html.Div([
            html.Img(src='assets/analytics_u.png'),
            html.Pre('\n\n'),
            html.H3('See the current track information relating to products'),
            html.H3(
                'supported by the Educational Technologies Support Tracks team'
            ),
            html.Pre('\n\n\n'),
        ], className='col-md-12 text-center'),
    ], className='row'),
    html.Pre('\n')
]

footer_elements = [
        html.Div([
            html.Div(
                html.Div([
                    html.Pre('\n'),
                    html.H6(
                        'Educational Technologies Support Tracks'
                        ' Information Site'
                    ),
                    html.P(
                        'Note: this service and it\'s data are'
                        ' confidential to SAS.'
                        ' Please do not distribute this data to anyone'
                        ' other than the project graders.'
                    ),
                ], className='col-lg-12'), className='row'
            )
        ], className='container')
    ]

# Title that apears on the browser tab
app.title = 'Edu Tech Support Tracks Site'

# External CSS (bootstrap)
app.css.append_css({
    "external_url":
    "https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
    })

# Overall app layout containing the header, main plotly graph, and the results
# of the later dropdown call back (id='output-container')
app.layout = html.Div(children=[
    # Header
    html.Div(header_elements, className='jumbotron', style={
        'background': 'url("assets/buildingq.jpg") no-repeat center center',
        'background-size':'cover', 'margin-bottom':'0', 'color':'white',
        'text-shadow':'1px 1px black'
    }),
    html.Div(
        dcc.Graph(
            id='example-graph',
            figure={
                'data': data,
                'layout': {
                    'barmode': 'stack',
                    'paper_bgcolor': 'rgb(229, 239, 255)',
                    'plot_bgcolor': 'rgb(229, 239, 255)',
                }
            }
        ), className='container text-center'),
    html.Div([
        dcc.Dropdown(
            id='prod-dropdown',
            options=[
                {'label': 'SAS University Edition', 'value': 'SASUE'},
                {'label': 'SAS OnDemand for Accademics', 'value': 'SODA'},
                {'label': 'SAS Profile', 'value': 'EXT'},
                {'label': 'Other', 'value': 'OTHER'},
            ]),
        html.Pre('\n\n'),
        html.Div(id='output-container')
    ], className='container'),
    html.Pre('\n\n\n\n\n\n\n\n\n\n\n'),
    html.Div(footer_elements, className='fixed-bottom', style={
        'background-color':'white', 'color':'black'
    })
], style={'background-color':'rgb(229, 239, 255)'})

# Fuction controlling the dropdown. It will render html to the output-container
# based on the dropdown option selected
@app.callback(
    dash.dependencies.Output('output-container', 'children'),
    [dash.dependencies.Input('prod-dropdown', 'value')])
def update_output(value):
    '''
    Renders the html based on the users input in the dropdown
    '''
    # Provides total count for all products in each dataframe
    prod_tracks_per_time = [
        value_counts(oda_data.dataframe, time) for time in times
    ]

    # Packs data for pie charts based on track topics and platforms
    # (Windows, Mac) For SAS Profile, the pie_chart_plat will not render
    pie_chart_topic = topic_dict(oda_data.dataframe, value)
    pie_chart_plat = platform_type(oda_data.dataframe, value)

    # Creates the pie chart object for topic
    labels_topic = list(pie_chart_topic.keys())
    values_topic = list(pie_chart_topic.values())
    trace_topic = go.Pie(labels=labels_topic, values=values_topic)

    # Creates the pie chart object for plat
    labels_plat = list(pie_chart_plat.keys())
    values_plat = list(pie_chart_plat.values())
    trace_plat = go.Pie(labels=labels_plat, values=values_plat)

    # Helpful dictionary for product labels
    product_key = {
        'SASUE':'SAS University Edition', 'SODA': 'SAS OnDemand for Accademics',
        'EXT': 'SAS Profile', 'OTHER':'Other products'
    }

    if value == None:
        pass
    else:
        # Elements to be rendered by the call back function
        call_back_elements = [
            html.H1(product_key[value]),
            html.H4(
                'View current stats as related to {}'.format(product_key[value])
            ),
            html.Pre('\n\n'),
            html.Div([
                html.Div([
                    html.H3('24 Hours Back'),
                    html.H3(prod_tracks_per_time[0][value]),
                ], className='col-md-3 text-center'),
                html.Div([
                    html.H3('7 Days Back'),
                    html.H3(prod_tracks_per_time[1][value]),
                ], className='col-md-3 text-center'),
                html.Div([
                    html.H3('30 Days Back'),
                    html.H3(prod_tracks_per_time[2][value]),
                ], className='col-md-3 text-center'),
                html.Div([
                    html.H3('365 Days Back'),
                    html.H3(prod_tracks_per_time[3][value]),
                ], className='col-md-3 text-center'),
            ], className='row'),
            html.Pre('\n\n'),
            html.Div([
                html.H2('{} Topics'.format(product_key[value])),
                dcc.Graph(
                    id='boo',
                    figure={
                        'data': [trace_topic],
                        'layout': {
                            'paper_bgcolor': 'rgb(198, 220, 255)',
                        }
                    }
                )], style={
                    'border':'5px solid rgb(130, 152, 188)',
                    'border-radius':'15px', 'padding':'20px',
                    'background-color':'rgb(198, 220, 255)'
                    }
            ),
            html.Pre('\n\n'),
        ]

        # Adds the platform pie chart for the products that use platforms
        if value != 'OTHER' and value != 'EXT':

                call_back_elements.append(html.Div([
                    html.H2('{} User OS'.format(product_key[value])),
                    dcc.Graph(
                        id='too',
                        figure={
                            'data': [trace_plat],
                            'layout': {
                                'paper_bgcolor': 'rgb(198, 220, 255)',
                            }
                        }
                    ),html.Pre('\n') ], style={
                        'border':'5px solid rgb(130, 152, 188)',
                        'border-radius':'15px', 'padding':'20px',
                        'background-color':'rgb(198, 220, 255)'
                        }
                ))

        return html.Div(call_back_elements)

server = app.server

if __name__ == '__main__':
    app.run_server(debug=True)
