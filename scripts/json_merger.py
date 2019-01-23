from pprint import pprint
import json

if __name__ == "__main__":
    with open("backend/scripts/db_anonymizer_whitelist.json") as original_whitelist, open("backend/scripts/loose.json") as loose_fks:
        original_whitelist = json.load(original_whitelist)
        loosefk_whitelist = json.load(loose_fks)
        ohmerged = {}

        for db in original_whitelist:
            whitelisted_fields = set(original_whitelist[db])
            loose_fields = set(loosefk_whitelist.get(db, []))
            ohmerged[db] = sorted(list(whitelisted_fields.union(loose_fields)))

        print(json.dumps(ohmerged, sort_keys=True, indent=2))
