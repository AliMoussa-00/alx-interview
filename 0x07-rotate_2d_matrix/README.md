# Rotate 2D Matrix

[task](https://drive.google.com/file/d/1vHqYYyWtfty8iy68292jkd-DxNyQ4oAP/view?usp=drive_link)

---

### Step 1: Transpose the Matrix

Consider the initial matrix:

```
1 2 3
4 5 6
7 8 9
```

After transposition, the matrix becomes:

```
1 4 7
2 5 8
3 6 9
```

This step swaps the elements along the main diagonal (top-left to bottom-right).

### Step 2: Reverse Each Row

After transposition, we reverse each row:

```
7 4 1
8 5 2
9 6 3
```

This step reverses the order of elements in each row. Now, the matrix is rotated by 90 degrees clockwise.

### Example

Consider a 4x4 matrix:

```
1  2  3  4
5  6  7  8
9 10 11 12
13 14 15 16
```

#### Step 1: Transpose

After transposition:

```
1  5  9 13
2  6 10 14
3  7 11 15
4  8 12 16
```

#### Step 2: Reverse Each Row

After reversing each row:

```
13  9  5  1
14 10  6  2
15 11  7  3
16 12  8  4
```

Now, the original matrix is rotated 90 degrees clockwise.

This two-step process ensures that the matrix is rotated in place without requiring extra memory or creating a new matrix.