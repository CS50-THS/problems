import check50
import check50.c


@check50.check()
def exists():
    """temps.c exists"""
    check50.exists("temps.c")


@check50.check(exists)
def compiles():
    """temps.c compiles"""
    check50.c.compile("temps.c", lcs50=True)



