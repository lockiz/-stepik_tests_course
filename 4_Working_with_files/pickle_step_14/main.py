import pickle


def filter_dump(filename, objects, typename):
    with open(filename, mode='wb') as file_pkl:
        pickle.dump([item for item in objects if type(item) == typename], file_pkl)
