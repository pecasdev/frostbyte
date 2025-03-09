from dataclasses import dataclass, replace

from returns.result import Success, Result, Failure


@dataclass
class Error:
    message: str
    status: int


type Errors = list[Error]
type AppResult[A] = Result[A, Errors]


@dataclass
class Person:
    name: str
    age: int


def create_person() -> AppResult[Person]:
    result: AppResult[Person] = Success(Person("john", 32))
    return result


def fail_create_person() -> AppResult[Person]:
    result: AppResult[Person] = Failure([Error("something happened", 500)])
    return result


def upper_name(person: Person) -> AppResult[Person]:
    return Success(person).map(lambda x: replace(x, name=x.name.upper()))
