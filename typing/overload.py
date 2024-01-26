"""
The @overload-decorated definitions are for the benefit of the type checker only,
since they will be overwritten by the non-@overload-decorated definition,
while the latter is used at runtime but should be ignored by a type checker.
"""

from typing import overload

# * ONLY for type checker
@overload
def process(response: None) -> None:
    ...

@overload
def process(response: int) -> tuple[int, str]:
    ...

@overload
def process(response: bytes) -> str:
    ...

# * Be ignored by type checker
def process(response):
    return response

response = None
print("1. This is response: ", process(response))

response = 123
print("2. This is response: ", process(response))

response = b"asdf"
print("3. This is response: ", process(response))

response = [1,2,3]
print("4. This is response: ", process(response))
