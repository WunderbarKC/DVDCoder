from promptings.CoT import CoTStrategy
from promptings.Direct import DirectStrategy
from promptings.Analogical import AnalogicalStrategy
from promptings.SelfPlanning import SelfPlanningStrategy

from promptings.MapCoder import MapCoder as MapCoder
from promptings.Debate import Debate
from promptings.Debate_r3 import Debate_R3
from promptings.Debate_r2 import Debate_R2
from promptings.SemanticOnly import SemanticOnly
from promptings.DVDCoder import DVDCoder

class PromptingFactory:
    @staticmethod
    def get_prompting_class(prompting_name):
        if prompting_name == "CoT":
            return CoTStrategy
        elif prompting_name == "MapCoder":
            return MapCoder
        elif prompting_name == "Direct":
            return DirectStrategy
        elif prompting_name == "Analogical":
            return AnalogicalStrategy
        elif prompting_name == "SelfPlanning":
            return SelfPlanningStrategy
        elif prompting_name == "Debate":
            return Debate
        elif prompting_name == "Debate-r3":
            return Debate_R3
        elif prompting_name == "Debate-r2":
            return Debate_R2
        elif prompting_name == "DVDCoder":
            return DVDCoder
        elif prompting_name == "SemanticOnly":
            return SemanticOnly
        else:
            raise Exception(f"Unknown prompting name {prompting_name}")
