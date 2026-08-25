from pydantic import BaseModel


class TrainRequest(BaseModel):

    version_id: int

    target_column: str

    algorithm: str

    test_size: float = 0.2

    random_state: int = 42