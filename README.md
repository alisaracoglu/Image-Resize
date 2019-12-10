# Image Resize
Image resize module for python / Image resize tool. This module has a function called "resize". See the description of the function about use.


### ABOUT FUNCTION

##### Definition

```python
resize(image_path, output_width='', output_height='', output_path='')
```


##### Parameters or Arguments
- 'image_path'   -> (required) Input image path. This value can be absolute path or relative path.
- 'output_width' -> (optional) Intended width of resized image.
- 'output_height'-> (optional) Intended height of resized image.
- 'output_path'  -> (optional) Directory of new resized image. New image send to this directory.


##### Warning
- Also at least one of the 'output_width' or 'output_height' data must be entered. If only one is entered,
the other will be changed at the same rate.
- The 'Output Path' value can be either the absolute file path or the directory path or empty. If left empty,
output to the same directory with Input Image.
