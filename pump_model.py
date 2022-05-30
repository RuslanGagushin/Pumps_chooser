class PumpModel:
    """ Make a pumps object from database with characteristics variables"""
    def __init__(self, p_model, p_mph, p_lph, p_connect, p_size):
        self.model = p_model
        self.mph = p_mph
        self.lph = p_lph
        self.connect = p_connect
        self.size = p_size
