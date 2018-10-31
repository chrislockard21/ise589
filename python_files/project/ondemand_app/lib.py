import pandas as pd
import datetime as dt
import plotly.graph_objs as go

class Data(object):

    def __init__(self, csv=None, dataframe=None):
        '''
        Initializes the data class
        '''
        self._csv_path = 'track_data.csv'
        self.dataframe = dataframe

    def dataframe_filled(self, csv_path):
        '''
        Returns: pandas_dataframe
        Type: dataframe

        Function:
        Converts a given csv to a pandas dataframe and fills Nan objects with
        a Not Availible string

        Notes:
        This function is designed to take the entire file path to the specified
        csv file. If on Windows provide two forward slashes to avaid unicode
        errors
        '''
        pandas_dataframe = pd.read_csv(csv_path, encoding='utf-8')
        pandas_dataframe.fillna('Not Availible', inplace=True)
        self.dataframe = pandas_dataframe

    def convert_str_date_column(self, dataframe, column_name):
        '''
        Returns: pandas_dataframe
        Type: dataframe

        Function:
        Converts date column from a string date to a datetime object

        Notes:
        This will only work for string time objects
        '''
        dataframe[column_name] = dataframe[column_name].apply(
            lambda x: dt.datetime.strptime(x, '%d%b%Y:%H:%M:%S.%f')
        )


def product_total_tracks_monthly(dataframe):
    '''
    Returns: product_dict
    Type: dictionary

    Function:
    This function will create a dictionary with the key as the month of the
    year, and the value as another dictionary refering to the number of tracks
    per user per that month

    Notes:
    This function will produce a dictionary of tracks that represent the months
    that have occured in this year and this year - 1 to ensure that there is
    no data overlap. The current month will always exclude the this year -1
    data with all other months that have not occured in the current year
    represented by their this year - 1 data.
    '''
    month_dict = {
        '1': 'January', '2': 'February', '3': 'March',
        '4': 'April', '5': 'May', '6': 'June',
        '7': 'July', '8': 'August', '9': 'September',
        '10': 'October', '11': 'November', '12': 'December'
    }

    non_other_products = [
        'External Web', 'SAS University Edition Basic vApp', 'SAS Viya Trial',
    ]

    date = dt.datetime.now()
    product_dict = {}

    for key, value in month_dict.items():
        product_list = []
        for index, row in dataframe.iterrows():
            if row[1].month == int(key) and row[1].year == date.year:
                if row[2][:12].upper() == 'SAS ONDEMAND':
                    product_list.append('SAS OnDemand for Academics')
                elif row[2] not in non_other_products:
                    product_list.append('Other')
                else:
                    product_list.append(row[2])
            elif (row[1].month == int(key) and row[1].year == date.year-1
                and row[1].month != date.month):
                    if row[2][:12].upper() == 'SAS ONDEMAND':
                        product_list.append('SAS OnDemand for Academics')
                    elif row[2] not in non_other_products:
                        product_list.append('Other')
                    else:
                        product_list.append(row[2])

        df = pd.DataFrame({'products': product_list})

        product_dict['set ' + key] = df.products.value_counts().to_dict()

    for month_set, product_totals in product_dict.items():
        for product in non_other_products:
            try:
                if product_totals[product]:
                    pass
            except:
                product_totals[product] = 0
    return product_dict


def sets_to_pack(x, y, label):
    '''
    Returns: product_dict
    Type: Bar object

    Function:
    This function will return a Bar object to be packed and graphed

    Notes:
    N/A
    '''
    trace = go.Bar(
        x = x,
        y = y,
        name = label,
    )
    return trace


def value_counts(dataframe, time_back):
    '''
    Returns: total_prod_tracks
    Type: dictionary

    Function:
    This function returns the three main products (SAS UE, SODA, EXT WEB)

    Notes:
    N/A
    '''
    date = dt.datetime.now()
    day_limit = date - dt.timedelta(days=time_back)
    dataframe_filtered = dataframe[dataframe.CreateDate >= day_limit]
    prod_count = dataframe_filtered.ProductName.value_counts().to_dict()
    total_prod_tracks = {}
    soda_sum = 0
    sas_ue = 0
    ext_web = 0
    other = 0
    for key, value in prod_count.items():
        if key[:12].upper() == 'SAS ONDEMAND':
            soda_sum += value
        elif key == 'SAS University Edition Basic vApp':
            sas_ue += value
        elif key == 'External Web':
            ext_web += value
        else:
            other += value

    total_prod_tracks['SODA'] = soda_sum
    total_prod_tracks['SASUE'] = sas_ue
    total_prod_tracks['EXT'] = ext_web
    total_prod_tracks['OTHER'] = other

    return total_prod_tracks


def topic_dict(dataframe, value):
    '''
    Returns: Topic dictionary
    Type: Dictionary

    Function:
    This function will provide the total number of occurances of all topics
    for each considered product

    Notes:
    N/A
    '''
    other_products = [
        'e-Learning', 'SAS Viya Trial', 'Not Availible', 'Curriculum Pathways',
        'SAS Solutions OnDemand', 'Miscellaneous', 'Web Profile',
        'SAS EVAAS for K-12', 'General Product Information',
        'SAS University Edition Basic for Amazon Marketplace'
    ]
    top_data = []
    if value == 'SASUE':
        for index, row in dataframe.iterrows():
            if row[2] == 'SAS University Edition Basic vApp':
                top_data.append(row[3])
    if value == 'SODA':
        for index, row in dataframe.iterrows():
            if row[2][:12].upper() == 'SAS ONDEMAND':
                top_data.append(row[3])
    if value == 'EXT':
        for index, row in dataframe.iterrows():
            if row[2] == 'External Web':
                top_data.append(row[4])
    if value == 'OTHER':
        for index, row in dataframe.iterrows():
            if row[2] in other_products:
                top_data.append(row[2])

    topic_dataframe = pd.DataFrame({'topic':top_data})

    return topic_dataframe.topic.value_counts().to_dict()


def platform_type(dataframe, value):
    '''
    Returns: Platform dictionary
    Type: Dictionary

    Function:
    This function will provide the total number of occurances of all platform
    names for each considered product

    Notes:
    This function will only consider SAS University Edition and SAS OnDemand
    for Accademics
    '''
    plat = []
    if value == 'SASUE':
        for index, row in dataframe.iterrows():
            if row[2] == 'SAS University Edition Basic vApp':
                plat.append(row[5])
    if value == 'SODA':
        for index, row in dataframe.iterrows():
            if row[2][:12].upper() == 'SAS ONDEMAND':
                plat.append(row[5])
    plat_dataframe = pd.DataFrame({'platform':plat})
    return plat_dataframe.platform.value_counts().to_dict()
