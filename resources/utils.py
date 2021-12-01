from resources import github_req
from github_req import get_last_data, get_state_list,get_data
import matplotlib.pyplot as plt
import numpy as np
import datetime



def label_figure(day, mode,func_name='plot'):
	plt.title(f'{mode}, {day}')
	plt.ylabel(f"{mode}")
	plt.tight_layout()
	filename = f'tmp/{func_name}_{mode}_{day.replace("/", "-")}.png'

	plt.savefig(filename)
	plt.close()

def plot_data(df, places, day, mode, column,func_name='plot'):
	n = len(places)
	rgba_colors = np.zeros((n, 4))
	rgba_colors[:, 0] = 1.0

	values = []
	for index, place in enumerate(places):
		provice_data = df[df[column] == place]
		values.append(provice_data.iloc[0][mode])

	alphas=[x/max(values) for x in values]


	alphas = np.array(alphas)
	rgba_colors[:, -1] = alphas.reshape(1, len(values)).flatten()

	plt.bar(places, values, color=rgba_colors)
	plt.xticks(places, rotation='vertical')
	plt.grid()
	label_figure(day, mode,func_name)


def plot_daily_total_cases_country(country='Spain',mode="Confirmed"):

	yesterday = datetime.date.today() - datetime.timedelta(days=1)
	date = yesterday.strftime("%d-%m-%Y")
	df=get_last_data()
	df=df.groupby('Province_State').sum().reset_index()
	day=date
	states=get_state_list(country)
	plot_data(df, states, day, mode, "Province_State",'dailytotal')
	return f'tmp/dailytotal_{mode}_{day.replace("/", "-")}.png'

def plot_daily_new_cases_country(country='Spain',mode="Confirmed"):
	yesterday = datetime.date.today() - datetime.timedelta(days=1)
	yesterday2=yesterday- datetime.timedelta(days=1)
	date_y = yesterday.strftime("%m-%d-%Y")
	date_y2 = yesterday2.strftime("%m-%d-%Y")
	df1=get_data(date_y)
	df2=get_data(date_y2)
	df1[mode]=df1[mode]-df2[mode]
	day=date_y
	states=get_state_list(country)
	plot_data(df1, states, day, mode, "Province_State",'dailynew')
	return f'tmp/dailynew_{mode}_{day.replace("/", "-")}.png'

# plot_daily_total_cases_comunity(get_state_list())
# plot_daily_new_cases_comunity(get_state_list())
