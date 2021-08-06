# create-ml-object-detection

Trying to use Apple's Create ML for Polyps Detection. The result was not impressive though but kind ok for just trying GUI based ML training suite. Thinking of using regular python script with TensorFlow etc for my next experiments.

- [Tried Apple’s CreateML and plugged the model into a sample app - YouTube](https://www.youtube.com/watch?v=GF25mYBaoRk) 

<img src="https://raw.githubusercontent.com/kiichi/create-ml-object-detection/main/results/review-chiken.jpg" width=300/>



## Setup

- Iteration: 6000
- Grid Size: 8 x 6 or could be 8 x 8
- Training and Valiation set: 850
- Testing set: 150
- Batch Size: 64

## Results

- Loss: 1.013
- I/U 50%: 90%

- Training: 90%
- Training: 71%
- Training: 46%

# Repo

1. Download Sample Files from Hyper-Kvasir Dataset with Bounding Box https://datasets.simula.no/hyper-kvasir/ 
2. Extract the files zip into segmented-images folder 
2. I wrote a little script convert.py it's located under segmented-images/convert.py. It takes hyper-vasier's bounding box json format and it converts it into Apple's CreateML annotation.json file format. It also takes 1000 images from the images folder, and split them into
- training : 700
- validation : 150
- testing: 150
it also puts training-validation folder for 850 images because I noticed that CreateML app does automatically pickup validation sets. Chose wichever you want.
4. Select folders from CreateML
5. Set parameter and run
6. After tranining is completed, build XCode project and deploy it to your phone. I used their "Breakfast Finder" sample app.
https://developer.apple.com/documentation/vision/recognizing_objects_in_live_capture
7. replace ObjectDetector.mlmodel with what you outputted from CreateML project.
8. Try the app on your phone.
