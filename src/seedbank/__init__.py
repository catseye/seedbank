from random import *

def autoseed():
    from datetime import datetime
    import os
    import sys

    seed_ = None
    try:
        seed_ = int(os.getenv('SEEDBANK_SEED', None))
    except TypeError:
        seed_ = None
    if seed_ is None:
        seed_ = randint(0, 1000000)

    base_filename = 'seedbank.log'
    filename = os.path.join(os.getenv('HOME'), base_filename)
    if not os.path.exists(filename):
        filename = base_filename

    with open(filename, 'a') as f:
        f.write('%s: %s: %s\n' % (sys.argv[0], datetime.now(), seed_))
    seed(seed_)
    return seed_

autoseed()
