def analyze(files):

    findings = []

    for file in files:

        perms = file["Octal"]

        if perms == "777":

            findings.append(

                f"{file['File']} has 777 permissions"

            )

        if perms.endswith("7"):

            findings.append(

                f"{file['File']} is world writable"

            )

    return findings