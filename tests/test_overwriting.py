from json_to_object.deserializer import deserialize


class SomeModel:
    def __init__(self):
        self.name = None
        self.surname = None
        self.full_name = [self.name, self.surname]
        self.address = {None, None}


def test_list_with_none_can_be_overwritten():
    name = 'John'
    surname = 'Snow'
    full_name = ['John', 'Snow']
    new_model = deserialize({'name': name, 'surname': surname, 'full_name': full_name}, SomeModel())

    assert new_model.name == name
    assert new_model.surname == surname
    assert new_model.full_name == full_name


def test_dict_with_none_can_be_overwritten():
    address_data = {'city': 'York', 'street': '146 baker street'}
    new_model = deserialize({'address': address_data}, SomeModel())

    assert new_model.address == address_data
