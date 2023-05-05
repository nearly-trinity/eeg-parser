from dataclasses import dataclass
from typing import List

@dataclass
class ElectrodeData:
    Fp1: float
    Fp2: float
    F7: float
    F3: float
    Fz: float
    F4: float
    F8: float
    FC3: float
    FCz: float
    FC4: float
    T7: float
    C3: float
    Cz: float
    C4: float
    T8: float
    CP3: float
    CPz: float
    CP4: float
    P7: float
    P3: float
    Pz: float
    P4: float
    P8: float
    O1: float
    Oz: float
    O2: float
    VPVA: float
    VNVB: float
    HPHL: float
    HNHR: float
    Erbs: float
    OrbOcc: float
    Mass: float

@dataclass
class ElectrodeDataList:
    data: List[ElectrodeData]