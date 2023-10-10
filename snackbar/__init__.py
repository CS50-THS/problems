import check50
import check50.c
from re import escape


@check50.check()
def exists():
    """snackbar.c exists"""
    check50.exists("snackbar.c")


@check50.check(exists)
def compiles():
    """snackbar.c compiles"""
    check50.c.compile("snackbar.c", lcs50=True)

@check50.check(compiles)
def test_0():
    """input of \"cold brew\", and \"hot dog\" results in $8.00"""
    items = ["cold brew", "hot dog"]
    output = 8.0
    check50.run("./snackbar"
    ).stdin(items[0], prompt=True
    ).stdin(items[1], prompt=True
    ).stdout(regex(f"{output:.2f}"), f"${output:.2f}", regex=True).kill()


def regex(cost):
    """match case-insensitively with dollar-sign required and only characters on either side"""
    return fr'(?i)^[\D]*\${escape(cost)}[\D]*$'


