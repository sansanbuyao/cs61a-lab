def distance(city_a, city_b):
    return sqrt((get_lat(city_a) - get_lat(city_b))**2 + (get_lon(city_a) - get_lon(city_b))**2)
