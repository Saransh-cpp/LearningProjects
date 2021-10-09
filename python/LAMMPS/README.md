# GIF maker for LAMMPS

Create a GIF from your output images in just 1 line of code.

## Installation
1. Clone this repository
```
git clone https://github.com/Saransh-cpp/LearningProjects
```
2. Change directory
```
cd python/LAMMPS
```
3. Create a wheel file
```
python setup.py bdist_wheel
```
4. Install the package using the wheel file
```
cd dist
python -m pip install create_gif-0.1.0-py3-none-any.whl
```

**NOTE**: To update the package, first uninstall the existing package and then follow the same steps.

## Usage
```py
# first create a new python file in the directory where your images are stored
# then use the following code to create a GIF
import create_gif

create_gif.create_gif(
    'image.*.jpg'   # path of the images, in my case the images were named as image.0000.jpg, image.0250.jpg, ... image.5000.jpg
)
# in addition to the path, you can also supply duration of a single image in the GIF
# and the output file name, check the docstring for more information
```