"""
You are given a dictionary where the keys are strings and the values are strings or dictionaries. The goal is flatten
the dictionary, but save the structures in the keys. The result should be the a dictionary without the nested
dictionaries. The keys should contain paths that contain the parent keys from the original dictionary. The keys in
the path are separated by a "/". If a value is an empty dictionary, then it should be replaced by an empty string ("").
Let's look at an example:
{
    "name": {
        "first": "One",
        "last": "Drone"
    },
    "job": "scout",
    "recent": {},
    "additional": {
        "place": {
            "zone": "1",
            "cell": "2"}
    }
}

The result will be:
{"name/first": "One",           # one parent
 "name/last": "Drone",
 "job": "scout",                # root key
 "recent": "",                  # empty dict
 "additional/place/zone": "1",  # third level
 "additional/place/cell": "2"}
"""
def flatten(d: dict, parent_key='', sep='/') -> dict:
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            if v == {}:
                items.append((new_key, ''))
            else:
                items.extend(flatten(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)




assert flatten({"key": "value"}) == {"key": "value"}
assert flatten({"key": {"deeper": {"more": {"enough": "value"}}}}) == {
    "key/deeper/more/enough": "value"
}
assert flatten({"empty": {}}) == {"empty": ""}
assert flatten(
    {
        "name": {"first": "One", "last": "Drone"},
        "job": "scout",
        "recent": {},
        "additional": {"place": {"zone": "1", "cell": "2"}},
    }
) == {
    "name/first": "One",
    "name/last": "Drone",
    "job": "scout",
    "recent": "",
    "additional/place/zone": "1",
    "additional/place/cell": "2",
}

