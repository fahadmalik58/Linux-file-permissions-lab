import json
import pandas as pd


def save_json(data):

    with open(

            "reports/report.json",

            "w"

    ) as f:

        json.dump(

            data,

            f,

            indent=4

        )


def save_csv(data):

    df = pd.DataFrame(data)

    df.to_csv(

        "reports/report.csv",

        index=False

    )


def save_txt(data):

    with open(

            "reports/report.txt",

            "w"

    ) as f:

        for row in data:

            f.write(

                str(row)

                + "\n"

            )
