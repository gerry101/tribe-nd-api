def userEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "email": item["email"],
    }


def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]
