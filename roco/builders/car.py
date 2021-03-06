from roco.api.component import Component
from roco.library import *
from roco.library import get_component

if __name__ == "__main__":
    c = Component(name = 'Car')
    c.add_subcomponent('Constant0', 'Constant')
    c.add_subcomponent('Constant1', 'Constant')
    c.add_subcomponent('Constant2', 'Constant')
    c.add_subcomponent('Constant3', 'Constant')
    c.add_subcomponent('DrivenServo0', 'DrivenServo')
    c.add_subcomponent('DrivenServo1', 'DrivenServo')
    c.add_subcomponent('DrivenServo2', 'DrivenServo')
    c.add_subcomponent('DrivenServo3', 'DrivenServo')
    c.add_subcomponent('node_mcu0', 'node_mcu')
    c.add_connection(('node_mcu0', 'do1'), ('DrivenServo0', 'PWMin'))
    c.add_connection(('Constant0', 'num'), ('DrivenServo0', 'inInt'))
    c.add_connection(('node_mcu0', 'do2'), ('DrivenServo1', 'PWMin'))
    c.add_connection(('Constant1', 'num'), ('DrivenServo1', 'inInt'))
    c.add_connection(('node_mcu0', 'do3'), ('DrivenServo2', 'PWMin'))
    c.add_connection(('Constant2', 'num'), ('DrivenServo2', 'inInt'))
    c.add_connection(('node_mcu0', 'do4'), ('DrivenServo3', 'PWMin'))
    c.add_connection(('Constant3', 'num'), ('DrivenServo3', 'inInt'))
    c.get_subcomponent('Constant0').set_parameter('num', '130')
    c.get_subcomponent('Constant1').set_parameter('num', '130')
    c.get_subcomponent('Constant2').set_parameter('num', '130')
    c.get_subcomponent('Constant3').set_parameter('num', '130')
    c.to_yaml("library/car.yaml")
    c.make_output()
