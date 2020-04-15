# class create to facilitate the creation of dataset/dataloader objects

# this implementation tried to follow the same patterns as used in the ImageFolder dataset object, meaning that they should be completely interchangeable

# this class can also be used to create Dataset objects for unsupervised tasks. For doing so you simply leave both data_labels and  f_get_label parameters with None (default value), it will set all labels to -1.

# https://pytorch.org/docs/stable/_modules/torchvision/datasets/folder.html#ImageFolder
# https://pytorch.org/tutorials/beginner/data_loading_tutorial.html

from torch.utils.data import Dataset
from torchvision.datasets.folder import default_loader


class FileListDataset(Dataset):

    def __init__(self, data_files, data_labels=None, f_get_label=None, transform=None, loader=default_loader):
        """Constructor
        
        Arguments:
            data_files {list} -- list of the paths for the files that are going to compose the dataset
        
        Keyword Arguments:
            data_labels {list} -- list of labels of each sample. Must be the same length as data_files. This argument is only used when the f_get_label is not defined. If both are not defined its supposed that the class label is not important (unsupervised task), the class labels are going to be set as (int)-1 (default: {None})

            f_get_label {function} -- function used to extract the labels of the dataset from its filename. The function should receive an string and return a string, that indicate the labe. An example can be found inside barrett_utils.py - function "get_patient_id". If this is not passed, the data_labels should be used. (default: {None})
            
            transform {torchvision.transforms} -- transformations applied on the dataset. Works the same way as in the ImageFolder, for example. (default: {None})

            loader {function} -- function used to load an image from its filepath. Recommended to not change this argument. By default it uses the same loader as the ImageFolder class (default: {default_loader})
        """
        
        # getting the file paths
        self.data_files = data_files

        # if there is a function to get the filelabel we use it
        # TODO - move this 'label extractor' to the __getitem__ to save memory (getting the label just when actually reading the file), making this method makes more sense to exist.
        if f_get_label is not None:
            self.data_labels = [f_get_label(d) for d in self.data_files]
        # if there is a list with the labels, we use it instead
        elif data_labels is not None:
            self.data_labels = data_labels
        else:
            # when we dont have information about the labels we set all of them to -1 (meaning that the labels actually do not matter)
            self.data_labels = [-1] * len(self.data_files)
            # raise Exception("LabelsNeeded")
        
        # getting the classes and the mapper (dict mapping class name to an int index)
        self.classes, self.class_to_idx = self._get_classes()

        # image loader method
        self.loader = loader

        # transformations
        self.transform = transform


    def _get_classes(self):
        # getting all possible classes for the dataset
        classes = list(set(self.data_labels))
        classes.sort()

        # mapping the classes to an index "class_name": index (index = int)
        class_to_idx = {classes[i]: i for i in range(len(classes))}

        return classes, class_to_idx


    # must overload method - get the len of the dataset
    def __len__(self):
        return len(self.data_files)


    # must overload method - iterator
    def __getitem__(self, idx):
        sample = self.loader(self.data_files[idx])

        if self.transform is not None:
            sample = self.transform(sample)

        label = self.class_to_idx[self.data_labels[idx]]

        # print("label", label, self.data_labels[idx])

        return sample, label
