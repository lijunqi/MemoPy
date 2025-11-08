from pydantic import BaseModel, ValidationError

class Person(BaseModel):
    first_name: str
    last_name: str
    age: int


data_dict = {
    "first_name": "Issac",
    "last_name": "Newton",
    "age": 20
}
newton = Person.model_validate(data_dict)
print("newton:", newton)

# * Serialization
json_str = newton.model_dump_json()
print(f"Serialization to json string:\n \t {json_str}, Type: {type(json_str)}")

newton_dict = newton.model_dump(exclude={"first_name", "age"})
print("[Exclude serialization]:\n \t newton_dict = ", newton_dict)

newton_dict = newton.model_dump(include={"first_name"})
print("[Include serialization]:\n \t newton_dict = ", newton_dict)
