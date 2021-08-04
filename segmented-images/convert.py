# kiichi
import json
import shutil
import os

f = open('bounding-boxes.json')
data = json.load(f)
f.close()
list = []
for key in data.keys():
	item = {}
	item['image'] = key+'.jpg'
	item['annotations'] = []
	bbox = data[key]['bbox']
	for box in bbox:
		label = box['label']
		x = box['xmin']
		y = box['ymin']
		width = box['xmax'] - box['xmin']
		height = box['ymax'] - box['ymin']
		print key, label, x, y, width, height
		rect = {
			'label':label,
			'coordinates':{
				'x':x,
				'y':y,
				'width':width,
				'height':height
			}
		}
		item['annotations'].append(rect)
	list.append(item)

folders = ['training','validation','testing','training-validation']
datasets = {
	'training':list[0:700],
	'validation':list[700:850],
	'testing':list[850:1000],
	'training-validation':list[0:850]
}
for folder in folders:
	if os.path.exists(folder):
		shutil.rmtree(folder)
	os.mkdir(folder)
	with open(folder + '/annotations.json', 'w') as outfile:
		json.dump(datasets[folder], outfile)
		jsonstr = json.dumps(datasets[folder])
		htmlstr = ''
		with open('index.html', 'r') as htmlfile:
			htmlstr = htmlfile.read() 
			htmlstr = htmlstr.replace('{{{LIST}}}', jsonstr)
		with open(folder + '/index.html', 'w') as htmlout:
			htmlout.write(htmlstr)
		for item in datasets[folder]:
			shutil.copyfile('images/'+item['image'],folder+'/'+item['image'])
