"""Defines the Record object.

    The Record object defines the minimum banking transaction which is
    the sender, receiver, and amount.  It is one of the attributes in
    the Block object.

    Typical usage example:
    record =  Record('Bank of America', 'Capital One', 5003.23)

"""

from dataclasses import dataclass

@dataclass
class Record:
    """Defines the Record object.

    The Record object defines the minimum banking transaction which is
    the sender, receiver, and amount.  It is one of the attributes in
    the Block object.

    Typical usage example:
    record =  Record('Bank of America', 'Capital One', 5003.23)
    
    Attributes:
        sender: str
            Sender, or originator, of the banking transaction.
        
        receiver: str
            Receiver, or recipient, of the banking transaction.
        
        amount: float
    
    Returns:
        None
    """

    sender: str
    receiver: str
    amount: float
