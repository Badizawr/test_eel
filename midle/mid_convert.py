from back.convert import converter_value
import eel

@eel.expose
def convert_value_py(value: float, from_cur:str, to_cur:str)->float:
    return converter_value(value, from_cur, to_cur)
