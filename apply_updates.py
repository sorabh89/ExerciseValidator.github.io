import json
from collections import defaultdict

# Read the files
print("Reading files...")
with open('aggregated_output.json', 'r') as f:
    aggregated_data = json.load(f)

with open('updates_consolidated.json', 'r') as f:
    updates = json.load(f)

print(f"Total records in aggregated_output.json: {len(aggregated_data)}")
print(f"Total updates in updates_consolidated.json: {len(updates)}")
print()

# Create a map of code to record index in aggregated_data
code_to_index = {record['code']: idx for idx, record in enumerate(aggregated_data)}

# Track which fields are being updated
fields_updated = defaultdict(int)
records_updated = 0
records_not_found = []

# Apply updates
for update in updates:
    update_code = update['code']
    
    if update_code in code_to_index:
        idx = code_to_index[update_code]
        original_record = aggregated_data[idx]
        
        # Track which fields are being updated for this record
        for key, value in update.items():
            if key in original_record:
                # Check if the value is different
                if original_record[key] != value:
                    fields_updated[key] += 1
                    original_record[key] = value
            else:
                # This is a new field being added
                fields_updated[key] += 1
                original_record[key] = value
        
        records_updated += 1
    else:
        records_not_found.append(update_code)

# Display results
print("=" * 60)
print("FIELDS UPDATED:")
print("=" * 60)
for field, count in sorted(fields_updated.items()):
    print(f"  {field:30} {count:4} records updated")

print()
print("=" * 60)
print("SUMMARY:")
print("=" * 60)
print(f"  Total records updated:         {records_updated}")
print(f"  Total records not found:       {len(records_not_found)}")
print(f"  Unique fields modified:        {len(fields_updated)}")
print()

if records_not_found:
    print("Records not found in aggregated_output.json:")
    for code in records_not_found[:10]:  # Show first 10
        print(f"  - {code}")
    if len(records_not_found) > 10:
        print(f"  ... and {len(records_not_found) - 10} more")

# Write the updated data back
print()
print("Writing updated data to aggregated_output.json...")
with open('aggregated_output.json', 'w', encoding='utf-8') as f:
    json.dump(aggregated_data, f, indent=2, ensure_ascii=False)

print("✓ Update complete!")
