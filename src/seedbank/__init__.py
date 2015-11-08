from random import *

def autoseed():
    from datetime import datetime
    import os
    import sys

    base_filename = 'seedbank.log'
    filename = os.path.join(os.getenv('HOME'), base_filename)
    if not os.path.exists(filename):
        filename = base_filename

    seed_ = os.getenv('SEEDBANK_SEED', None)
    if seed_ == 'LAST':
        with open(filename, 'r') as f:
            for line in f:
                pass
            seed_ = int(line.split(':')[-1].strip())
    try:
        seed_ = int(seed_)
    except TypeError:
        seed_ = None
    if seed_ is None:
        seed_ = randint(0, 1000000)

    with open(filename, 'a') as f:
        f.write('%s: %s: %s\n' % (sys.argv[0], datetime.now(), seed_))
    seed(seed_)
    return seed_

autoseed()
