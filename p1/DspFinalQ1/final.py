import plotly.graph_objects as go
import os
import pandas as pd
from IPython.display import Image

data_file = 'p.csv'

dataset = pd.read_csv(data_file)
dates= ["01-01-20","02-01-20","03-01-20","03-01-20","05-01-20",
"06-01-20","07-01-20","08-01-20","09-01-20","10-01-20",
"11-01-20","12-01-20","13-01-20","14-01-20","15-01-20",
"16-01-20","17-01-20","18-01-20","19-01-20","20-01-20",
"21-01-20","22-01-20","23-01-20","24-01-20","25-01-20",
"26-01-20","27-01-20","28-01-20","29-01-20","30-01-20","01-02-20","02-02-20","03-02-20","02-02-20","05-02-20",
"06-02-20","07-02-20","08-02-20","09-02-20","10-02-20",
"11-02-20","12-02-20","13-02-20","14-02-20","15-02-20",
"16-02-20","17-02-20","18-02-20","19-02-20","20-02-20",
"21-02-20","22-02-20","23-02-20","24-02-20","25-02-20",
"26-02-20","27-02-20","28-02-20","29-02-20","30-02-20","01-03-20","02-03-20","03-03-20","03-03-20","05-03-20",
"06-03-20","07-03-20","08-03-20","09-03-20","10-03-20",
"11-03-20","12-03-20","13-03-20","14-03-20","15-03-20",
"16-03-20","17-03-20","18-03-20","19-03-20","20-03-20",
"21-03-20","22-03-20","23-03-20","24-03-20","25-03-20",
"26-03-20","27-03-20","28-03-20","29-03-20","30-03-20",
"01-04-20","02-04-20","03-04-20","03-04-20","05-04-20",
"06-04-20","07-04-20","08-04-20","09-04-20","10-04-20",
"11-04-20","12-04-20","13-04-20","14-04-20","15-04-20",
"16-04-20","17-04-20","18-04-20","19-04-20","20-04-20",
"21-04-20","22-04-20","23-04-20","24-04-20","25-04-20",
"26-04-20","27-04-20","28-04-20","29-04-20","30-04-20",
"01-05-20","02-05-20","03-05-20","03-05-20","05-05-20",
"06-05-20","07-05-20","08-05-20","09-05-20","10-05-20",
"11-05-20"
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
fig_dict["layout"]["xaxis"] = {"title": "total_deaths","range": [ 0,90000 ]}
fig_dict["layout"]["yaxis"] = {"title": "total_recovered","range": [ 0, 350000] }
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

size_ref_max = 3000
marker_size = 50
#Size of each bubble with respect to "max" size bubble
sizeref = 2 * ( size_ref_max ) / ( (marker_size) * 2)   

# make data
date = "01-01-20"
for location in locations:
    dataset_by_date = dataset[dataset["date"] == date]
    dataset_by_date_and_location = dataset_by_date[
        dataset_by_date["location"] == location]
    data_dict = {
        "x": list(dataset_by_date_and_location["total_deaths"]),
        "y": list(dataset_by_date_and_location["total_recovered"]),
        "mode": "markers",
        "text": list(dataset_by_date_and_location["location"]),
        "marker": {
            "sizemode": "area",
            "sizeref": sizeref,
            "size": list(dataset_by_date_and_location["total_cases"])
        },
        "name": location
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
            "x": list(dataset_by_date_and_location["total_deaths"]),
            "y": list(dataset_by_date_and_location["total_recovered"]),
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
# if not os.path.exists("images"):
#     os.mkdir("images")
# img_bytes = fig.to_image(format="png", width=600, height=350, scale=2)
# Image(img_bytes)
StorageData=16129
for i in range(StorageData):
           fig = px.bar(StorageData[i], x="location", y="total_cases",
      animation_frame="date", animation_group="total_cases",text='total_cases')

