# FileListDataset

This project aims to be an alternative to the `ImageFolder` Dataset object from `Pytorch` in which, instead of giving the containing folder to the Dataset object we give it the data file paths, file by file. Labels are defined by the user as a second argument being in the form of a `list` of in the form of a `callback function`.

It is inspired and tries to follow the same standards `ImageFolder` Dataset object from `Pytorch`. The goal is to make them completely interchangeable, giving better control over the dataset loading procedure.

Note that this class, at the moment is used only for image data, but simply changing the `loader` show make it work for other types of data, like texts.

You can also checkout the `docstring` of the class for more details about each parameter.

You can also find some help/inspiration on the bundled jupyter notebook: `Tutorial.ipynb`

## Prerequisites

What things you need to install the software and how to install them

``` python
pytorch >= 1.2.0
torchvision >= 0.4.0
```

## Usage

The folowing examples are going to show how you could use this class.

First examples is by passing the list of labels already captured to the Dataset object and the second how to use the callback function.

Example 1:

``` python
from dataset_filelist import DatasetFileList
import glob
import os

data_files = glob.glob("examples/data/*/*")

# data_files = ['examples/data/class0/data_0.png',
#               'examples/data/class0/data_1.png',
#               'examples/data/class0/data_2.png',
#               'examples/data/class0/data_3.png',
#               'examples/data/class0/data_4.png',
#               'examples/data/class0/data_5.png',
#               'examples/data/class0/data_6.png',
#               'examples/data/class0/data_7.png',
#               'examples/data/class0/data_8.png',
#               'examples/data/class0/data_9.png',
#               'examples/data/class1/data_0.png',
#               'examples/data/class1/data_1.png',
#               'examples/data/class1/data_2.png',
#               'examples/data/class1/data_3.png',
#               'examples/data/class1/data_4.png',
#               'examples/data/class1/data_5.png',
#               'examples/data/class1/data_6.png',
#               'examples/data/class1/data_7.png',
#               'examples/data/class1/data_8.png',
#               'examples/data/class1/data_9.png',
#               'examples/data/class2/data_0.png',
#               'examples/data/class2/data_1.png',
#               'examples/data/class2/data_2.png',
#               'examples/data/class2/data_3.png',
#               'examples/data/class2/data_4.png',
#               'examples/data/class2/data_5.png',
#               'examples/data/class2/data_6.png',
#               'examples/data/class2/data_7.png',
#               'examples/data/class2/data_8.png',
#               'examples/data/class2/data_9.png']

data_labels = [f_name.split(os.sep)[-2] for f_name in data_files]

# data_labels = ['class0',
#                'class0',
#                'class0',
#                'class0',
#                'class0',
#                'class0',
#                'class0',
#                'class0',
#                'class0',
#                'class0',
#                'class1',
#                'class1',
#                'class1',
#                'class1',
#                'class1',
#                'class1',
#                'class1',
#                'class1',
#                'class1',
#                'class1',
#                'class2',
#                'class2',
#                'class2',
#                'class2',
#                'class2',
#                'class2',
#                'class2',
#                'class2',
#                'class2',
#                'class2']

dataset = DatasetFileList(data_files=data_files,
                          data_labels=data_labels,
                          transform=transforms.ToTensor())

print('Number of samples: ', len(dataset))

img, label = next(iter(dataset))

print('img:', img)
print('label:', label)
```

Output:

``` python
Number of samples:  30

img: tensor([[[1., 1., 1.,  ..., 1., 1., 1.],
         [1., 1., 1.,  ..., 1., 1., 1.],
         [1., 1., 1.,  ..., 1., 1., 1.],
         ...,
         [1., 1., 1.,  ..., 1., 1., 1.],
         [1., 1., 1.,  ..., 1., 1., 1.],
         [1., 1., 1.,  ..., 1., 1., 1.]],

        [[1., 1., 1.,  ..., 1., 1., 1.],
         [1., 1., 1.,  ..., 1., 1., 1.],
         [1., 1., 1.,  ..., 1., 1., 1.],
         ...,
         [1., 1., 1.,  ..., 1., 1., 1.],
         [1., 1., 1.,  ..., 1., 1., 1.],
         [1., 1., 1.,  ..., 1., 1., 1.]],

        [[1., 1., 1.,  ..., 1., 1., 1.],
         [1., 1., 1.,  ..., 1., 1., 1.],
         [1., 1., 1.,  ..., 1., 1., 1.],
         ...,
         [1., 1., 1.,  ..., 1., 1., 1.],
         [1., 1., 1.,  ..., 1., 1., 1.],
         [1., 1., 1.,  ..., 1., 1., 1.]]])

label: 0
```

Example 2:

``` python
from dataset_filelist import DatasetFileList
import glob
import os

data_files = glob.glob("examples/data/*/*")

# data_files = ['examples/data/class0/data_0.png',
#               'examples/data/class0/data_1.png',
#               'examples/data/class0/data_2.png',
#               'examples/data/class0/data_3.png',
#               'examples/data/class0/data_4.png',
#               'examples/data/class0/data_5.png',
#               'examples/data/class0/data_6.png',
#               'examples/data/class0/data_7.png',
#               'examples/data/class0/data_8.png',
#               'examples/data/class0/data_9.png',
#               'examples/data/class1/data_0.png',
#               'examples/data/class1/data_1.png',
#               'examples/data/class1/data_2.png',
#               'examples/data/class1/data_3.png',
#               'examples/data/class1/data_4.png',
#               'examples/data/class1/data_5.png',
#               'examples/data/class1/data_6.png',
#               'examples/data/class1/data_7.png',
#               'examples/data/class1/data_8.png',
#               'examples/data/class1/data_9.png',
#               'examples/data/class2/data_0.png',
#               'examples/data/class2/data_1.png',
#               'examples/data/class2/data_2.png',
#               'examples/data/class2/data_3.png',
#               'examples/data/class2/data_4.png',
#               'examples/data/class2/data_5.png',
#               'examples/data/class2/data_6.png',
#               'examples/data/class2/data_7.png',
#               'examples/data/class2/data_8.png',
#               'examples/data/class2/data_9.png']

# this function is applied for a single file and return a simple label as string
def getter_image_label(file_name):
    return file_name.split(os.sep)[-2]

dataset = DatasetFileList(data_files=data_files,
                          f_get_label=getter_image_label,
                          transform=transforms.ToTensor())

print('Number of samples: ', len(dataset))

img, label = next(iter(dataset))

print('img:', img)
print('label:', label)
```

Output:

``` python
Number of samples:  30

img: tensor([[[1., 1., 1.,  ..., 1., 1., 1.],
         [1., 1., 1.,  ..., 1., 1., 1.],
         [1., 1., 1.,  ..., 1., 1., 1.],
         ...,
         [1., 1., 1.,  ..., 1., 1., 1.],
         [1., 1., 1.,  ..., 1., 1., 1.],
         [1., 1., 1.,  ..., 1., 1., 1.]],

        [[1., 1., 1.,  ..., 1., 1., 1.],
         [1., 1., 1.,  ..., 1., 1., 1.],
         [1., 1., 1.,  ..., 1., 1., 1.],
         ...,
         [1., 1., 1.,  ..., 1., 1., 1.],
         [1., 1., 1.,  ..., 1., 1., 1.],
         [1., 1., 1.,  ..., 1., 1., 1.]],

        [[1., 1., 1.,  ..., 1., 1., 1.],
         [1., 1., 1.,  ..., 1., 1., 1.],
         [1., 1., 1.,  ..., 1., 1., 1.],
         ...,
         [1., 1., 1.,  ..., 1., 1., 1.],
         [1., 1., 1.,  ..., 1., 1., 1.],
         [1., 1., 1.,  ..., 1., 1., 1.]]])

label: 0
```

## Support

If you would like to see a new functionality, have a suggestion of how to make the documentation clearer or would to report a problem/bug, you can open an [issue](https://github.com/danilown/FileListDataset/issues/new) here on Github or send me and e-mail danilownunes@gmail.com.
