from enum import Enum

from pydantic import BaseModel, ConstrainedStr

TASKS: list[dict[str, str]] = []


class TaskTitle(ConstrainedStr):
    min_length = 3
    max_length = 50


class TaskDescription(ConstrainedStr):
    max_length = 50


class Status(str, Enum):
    finalized = "Finalized"
    not_finalized = "Not finalized"


class InputTask(BaseModel):
    title: TaskTitle
    description: TaskDescription
    status: Status = Status.not_finalized


class OutputTask(InputTask):
    id: str
