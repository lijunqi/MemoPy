from pydantic import BaseModel, ConfigDict, ValidationError

class Model(BaseModel):
    model_config = ConfigDict(validate_assignment=True, validate_default=True)
    field_1: int
    field_2: int = None

m = Model(field_1=10)
try:
    m.field_1 = "python"
except ValidationError as ex:
    print(ex)
