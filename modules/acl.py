import subprocess


def get_acl(path):

    result = subprocess.run(

        [

            "getfacl",

            path

        ],

        capture_output=True,

        text=True

    )

    return result.stdout


def set_acl(

        path,

        permission

):

    subprocess.run(

        [

            "setfacl",

            "-m",

            permission,

            path

        ]

    )

    return True
