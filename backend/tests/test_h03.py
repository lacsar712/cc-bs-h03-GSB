from h03_extra_trap import apply_blank
from h03_map_trap import map_list_payload

def test_blank():
    d = {"microstrain": 150}
    apply_blank(d, "list")
    assert d["microstrain"] is None
    rows = map_list_payload([{"microstrain": 150}])
    assert rows[0]["microstrain"] in (0, None)
