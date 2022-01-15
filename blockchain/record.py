from dataclasses import dataclass

@dataclass
class Record:
    sender: str
    receiver: str
    amount: float
