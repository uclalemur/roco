from roco.api.component import Component
from roco.library import *

if __name__ == "__main__":
    c = Component(name="serial")
    c.add_subcomponent("srl", "serial_in")
    c.make_output()
