'''
    __file__ = 'minigame.minigame.nosetest_runner.py'
    __author__ = 'Kyle Roux'
    __date__ = '04/12/13'
    __pkg__ = 'minigame'
    __desc__ = 'Just runs all test modules in current package 
                (not recursive)'
'''
#tests = ('playertest.py', 'dietest.py', 'locktest.py')

if __name__ == "__main__":
    import nose
    nose.run(argv=["","playertest.py","dietest.py","locktest.py","--verbosity=2"])
