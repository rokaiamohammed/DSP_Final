import plotly.graph_objects as go

import pandas as pd

data_file = 'customed_DB.xlsx'

dataset = pd.read_excel(data_file)
dates= ["2020-12-31",
"2020-01-01","2020-01-02","2020-01-03","2020-01-04","2020-01-05","2020-01-06","2020-01-07","2020-01-08","2020-01-09","2020-01-10"
,"2020-01-11","2020-01-12","2020-01-13","2020-01-14","2020-01-15","2020-01-16","2020-01-17","2020-01-18","2020-01-19","2020-01-20","2020-01-21"
,"2020-01-22","2020-01-23","2020-01-24","2020-01-25","2020-01-26","2020-01-27"
,"2020-01-28","2020-01-29","2020-01-30","2020-01-31"
,"2020-02-01","2020-02-02","2020-02-03","2020-02-04","2020-02-05","2020-02-06","2020-02-07","2020-02-08","2020-02-09","2020-02-10"
,"2020-02-11","2020-02-12","2020-02-13","2020-02-14","2020-02-15","2020-02-16","2020-02-17","2020-02-18","2020-02-19","2020-02-20","2020-02-21"
,"2020-02-22","2020-02-23","2020-02-24","2020-02-25","2020-02-26","2020-02-27"
,"2020-02-28","2020-02-29","2020-02-30","2020-03-01","2020-03-02","2020-03-03","2020-03-04","2020-03-05","2020-03-06","2020-03-07","2020-03-08","2020-03-09","2020-03-10"
,"2020-03-11","2020-03-12","2020-03-13","2020-03-14","2020-03-15","2020-03-16","2020-03-17","2020-03-18","2020-03-19","2020-03-20","2020-03-21"
,"2020-03-22","2020-03-23","2020-03-24","2020-03-25","2020-03-26","2020-03-27"
,"2020-03-28","2020-03-29","2020-03-30","2020-04-01","2020-04-02","2020-04-03","2020-04-04","2020-04-05","2020-04-06","2020-04-07","2020-04-08","2020-04-09","2020-04-10"
,"2020-04-11","2020-04-12","2020-04-13","2020-04-14","2020-04-15","2020-04-16","2020-04-17","2020-04-18","2020-04-19","2020-04-20","2020-04-21"
,"2020-04-22","2020-04-23","2020-04-24","2020-04-25","2020-04-26","2020-04-27"
,"2020-04-28","2020-04-29","2020-04-30","2020-05-01","2020-05-02","2020-05-03","2020-05-04","2020-05-05","2020-05-06","2020-05-07","2020-05-08","2020-05-09","2020-05-10"
,"2020-05-11","2020-05-12","2020-05-13","2020-05-14","2020-05-15","2020-05-16","2020-05-17","2020-05-18","2020-05-19"
]


# make list of location
locations = []
for location in dataset["location"]:
    if location not in locations:
        locations.append(location)
# make figure
fig_dict = {
    "data": [],
    "layout": {},
    "frames": []
}


# fill in most of layout
fig_dict["layout"]["xaxis"] = {"title": "diabetes_prevalence","range": [ 0,30 ]}
fig_dict["layout"]["yaxis"] = {"title": "Age 65+","range": [ 0, 30] }
fig_dict["layout"]["hovermode"] = "closest"
fig_dict["layout"]["updatemenus"] = [
    {
        "buttons": [
            {
                "args": [None, {"frame": {"duration": 500, "redraw": False},
                                "fromcurrent": True, "transition": {"duration": 300,
                                                                    "easing": "quadratic-in-out"}}],
                "label": "Play",
                "method": "animate"
            },
            {
                "args": [[None], {"frame": {"duration": 0, "redraw": False},
                                  "mode": "immediate",
                                  "transition": {"duration": 0}}],
                "label": "Pause",
                "method": "animate"
            }
        ],
        "direction": "left",
        "pad": {"r": 10, "t": 87},
        "showactive": False,
        "type": "buttons",
        "x": 0.1,
        "xanchor": "right",
        "y": 0,
        "yanchor": "top"
    }
]

sliders_dict = {
    "active": 0,
    "yanchor": "top",
    "xanchor": "left",
    "currentvalue": {
        "font": {"size": 20},
        "prefix": "days:",
        "visible": True,
        "xanchor": "right"
    },
    "transition": {"duration": 300, "easing": "cubic-in-out"},
    "pad": {"b": 10, "t": 50},
    "len": 0.9,
    "x": 0.1,
    "y": 0,
    "steps": []
}

size_ref_max = 10000
marker_size = 50
#Size of each bubble with respect to "max" size bubble
sizeref = 2 * ( size_ref_max ) / ( (marker_size) * 2)   

# make data
date = "2020-12-31"
for location in locations:
    dataset_by_date = dataset[dataset["date"] == date]
    dataset_by_date_and_location = dataset_by_date[
        dataset_by_date["location"] == location]
    data_dict = {
        "x": list(dataset_by_date_and_location["diabetes_prevalence"]),
        "y": list(dataset_by_date_and_location["age_above_65"]),
        "mode": "markers",
        "text": list(dataset_by_date_and_location["location"]),
        "marker": {
            "sizemode": "area",
            "sizeref": sizeref,
            "size": list(dataset_by_date_and_location["total_cases"])
        },
        "name": location
        # check this later
        # "color"=['rgb(93, 164, 214)', 'rgb(255, 144, 14)',
        #        'rgb(44, 160, 101)', 'rgb(255, 65, 54)'],
    }
    fig_dict["data"].append(data_dict)

# make frames
for date in dates:
    frame = {"data": [], "name": str(date)}
    for location in locations:
        dataset_by_date = dataset[dataset["date"] == date]
        dataset_by_date_and_location = dataset_by_date[
            dataset_by_date["location"] == location]
        
        data_dict = {
            "x": list(dataset_by_date_and_location["diabetes_prevalence"]),
            "y": list(dataset_by_date_and_location["age_above_65"]),
            "mode": "markers",
            "text": list(dataset_by_date_and_location["location"]),
            "marker": {
                "sizemode": "area",
                "sizeref": sizeref,
                "size": list(dataset_by_date_and_location["total_cases"])
            },
            "name": location
        }
        frame["data"].append(data_dict)

    fig_dict["frames"].append(frame)
    slider_step = {"args": [
        [date],
        {"frame": {"duration": 300, "redraw": False},
         "mode": "immediate",
         "transition": {"duration": 300}}
    ],
        "label": date,
        "method": "animate"}
    sliders_dict["steps"].append(slider_step)


fig_dict["layout"]["sliders"] = [sliders_dict]

fig = go.Figure(fig_dict)

fig.show()


