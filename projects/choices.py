from enum import Enum


class Priorities(Enum):
    VERY_LOW = (1, "Very low")
    LOW = (2, "Low")
    MEDIUM = (3, "Medium")
    HIGH = (4, "High")
    CRITICAL = (5, "Critical")

    @classmethod
    def choices(cls):
        return [(p.db_value, p.label) for p in cls]

    @property
    def db_value(self) -> int:
        return self.value[0]

    @property
    def label(self) -> str:
        return self.value[1]

    def __str__(self) -> str:
        return self.label


class Positions(str, Enum):
    CEO = "CEO"
    CTO = "CTO"
    DESIGNER = "DESIGNER"
    PROGRAMMER = "PROGRAMMER"
    PRODUCT_OWNER = "PRODUCT_OWNER"
    PROJECT_OWNER = "PROJECT_OWNER"
    PROJECT_MANAGER = "PROJECT_MANAGER"
    QA = "QA"

    @classmethod
    def choices(cls):
        return [(attr.name, attr.value) for attr in cls]

    def __str__(self):
        return self.value


class Statuses(str, Enum):
    NEW = "NEW"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    CLOSED = "CLOSED"
    PENDING = "PENDING"
    BLOCKED = "BLOCKED"

    @classmethod
    def choices(cls):
        return [(attr.name, attr.value) for attr in cls]

    def __str__(self):
        return self.value
