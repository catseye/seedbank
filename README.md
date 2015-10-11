seedbank
========

One of the gotchas with writing programs that use randomness is reproducibility.

Like, if you're developing a Markov-chain-based generator for [NaNoGenMo][],
and you're running it a few times while tweaking it, and — hey, that output
was pretty interesting! — but you've already pressed ctrl-C and now it's gone
forever.

A good solution is to write your program so that it can take a given random
seed as input somehow, and if one is not given, pick one randomly and report
it somehow, for possible future use.

You could implement that pattern using a command-line option and whatnot,
but that gets tedious and possibly inconsistent if you're developing multiple
such programs.  So `seedbank` aims to make it dead simple — a one-line change
to your script.

Usage
-----

First, make sure the `seedbank` module is on your `PYTHONPATH`.  For example,
you might add this line to your `.bashrc`:

    export PYTHONPATH=/path/to/this/repo/src:$PYTHONPATH

Then, in your Python program, where you would normally say

    import random

you instead say

    import seedbank as random

and you can continue to use all the functions in the `random` module as normal,
while `seedbank` takes care of the seeding and reporting in the following
manner:

*   If the environment variable `SEEDBANK_SEED` was set to an integer,
    it uses that as the seed for the random number generator.  Otherwise,
    it picks a random integer to use as the seed.
*   After the seed is picked, it appends a line to a logfile which contains
    the name of the script, the timestamp, and the chosen seed.  If a file
    called `seedbank.log` exists in your home directory, that file will be
    used as the logfile.  Otherwise, the file `seedbank.log` in the current
    directory will be used (it will be created if it doesn't exist.)

Then, if you ever want to re-run with a seed that was picked, you can
review the log file, pick the seed you want, and set `SEEDBANK_SEED` to that.

You can of course import individual functions from `seedbank` as if they
were from `random`, and that works too:

    from seedbank import choice, randint

Example
-------

The programs in `bin/` in this repo demonstrate the concept.  Example
transcript:

    $ bin/seedbank_demo1
    eoaeuio
    $ bin/seedbank_demo1
    aoueo
    $ cat seedbank.log 
    bin/seedbank_demo1: 2015-10-11 10:39:11.440595: 615184
    bin/seedbank_demo1: 2015-10-11 10:39:12.495845: 100141
    $ SEEDBANK_SEED=615184 bin/seedbank_demo1
    eoaeuio
    $ 

[NaNoGenMo]:   https://github.com/dariusk/NaNoGenMo
