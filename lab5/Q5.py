def closer_city(lat, lon, city_a, city_b):
    dist_to_a = distance(make_city('temp', lat, lon), city_a)
    dist_to_b = distance(make_city('temp', lat, lon), city_b)
    
    if dist_to_a <= dist_to_b:
        return get_name(city_a)
    else:
        return get_name(city_b)
