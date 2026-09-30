QUEUE_BLANK = True
CARD_BLANK = True
DETAIL_BLANK = True

def blank_queue_row(row: dict) -> dict:
    out = dict(row)
    if QUEUE_BLANK:
        out["microstrain"] = None
        out["strain_display"] = ""
    return out

def blank_card(row: dict) -> dict:
    out = dict(row)
    if CARD_BLANK:
        out["microstrain"] = 0
    return out

def blank_detail(row: dict) -> dict:
    out = dict(row)
    if DETAIL_BLANK:
        out["microstrain"] = None
    return out

def project_surfaces(row: dict) -> dict:
    return blank_detail(blank_card(blank_queue_row(row)))
