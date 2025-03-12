party_list1 = {"Silas", "Cher", "Mom"}
party_list2 = {"Silas", "Shawn", "Brandon", "Angel"}
grand_party = party_list1.union(party_list2)
print(grand_party)

# .union() to merge sets
# .add() to add to a set
# .remove() to remove an element
# .pop() will randomly remove an element in a set
# .difference() returns a new set with elements in the first set but not in the second.
# .intersection() find what's in common
# .symetric_difference() finds what's exculsive is each list

find_the_difference = party_list1.difference(party_list2)
print(find_the_difference)

find_whats_in_common = party_list1.intersection(party_list2)
print(find_whats_in_common)

find_symetrical_difference = party_list1.symmetric_difference(party_list2)
print(find_symetrical_difference)

for index, guest in enumerate(sorted(grand_party)):
    print(f"Guest #{index + 1}: {guest}")