from returns.result import Success

from src.monad import Error, Person, create_person, fail_create_person, upper_name


class TestPerson:
    def test_person_age(self) -> None:
        person = Person("john", 32)
        assert person.age == 32

    def test_create_person_success(self):
        person = Person("john", 32)
        assert create_person() == Success(person)

    def test_create_person_failure(self):
        result = fail_create_person()
        assert isinstance(result.failure()[0], Error)

    def test_upper(self):
        person = create_person()
        assert person == Success(Person("john", 32))
        upper_person = person.bind_result(upper_name)
        assert upper_person == Success(Person("JOHN", 32))
