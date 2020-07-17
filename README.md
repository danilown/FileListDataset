# FileListDataset

This project aims to be an alternative to the `ImageFolder` Dataset object from `Pytorch` in which, instead of giving the containing folder to the Dataset object we give it the data file paths, file by file. Labels are defined by the user as a second argument being in the form of a `list` of in the form of a `callback function`.

It is inspired and tries to follow the same standards `ImageFolder` Dataset object from `Pytorch`. The goal is to make them completely interchangeable, giving better control over the dataset loading procedure.

Note that this class, at the moment is used only for image data, but simply changing the `loader` show make it work for other types of data, like texts.

You can also checkout the `docstring` of the class for more details about each parameter.

You can also find some help/inspiration on the bundled jupyter notebook: `Tutorial.ipynb`

## Prerequisites

What things you need to install the software and how to install them.

``` python
torch >= 1.2.0
torchvision >= 0.4.0
```

You can install them either manually or through the command:

``` bash
pip install -r requirements.txt
```

## Instalation

If you want to use this class, you have two options:

A) Simply copy and paste it in your project;

B) Or install it through `pip` following the command bellow:

``` bash
pip install git+git://github.com/danilown/FileListDataset.git#egg=FileListDataset
```

Then, using it is as simples as:

```python
from FileListDataset import FileListDataset
```

> **Note 1**: As noted by [David Winterbottom](https://codeinthehole.com/tips/using-pip-and-requirementstxt-to-install-from-the-head-of-a-github-branch/), if you freeze the environment to export the dependencies, note that this will add the specific commit to your requirements, so it might be a good idea to delete the commit ID from it.
> ___
> **Note 2**: Due to the simplicity of this "package", this installation method was preferred over the more traditional [PyPI](https://pypi.org/).

## Usage

The folowing examples are going to show how you could use this class.

First examples is by passing the list of labels already captured to the Dataset object and the second how to use the callback function.

Example 1:

``` python
from FileListDataset import FileListDataset
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

dataset = FileListDataset(data_files=data_files,
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
from FileListDataset import FileListDataset
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

dataset = FileListDataset(data_files=data_files,
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

If you would like to see a new functionality, have a suggestion on how to make the documentation clearer or report a problem, you can open an [issue](https://github.com/danilown/FileListDataset/issues/new) here on Github or send me an e-mail danilownunes@gmail.com.
