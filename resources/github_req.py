import pandas as pd
import datetime


def get_last_data():
    yesterday=datetime.date.today() - datetime.timedelta(days=1)

    date=yesterday.strftime("%m-%d-%Y")

    df=pd.read_csv(f'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{date}.csv')
    return df

def get_data(date=datetime.date.today().strftime("%m-%d-%Y")):
    df=pd.read_csv(f'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{date}.csv')
    return df

def get_state_list(country='Spain'):
    df = pd.read_csv(
        f'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/UID_ISO_FIPS_LookUp_Table.csv')
    df.dropna(subset=['Province_State'],inplace=True)
    df.drop(df[df['Province_State']=='Unknown'].index,inplace=True)
    return df[df['Country_Region']==country]['Province_State'].to_list()


