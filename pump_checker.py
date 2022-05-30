class PumpChecker:
    """ Find request pump with needed characteristics
    user_answer - request vessel volume
    pump_list - list from PumpModel module"""
    def __init__(self, user_answer, pump_list):
        self.user_answer = user_answer  # data from user
        self.pump_list = pump_list  # pump list from calculate
        # calculated values
        self.jacket_volume = self.user_answer * 0.15
        self.circulate_volume = self.jacket_volume * 3
        self.needed_pump = 0

    def pump_finder(self):
        pumps_lph = []

        for pump in self.pump_list:
            pumps_lph.append(pump.lph)

        pumps_lph.sort()

        for lph in pumps_lph:
            if lph >= self.circulate_volume:
                self.needed_pump = lph
                break  # For  stop on first suitable pump

        if self.circulate_volume > 800:
            self.needed_pump = 800

        for pump in self.pump_list:
            if pump.lph == self.needed_pump:
                return pump
