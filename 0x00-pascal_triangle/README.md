# Pascal's Triangle

Pascal's Triangle is a 2D array where each row represents an array containing the coefficients of the binomial expansion.

each element in row is the **sum** of the element on **top of it** + **left** and **top of it** + **right**

### Overview

![Image Alt Text](https://www.bing.com/images/search?view=detailV2&ccid=lRjrQ6nc&id=7D37D2389AB75B4872CE2450C875E30DB7103B6E&thid=OIP.lRjrQ6ncPSNmZAz1S_AaHQHaGW&mediaurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.9518eb43a9dc3d2366640cf54bf01a1d%3frik%3dbjsQtw3jdchQJA%26riu%3dhttp%253a%252f%252fcodescracker.com%252fpython%252fimages%252fpascal-triangle-python.JPG%26ehk%3dCqiIhBO5OCBfqx3XDq8yBm287Y0WXIBQLJBslFENJSI%253d%26risl%3d%26pid%3dImgRaw%26r%3d0&exph=427&expw=498&q=pascal+triangle+python&simid=607992946960040005&FORM=IRPRST&ck=D9657C97CABD0E7DE311C4D715DC7618&selectedIndex=8&itb=0&ajaxhist=0&ajaxserp=0)

### Python algorithm

```python
#!/usr/bin/python3
'''Pascal triangle module'''

def pascal_triangle(n):
	'''
	create and  list of lists of integers
	representing the Pascal’s triangle of n
	'''

	if n <= 0 :
		return []
	
	triangle = []
	for row in range(n):
		current_row = []

		for col in range(row + 1):
			if col == 0 or col == row:
				current_row.append(1)
			else:
				current_row.append(triangle[row - 1][col] + triangle[row - 1][col - 1])
		
		triangle.append(current_row)
	
	return triangle
```
