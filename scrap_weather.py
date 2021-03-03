import pandas as pd
weather_data = pd.read_html('https://www.imn.ac.cr/reporte-pronostico-regional')
print(weather_data[0].columns)