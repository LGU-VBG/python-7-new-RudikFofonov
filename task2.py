def update_car_info(**kwargs):
    car_info = kwargs
    
    car_info['is_available'] = True
    
    return car_info

result = update_car_info(brand='Toyota', price=30000)

print(result)
