"""Blank microstrain on list / create projections."""

def blank_value(_v):
    return None

def blank_list_item(item: dict) -> None:
    item["microstrain"] = blank_value(item.get("microstrain"))

def blank_create_item(item: dict) -> None:
    item["microstrain"] = blank_value(item.get("microstrain"))

def should_blank_path(path: str) -> bool:
    return path in {"list", "create"}
