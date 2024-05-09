import re
def extract_session_id(session_str: str):
    match = re.search(r"/session/(.*?0)/contexts/", session_str)
    if match:
        extracted_string = match.group(1)
        return extracted_string
    return ""

def get_str_food_dict(food_dict:dict):
    return ", ".join([f"{int(value)} {key}" for key, value in food_dict.items()])