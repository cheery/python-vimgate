# Python vimgate

This gate has been tested in Linux, before using it in other systems, you need to reason whether it works out.

Contains a module `gate.py` which creates new unix socket that has interpreter behind it.

The vimgate -plugin feeds the current buffer into the gate, using nc command, when you press Ctrl-Return.
