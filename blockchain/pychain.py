"""Defines the PyChain object.

    The PyChain object defines the protocol or rules for the banking
    blockchain. It enables the proof of work validation before adding
    a block as well as functionality to determine if the chain is 
    valid.

    Typical usage example:
    pychain =  PyChain([Block("Genesis", 0)])

"""

from dataclasses import dataclass
from typing import List
from blockchain.block import Block

@dataclass
class PyChain:
    """Represents the protocol or rules for the banking blockchain.

    It enables the proof of work validation before adding
    a block as well as functionality to determine if the chain is 
    valid.
    
    Attributes:
        chain: List[Block]
            Contains a List of all of the Blocks added to the
            blockchain.  The first Block will be a Genesis Block with
            prev_hash of 0.  From then on each new block will contain
            the SHA-256 hash of the previous Block's encoded
            attributes.
        
        difficulty: int
            Defines the difficulty of solving the hash puzzle required
            to add a block to the blockchain.  The number represents
            how many zeros the hash of the Block's encoded attributes
            needs to start with.

    """

    chain: List[Block]
    difficulty: int = 4


    def proof_of_work(self, block):
        """Solves a computation puzzle required to add the Block.
        
        A miner must execute proof_of_work to solve a computational
        puzzle requiring that the block's hash begin with a certain
        amount of zeroes defined by the PyChain difficulty attribute.

        The Block's hash can be recomputed multiple times without
        modifying the data by manipulating the Block's nonce attribute.

        Args:
            self: PyChain
                this PyChain class.

            block: Block
                the candidate block targeted for addition to the
                blockchain.

        Returns:
            The candidate Block with a nonce attribute value that
            solves the puzzle. 

        """        

        calculated_hash = block.hash_block()
        num_of_zeros = "0" * self.difficulty

        while not calculated_hash.startswith(num_of_zeros):
            block.nonce += 1
            calculated_hash = block.hash_block()

        return block


    def add_block(self, candidate_block):
        """Adds a Block to the blockchain.
        
        Orchestrates the proof of work challenge and upon resolution of
        the puzzle adds the Block to the blockchain.

        Args:
            self: PyChain
                this PyChain class.

            candidate_block: Block
                the candidate block targeted for addition to the
                blockchain.

        Returns:
            None

        """

        block = self.proof_of_work(candidate_block)
        self.chain += [block]


    def is_valid(self):
        """Determines if the entire blockchain is valid.
        
        A valid blockchain requires that the prev_hash attribute of
        every Block on the blockchain matches the SHA-256 hash of the
        previous Block's encoded attributes.

        Args:
            self: PyChain
                this PyChain class.

        Returns:
            True if blockchain is valid, False if invalid.

        """

        block_hash = self.chain[0].hash_block()

        for block in self.chain[1:]:
            if block_hash != block.prev_hash:
                return False

            block_hash = block.hash_block()

        return True
