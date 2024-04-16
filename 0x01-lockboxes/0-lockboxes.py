#!/usr/bin/python3
'''
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1 and each box
may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.
'''


def getKeys(Boxes, keys):
	'''a recursive function to get all the keys in opened boxes'''
	updatedKeys = set()
	updatedKeys.update(keys)
	set_init_size = len(updatedKeys)

	for k in keys:
		if k < len(Boxes):
			updatedKeys.update(Boxes[k])

	if set_init_size != len(updatedKeys):
		return getKeys(Boxes, updatedKeys)
	else:
		return updatedKeys
	
def canUnlockAll(Boxes):
	'''check if all Boxes can be opened'''
	if len(Boxes) == 0:
		return False
	
	keys = getKeys(Boxes, [0])
	
	opened_Boxes = []
	for k in keys:
		if k < len(Boxes):
			opened_Boxes.append(Boxes[k])

	if len(Boxes) == len(opened_Boxes):
		return True
	else:
		return False
	'''
	for i in range(len(Boxes)):
		if i not in keys:
			return False
	
	return True
	'''
