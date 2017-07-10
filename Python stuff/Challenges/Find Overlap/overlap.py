

first_rect = {
	
	"left_x": 1,
	"bottom_y": 5,
	
	"width": 10,
	"height": 4

}

second_rect = {
	
	"left_x": 5,
	"bottom_y": 5,
	
	"width": 4,
	"height": 10

}





def get_x(x1, x2, w1, w2): #x and width
	
	right_x1 = x1 + w1
	right_x2 = x2 + w2
	
	#difference = right_x2 - right_x1
	
	
	if right_x1 > right_x2:
		difference = right_x1 - right_x2
		
	else:
		difference = right_x2 - right_x1
	
	
	return difference

	
def get_y(y1, y2, h1,h2):
	
	top_y1 = y1 + h1
	top_y2 = y2 + h2
	
	if top_y1 > top_y2:
		difference = top_y1 - top_y2
		
	else:
		difference = top_y2 - top_y1
		
def get_area(rect1, rect2):
	
	width = get_x(rect1["left_x"], rect1["width"],rect2["left_x"], rect2["width"])
	height = get_y(rect1["bottom_y"], rect1["height"],rect2["bottom_y"], rect2["height"])
		
	area = width*height
	
	print(area)

get_area(first_rect, second_rect)	
		
		
		
		
		
		
		
		
		
		
		
	