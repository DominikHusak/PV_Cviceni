import re

def build_sql_select_user_by_username_and_variable_symbol(username, vs):
    if not (re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', username) and re.match(r'^\d+$', str(vs))):
        raise ValueError("Neplatný vstup")
    return f"SELECT * FROM USERS WHERE USERNAME = '{username}' AND VARIABLE_SYMBOL = {vs}"

def build_sql_select_user_by_id(id):
    if not re.match(r'^\d+$', str(id)):
        raise ValueError("Neplatné ID")
    return f"SELECT * FROM USERS WHERE ID = {id}"

def build_sql_select_users_order_by_custom(order_by_section):
    if not re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*(\s(ASC|DESC))?$', order_by_section):
        raise ValueError("Neplatná sekce pro řazení")
    return f"SELECT * FROM USER ORDER BY {order_by_section}"
