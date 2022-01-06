import matplotlib.pyplot as plt
from highlight_text import fig_text
from mplsoccer import PyPizza, FontManager
import csv

font_normal = FontManager(("https://github.com/google/fonts/blob/main/apache/roboto/static/"
                           "Roboto-Regular.ttf?raw=true"))
font_italic = FontManager(("https://github.com/google/fonts/blob/main/apache/roboto/static/"
                           "Roboto-Italic.ttf?raw=true"))
font_bold = FontManager(("https://github.com/google/fonts/blob/main/apache/roboto/static/"
                         "Roboto-Medium.ttf?raw=true"))

params = ['Goals', 'Shots', 'Shooting accuracy %', 'Assists', 'Passes per match', 'Big Chances Created', 'Through balls', 'Accurate long balls', 'Tackle success %', 'Duels won']
values = []
values_2 = []
first_name = ''
second_name = ''

with open('stats.csv') as file:
    reader = csv.reader(file)

    next(reader)

    cnt = 0
    for row in reader:
        if cnt == 0:
            first_name = row[0]
            row.remove(row[0])
            for value in row:
                temp_str = value
                temp_str = temp_str.replace("%", "")
                temp_str = temp_str.replace(",", "")
                temp_float = float(temp_str)
                row[row.index(value)] = temp_float
            values = row
            cnt += 1
        else:
            second_name = row[0]
            row.remove(row[0])
            for value in row:
                temp_str = value
                temp_str = temp_str.replace("%", "")
                temp_str = temp_str.replace(",", "")
                temp_float = float(temp_str)
                row[row.index(value)] = temp_float
            values_2 = row

# minimum range value and maximum range value for parameters
min_range = [10, 50, 5, 5, 10, 5, 5, 100, 10, 100]
max_range = [40, 400, 45, 40, 70, 35, 85, 700, 75, 1200]

# instantiate PyPizza class
baker = PyPizza(
    params=params,
    min_range=min_range,        # min range values
    max_range=max_range,        # max range values
    background_color="#222222", straight_line_color="#000000",
    last_circle_color="#000000", last_circle_lw=2.5, other_circle_lw=0,
    other_circle_color="#000000", straight_line_lw=1
)

# plot pizza
fig, ax = baker.make_pizza(
    values,                     # list of values
    compare_values=values_2,    # passing comparison values
    figsize=(8, 8),             # adjust figsize according to your need
    color_blank_space="same",   # use same color to fill blank space
    blank_alpha=0.4,            # alpha for blank-space colors
    param_location=110,         # where the parameters will be added
    kwargs_slices=dict(
        facecolor="#1A78CF", edgecolor="#000000",
        zorder=1, linewidth=1
    ),                          # values to be used when plotting slices
    kwargs_compare=dict(
        facecolor="#ff9300", edgecolor="#222222", zorder=3, linewidth=1,
    ),                          # values to be used when plotting comparison slices
    kwargs_params=dict(
        color="#F2F2F2", fontsize=12, zorder=5,
        fontproperties=font_normal.prop, va="center"
    ),                          # values to be used when adding parameter
    kwargs_values=dict(
        color="#000000", fontsize=12,
        fontproperties=font_normal.prop, zorder=3,
        bbox=dict(
            edgecolor="#000000", facecolor="#1A78CF",
            boxstyle="round,pad=0.2", lw=1
        )
    ),                           # values to be used when adding parameter-values
    kwargs_compare_values=dict(
        color="#000000", fontsize=12,
        fontproperties=font_normal.prop, zorder=3,
        bbox=dict(
            edgecolor="#000000", facecolor="#FF9300",
            boxstyle="round,pad=0.2", lw=1
        )
    )                            # values to be used when adding comparison-values
)

# add title
title = "<" + first_name + "> vs <" + second_name + ">"
fig_text(
    0.515, 0.99, title,
    size=16, fig=fig,
    highlight_textprops=[{"color": '#1A78CF'}, {"color": '#FF9300'}],
    ha="center", fontproperties=font_bold.prop, color="#F2F2F2"
)

# add subtitle
fig.text(
    0.515, 0.942,
    "Premier League | All Seasons | 2016 to Present",
    size=15,
    ha="center", fontproperties=font_bold.prop, color="#F2F2F2"
)

# add credits
CREDIT_1 = "data: statsbomb viz fbref"
CREDIT_2 = "inspired by: @Worville, @FootballSlices, @somazerofc & @Soumyaj15209314"

fig.text(
    0.99, 0.005, f"{CREDIT_1}\n{CREDIT_2}", size=9,
    fontproperties=font_italic.prop, color="#F2F2F2",
    ha="right"
)

plt.show()