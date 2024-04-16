#!/usr/bin/python3
'''
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1 and each box
may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.
'''


def get_keys(boxes, keys):
    '''a recursive function to get all the keys in opened boxes'''
    updated_keys = set()
    updated_keys.update(keys)
    set_init_size = len(updated_keys)

    for k in keys:
        if k < len(boxes):
            updated_keys.update(boxes[k])

    if set_init_size != len(updated_keys):
        return get_keys(boxes, updated_keys)

    return updated_keys


def canUnlockAll(boxes):
    '''check if all boxes can be opened'''
    if len(boxes) == 0:
        return False

    keys = get_keys(boxes, [0])

    opened_boxes = []
    for k in keys:
        if k < len(boxes):
            opened_boxes.append(boxes[k])

    return len(boxes) == len(opened_boxes)
