import os
import stat
import pwd
import grp


def scan_permissions(path):

    results = []

    for item in os.listdir(path):

        full_path = os.path.join(path, item)

        info = os.stat(full_path)

        permissions = stat.filemode(info.st_mode)

        owner = pwd.getpwuid(
            info.st_uid
        ).pw_name

        group = grp.getgrgid(
            info.st_gid
        ).gr_name

        results.append({

            "File": item,

            "Owner": owner,

            "Group": group,

            "Permissions": permissions,

            "Octal": oct(

                info.st_mode

            )[-3:]

        })

    return results