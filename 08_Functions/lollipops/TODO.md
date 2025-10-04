
Implement hue / saturation / brightness:
```python
stroke(hue(fill_col), saturation(fill_col) - 100, brightness(fill_col))

stroke(hue(fill_col), saturation(fill_col), brightness(fill_col) - 100)  # shadow
```

`arc` will fail if you pass zero for w or h, fix?

`fill(255)` should be white even in HSB?
