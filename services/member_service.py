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
        print(f"{member['member_id']}. {member['first_name']} {member['last_name']}")
    member_id = int(input("Enter the member ID to edit: "))
    for member in members:
        if member["member_id"] == member_id:
            fields = {k: v for k, v in member.items() if k != "member_id"}
            for i, (k, v) in enumerate(fields.items(), start=1):
                print(f"{i}. {k}: {v}")
            choice = int(input("Enter the field you want to edit: "))

            edit_function = {
                "first_name": get_first_name,
                "last_name": get_last_name,
                "email": get_email,
                "phone": get_phone,
                "address": get_address,
            }
            field = list(fields.keys())[choice - 1]
            get_value = edit_function[field]
            new_value = get_value()
            member[field] = new_value
            save_json("storage/members.json", members)



            print("===========================")

def show_all_members():
    members = load_json("storage/members.json")
    for member in members:
        print(f"Member ID: {member['member_id']}. \n"
              f"Name: {member['first_name']} {member['last_name']}\n"
              f"Email: {member['email']}\n"
              f"Phone: {member['phone']}\n"
              f"Address: {member['address']}\n")
        print("=" * 20)

def delete_member():
    members = load_json("storage/members.json")
    rentals = load_json("storage/rentals.json")
    archive = load_json("storage/archive.json")


    for member in members:
        print(f"{member['member_id']}."
              f" {member['first_name']}"
              f" {member['last_name']}")
    member_id = int(input("Enter the member ID to delete: "))

    # Check active rentals
    for rental in rentals:
        if rental['member_id'] == member_id and rental['return_date'] is None:
            print("Member has an active rental. Cannot delete.")
            return

    for member in members:
            if member["member_id"] == member_id:
                members.remove(member)
                archive.append(member)

                save_json("storage/members.json", members)
                save_json("storage/archive.json", archive)
                print("Member deleted successfully.")
                return

    print("Member not found.")

if __name__ == "__main__":
    show_all_members()