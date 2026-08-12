from json_storage import load_json, save_json
from models.member import Member
from user_input import (
    get_first_name,
    get_last_name,
    get_email,
    get_phone,
    get_address,
)

def generate_member_id(members):
    if not members:
        return 1

    return max(member["member_id"] for member in members) + 1

def add_member():
    members = load_json("storage/members.json")

    first_name = get_first_name()
    last_name = get_last_name()
    email = get_email()
    phone = get_phone()
    address = get_address()
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

def edit_member():
    members = load_json("storage/members.json")
    for member in members:
        print(f"{member['member_id']}: {member['first_name']} {member['last_name']}")
    member_id = int(input("Enter the member ID to edit: "))
    for member in members:
        if member["member_id"] == member_id:
            for k, v in member.items():
                print(f"{k}: {v}")
            print("===========================")

    print("1. First name")
    print("2. Last name")
    print("3. Email")
    print("4. Phone")
    print("5. Address")

    choice = input("Enter the field you want to edit: ")




def delete_member():
    pass

if __name__ == "__main__":
    edit_member()