import folium
import pandas as pd

def plot_cities_by_country(cities_df, country):

    country_cities = cities_df[cities_df['country'] == country]
    
   
    first_city = country_cities.iloc[0]
    city_map = folium.Map(location=[first_city['lat'], first_city['lon']], zoom_start=5)
    
  
    for _, city in country_cities.iterrows():
        folium.Marker([city['lat'], city['lon']], popup=city['name']).add_to(city_map)
    
    return city_map

def plot_cities_by_density(cities_df, min_density, max_density):
   
    density_cities = cities_df[(cities_df['density'] >= min_density) & (cities_df['density'] <= max_density)]
  
    first_city = density_cities.iloc[0]
    city_map = folium.Map(location=[first_city['lat'], first_city['lon']], zoom_start=5)
    
    
    for _, city in density_cities.iterrows():
        folium.Marker([city['lat'], city['lon']], popup=city['name']).add_to(city_map)
    
    return city_map


# density_map = plot_cities_by_density(cities_df, min_density=1000, max_density=5000)
# density_map.save('density_cities_map.html')
# cities_df should be a DataFrame containing 'name', 'lat', 'lon', 'country', and other relevant columns
# cities_df = pd.read_csv('path_to_cities_data.csv')
# country_map = plot_cities_by_country(cities_df, 'CountryName')
# country_map.save('country_cities_map.html')
