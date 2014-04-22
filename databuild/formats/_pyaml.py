import pyaml

title = 'pyaml'

def export_set(dset):
    return pyaml.dump(dset.dict)

def import_set(dset, in_stream):
    dset.wipe()
    dset.dict = pyaml.load(in_stream)
