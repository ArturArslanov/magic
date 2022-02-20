from data.users import User


def add_team(db_session):
    session = db_session.create_session()
    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    user.set_password("cap")
    session.add(user)
    session.commit()

    user = User()
    user.surname = "Marli"
    user.name = "Rayner"
    user.age = 25
    user.position = "colonist"
    user.speciality = "dragon pilot"
    user.address = "module_3"
    user.email = "Rayner_ray@mars.org"
    user.set_password("i`m_armored")
    session.add(user)
    session.commit()

    user = User()
    user.surname = "Holmes"
    user.name = "Sherlock"
    user.age = 25
    user.position = "colonist"
    user.speciality = "detective consultant"
    user.address = "module_2"
    user.email = "Sheri_shegi@mars.org"
    user.set_password('I`m_sherlocked')
    session.add(user)
    session.commit()

    session = db_session.create_session()
    user = User()
    user.surname = "Watson"
    user.name = "John"
    user.age = 28
    user.position = "colonist"
    user.speciality = "doctor"
    user.address = "module_4"
    user.email = "John_John@mars.org"
    user.set_password('i_Love_Mary_Morstn')
    session.add(user)
    session.commit()
