import pywapi # Read about the API


class WeatherHandler(object):
    def __init__(self):
        self.bulgaria_code = 'BUXX0005'

    def get_current_weather(self):
        weather_forecast = pywapi.get_weather_from_weather_com(
            self.bulgaria_code, units='metric')
        last_updated = weather_forecast['current_conditions'][
                           'last_updated'].split(' ')[1:3]
        hour_minutes = last_updated[0].split(':')
        hour = hour_minutes[0]
        minutes = int(hour_minutes[1])
        hour_minutes = '%s oclock and %s minutes' % (hour, minutes)
        type_of_weather = weather_forecast['current_conditions']['text']
        station = weather_forecast['current_conditions']['station'].split(
            ',')[0]
        current_temp = weather_forecast['current_conditions']['temperature']
        feels_like = weather_forecast['current_conditions']['feels_like']
        wind_speed = weather_forecast['current_conditions']['wind']['speed']

        forecast_to_read = 'It is %s in %s. The temperature is %s degrees and ' \
                        'it feels like %s degrees. The wind speed is %s ' \
                        'kilometers per hour. This forecast was updated at ' \
                        '%s.' % (type_of_weather, station, current_temp,
                                 feels_like, wind_speed, hour_minutes)
        return forecast_to_read
