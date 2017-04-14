import logging
logger = logging.getLogger(__name__)

from ControlBoardApp.cbhal.SimulatorBase import SimulatorBase, SimulatorFrame


CB_SNAME = 'ControlBoard_1v1_Simulator'
CB_LNAME = 'FRC Control Board v1.1 Simulator'

class HardwareAbstractionLayer(SimulatorBase):

    LED_OUTPUTS = 16
    PWM_OUTPUTS = 11
    ANALOG_INPUTS = 16
    SWITCH_INPUTS = 16
