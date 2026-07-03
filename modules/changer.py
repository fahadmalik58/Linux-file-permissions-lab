import os


def chmod_file(path, mode):

    os.chmod(

        path,

        int(mode,8)

    )

    return True