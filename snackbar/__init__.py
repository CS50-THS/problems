import check50
import check50.c


@check50.check()
def exists():
    """snackbar.c exists"""
    check50.exists("snackbar.c")


@check50.check(exists)
def compiles():
    """snackbar.c compiles"""
    check50.c.compile("snackbar.c", lcs50=True)


@check50.check(compiles)
def test0():
    """input of cold brew and hot dog yields output of $8.00"""
    check50.run("./snackbar").stdin(
        "cold brew\nhot dog\n\n").stdout(
        "Your total cost is: $8.00\n"
        ).exit(0)


