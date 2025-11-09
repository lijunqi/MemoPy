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


# * field set
class Model(BaseModel):
    field_1: int = 1
    field_2: int | None = None
    field_3: str
    field_4: str | None = "Python"

m1 = Model(field_3="m1")
m2 = Model(field_1=1, field_2=None, field_3="m2", field_4="Py")
m3 = Model(field_1=10, field_2=20, field_3="m3", field_4="Pydantic")
m4 = Model(field_1=10, field_3="m2", field_4="Py")

print("m1 field set: ", m1.model_fields_set)
print("m2 field set: ", m2.model_fields_set)
print("m3 field set: ", m3.model_fields_set)
print("m4 field set: ", m4.model_fields_set)

d1 = {"field_3": "foo"}
m5 = Model.model_validate(d1)
print("m5 field set: ", m5.model_fields_set)

d2 = {"field_2": None, "field_3": "foo"}
m6 = Model.model_validate(d2)
print("m6 field set: ", m6.model_fields_set)
