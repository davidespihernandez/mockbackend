from app.modules.models.users import User

objects = {
    "00000000-0000-0000-0000-000000000000": User(
        token="00000000-0000-0000-0000-000000000000",
        title="Mr",
        login="test1@test.com",
        first_name="Test 1",
        last_name="User",
        email="test1@test.com",
        address="Address",
        postcode="12345",
        town="Gent",
        country="BE",
        phone="+33 444 555 666",
        language="en_US",
        birthday=None
    ),
    "10000000-0000-0000-0000-000000000000":  User(
        token="10000000-0000-0000-0000-000000000000",
        title="Mr",
        login="test2@test.com",
        first_name="Test 2",
        last_name="User",
        email="test2@test.com",
        address="Address",
        postcode="12345",
        town="Gent",
        country="BE",
        phone="+33 444 555 666",
        language="en_US",
        birthday=None
    ),
}
