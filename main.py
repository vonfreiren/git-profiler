import pandas as pd
import yaml

with open('config.yaml') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)

url = data['url']
path_movies = data['save_path_local_wishlist_movies']
path_series = data['save_path_local_wishlist_series']

df_files = pd.read_csv(url)
df_files.sort_values('Position', ascending=False, inplace=True)
df_files['Title'] = '<a href="' + df_files['URL'] + '" target="_blank">'+df_files['Title']+'</a>'
df_files = df_files.filter(['Title', 'Title Type', 'IMDb Rating', 'Year', 'Genres', 'Release Date (month/day/year)'])

df_movies = df_files[df_files['Title Type'] == 'movie']
df_series = df_files[(df_files['Title Type'] == 'tvSeries') | (df_files['Title Type'] == 'tvMiniSeries')]

df_series.drop(['Title Type'], axis=1, inplace=True)
df_movies.drop(['Title Type'], axis=1, inplace=True)

df_movies.to_html(path_movies, index=False, classes='table-responsive table-bordered', table_id='table_movies', border=0, escape=False, justify='center', col_space=100, na_rep='N/A')
df_series.to_html(path_series, index=False, classes='table-responsive table-bordered', table_id='table_series', border=0, escape=False, justify='center', col_space=100, na_rep='N/A')