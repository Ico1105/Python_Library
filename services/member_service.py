from json_storage import load_json, save_json
from models.member import Member
from user_input import (
    get_first_name,
    get_last_name,
    get_email,
    get_phone,
    get_address,
)
import os
print(os.getcwd())
print(os.listdir())


def generate_member_id(members):
    if not members:
        return 1

    return max(member["member_id"] for member in members) + 1

def add_member():
    members = load_json("storage/members.json")

    first_name = get_first_name().title()
    last_name = get_last_name().title()
    email = get_email()
    phone = get_phone()
    address = get_address().title()
    member_id = generate_member_id(members)

    member = Member(
        member_id=member_id,
        first_name=first_name,
        last_name=last_name,
        email=email,
        phone=phone,
        address=address,
    )

    members.append(member.to_dict())
    save_json("storage/members.json", members)

if __name__ == "__main__":
    add_member()