import check50
import check50.c


@check50.check()
def exists():
    """atoi.c exists"""
    check50.exists("atoi.c")


@check50.check(exists)
def compiles():
    """atoi.c compiles"""
    check50.c.compile("atoi.c", lcs50=True)

@check50.check(compiles)
def test_1():
    check50.run("./atoi").stdin('3432').stdout(3432)


@check50.check(compiles)
def test_2():
    check50.run("./atoi").stdin('98765').stdout(98765)


