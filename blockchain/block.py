"""Defines the Block object.

    The Block object represents the data from one transaction on the 
    blockchain.

    Typical usage example:
    block =  Block()

"""

import datetime as datetime
import hashlib
from dataclasses import dataclass
from blockchain.record import Record

@dataclass
class Block:
    """Represents the data from one transaction on the blockchain.
    
    Attributes:
        record: Record
            Object that contains the sender, receiver, and amount data
            from a banking transaction.
        
        creator_id: int
            Unique identifier of the entity constructing the block.
        
        prev_hash: str
            SHA-256 hash of all encoded attributes in the Block object 
            that was added to blockchain preceding this one.  This 
            enables chain linking of Blocks which in turn enables
            validation of the chain.

        timestamp: datetime
            Time the block was programatically constructed (UTC) in
            %H:%M:%S format.
        
        nonce: int
            A number field that can be used by blockchain miners and 
            validators to iteratively change the hash of this object 
            until the required validation pattern is met.
    """

    record: Record
    creator_id: int
    prev_hash: str = "0"
    timestamp: str = datetime.datetime.utcnow().strftime("%H:%M:%S")
    nonce: int = 0

    def hash_block(self):
        """Creates a hash of the block
        
        Leverages SHA-256 hashing to create a hash of all of the
        attributes within this class.

        Args:
            self: Block
                this Block class.

        Returns:
            A str containing the hash of all attributes within this
            class. Note that timestamp is also hashed, so identical
            data will return a different hash.

        """
        
        sha = hashlib.sha256()

        record = str(self.record).encode()
        sha.update(record)

        creator_id = str(self.creator_id).encode()
        sha.update(creator_id)

        timestamp = str(self.timestamp).encode()
        sha.update(timestamp)

        prev_hash = str(self.prev_hash).encode()
        sha.update(prev_hash)

        nonce = str(self.nonce).encode()
        sha.update(nonce)

        return sha.hexdigest()