import os

import anago
from anago.utils import download, load_data_and_labels


if __name__ == '__main__':
    dir_path = 'test_dir'
    url = 'https://storage.googleapis.com/chakki/datasets/public/models.zip'
    DATA_ROOT = os.path.join(os.path.dirname(__file__), '../data/conll2003/en/ner')

    test_path = os.path.join(DATA_ROOT, 'test.txt')
    x_test, y_test = load_data_and_labels(test_path)

    download(url, dir_path)

    model = anago.Sequence.load(dir_path)
    model.score(x_test, y_test)
