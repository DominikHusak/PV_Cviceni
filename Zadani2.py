import re


def build_sql_select_all_from_table(table_name):
    if not re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', table_name):
        raise ValueError("Neplatný název tabulky")
    return f"SELECT * FROM {table_name}"


def build_sql_select_custom_from_users(columns):
    if not all(re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', column) for column in columns):
        raise ValueError("Neplatný název sloupce")
    columns_str = ", ".join(columns)
    return f"SELECT {columns_str} FROM USER"


def build_sql_select_users_order_by_custom(order_by_section):
    if not re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*(\s(ASC|DESC))?$', order_by_section):
        raise ValueError("Neplatná sekce pro řazení")
    return f"SELECT * FROM USER ORDER BY {order_by_section}"

