import math
import types

class Cargo:
    def __init__(self, price: int, floor: int, bLift: bool) -> None:
        if price < 0:
            raise ValueError("Price < 0")
        
        if floor < 0:
            raise ValueError("Floot < 0")
        
        self.__attr_map = {
            "price":  price,
            "floor": floor,
            "bLift": bLift
        }

        self._price = price
        self._floor = floor
        self._bLift = bLift

    def get_price(self) -> int:
        return self._price
    
    def get_floor(self) -> int:
        return self._floor
    
    def get_bLift(self) -> bool:
        return self._bLift

    
    def __setitem__(self, key: str, value):
        if key == "price" and not (isinstance(value, (int, float))) and value < 0:
            raise ValueError("int Price range(0, inf)")

        if key == "floor" and not (isinstance(value, int)) and value < 0:
            raise ValueError("int Floor shoud above 0")
        
        if key == "bLift" and not (isinstance(value, type(self._bLift))):
            raise ValueError(f"bLift invalid type should be {type(self._bLift)}")

        self.__attr_map[key] = value


    def __getitem__(self, key: str) -> None:
        if key not in self.__attr_map:
            raise KeyError(f"Not such key like: {key}")
        return self.__attr_map[key]

    def __len__(self) -> int:
        return self.__attr_map.__len__()
    



class CManager:
    def __init__(self) -> None:
        pass

    def _get_input(self) -> str:
        


        return ""

# CManager 


