def generate_member_id(members):
    if not members:
        return 1

    return max(member.member_id for member in members) + 1

#member_id = generate_member_id(all_members)