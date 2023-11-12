import pyecharts
print(pyecharts.__version__)

import pandas as pd
from pyecharts.charts import Map
from pyecharts import options as opts

data = pd.read_excel('GDP.xlsx')
province = list(data["province"])
gdp = list(data["2019_gdp"])
data_list = [list(z) for z in zip(province, gdp)]

c = (
    Map(init_opts=opts.InitOpts(width="1000px", height="600px"))  # Initialize map size
    .set_global_opts(
        title_opts=opts.TitleOpts(title="2019 Provinces GDP Distribution (unit: 100 million yuan)"),
        # Configure title
        visualmap_opts=opts.VisualMapOpts(type_="scatter")  # Scatter type
    )
    .add("GDP", data_list, maptype="china")  # Take data_list, map type is China Map
    .render("Map1.html")
)
