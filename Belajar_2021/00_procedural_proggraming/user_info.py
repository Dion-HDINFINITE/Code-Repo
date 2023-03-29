
def build_profile(first, last, **info):
    info["fullname"] = f"{first.title()} {last.title()}"
    return info


user_profile = build_profile("albert", "einstein", location="princeton", field="physics")

print(user_profile)