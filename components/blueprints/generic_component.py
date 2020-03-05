from components.base.base_component import ProgramHarness
from qcelemental import models

class GenericComponent(ProgramHarness):

    @classmethod
    def input(cls):
        return models.ProtoModel

    @classmethod
    def output(cls):
        return models.ProtoModel