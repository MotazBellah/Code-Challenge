def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    result = []

    """
    Populate result with all the matched files, and recurse
    """

    def helper(directory):
        from os import listdir
        from os.path import isdir, join
        for f in listdir(directory):
            full_path = join(directory, f)
            if isdir(full_path):
                helper(full_path)
            else:
                if f.endswith(suffix):
                    result.append(full_path)

    helper(path)
    return sorted(result)


def get_data_path(dir):
    from os.path import dirname, join
    return join(dirname(__file__), 'data', dir)


def test_find_files(example, suffix):
    print('-' * 12)
    data_path = get_data_path(example)
    for f in find_files(suffix, data_path):
        print(f[len(data_path) + 1:])


if __name__ == '__main__':
    test_find_files('testdir', '.c')
    # subdir1/a.c
    # subdir3/subsubdir1/b.c
    # subdir5/a.c
    # t1.c

    test_find_files('testdir_empty', '.c')
    # nothing

    test_find_files('testdir', '.h')
    # subdir1 / a.h
    # subdir3 / subsubdir1 / b.h
    # subdir5 / a.h
    # t1.h

    test_find_files('testdir', '')
    # subdir1 / a.c
    # subdir1 / a.h
    # subdir2 /.gitkeep
    # subdir3 / subsubdir1 / b.c
    # subdir3 / subsubdir1 / b.h
    # subdir4 /.gitkeep
    # subdir5 / a.c
    # subdir5 / a.h
    # t1.c
    # t1.h
