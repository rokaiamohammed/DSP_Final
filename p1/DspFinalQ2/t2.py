import plotly.express as px
import pandas as pd
data_file = 'p.csv'
import cv2

dataset=pd.read_csv(data_file)  

fig = px.choropleth(dataset, locations="iso_alpha",
                    color="total_deaths",
                    hover_name="location", 
                    color_continuous_scale=px.colors.sequential.Plasma,
                    animation_frame="date"
                    
                    
                    )
fig.show()

image_folder = 'question2pics'
video_name = 'question2video.avi'

images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, 0, 1, (width,height))

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()


