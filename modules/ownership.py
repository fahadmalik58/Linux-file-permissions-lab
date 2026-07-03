import os
import pwd
import grp


def change_owner(

        path,

        user,

        group

):

    uid = pwd.getpwnam(

        user

    ).pw_uid

    gid = grp.getgrnam(

        group

    ).gr_gid

    os.chown(

        path,

        uid,

        gid

    )

    return True