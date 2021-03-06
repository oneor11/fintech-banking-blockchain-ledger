# Banking Blockchain Ledger

Example of a blockchain-based ledger system, complete with a user-friendly web interface. This ledger allows partner banks to conduct financial transactions (that is, to transfer money between senders and receivers) and to verify the integrity of the data in the ledger.  The example demonstrates chaining blocks on the chain via hash linking, proof of work, dynamic adjustments to proof of work difficulty, and blockchain validation.

## Technologies Used

The application uses the following technologies:

- Python 3.7
- [pandas](https://pandas.pydata.org/pandas-docs/stable/index.html)
- [streamlit](https://streamlit.io)

## Installation Guide

```python

pip install pandas
pip install streamlit

```

## Usage

There are four blockchain workflows in this demo:

1. Adding a transaction to the PyChain blockchain
2. Validating the entire PyChain blockchain
3. Dynamically adjusting the proof of work difficulty
4. Viewing a specific raw block on the PyChain

Blocks for transactions are constructed from user input facilitated through the Streamlit UI.  To launch the application open a terminal, navigate to the project directory, and run the following code in the Python virtual environment where Streamlit is installed:

```python

streamlit run app.py

```

### Adding a transaction to the PyChain blockchain

![screenshot of transaction entry form](images/store_transaction.png)

On the **Store a Transaction Record on the PyChain** section of the app:

- Enter the **Sender**, or originator, of the transaction. In the example above *Capital One* was entered.
- Enter the **Receiver**, or recipient, of the transaction. In the example above *Chevron Federal Credit Union* was entered.
- Enter a numeric amount in the **Amount** text box.
- Click the **Add Block** button.

When the transaction has been successfully added to the PyChain, a success message will appear. The amount of time required to add to the blockchain is dependent upon the proof of work difficulty setting in the left bar.  Added transactions will appear in the **PyChain Ledger** section of the app for further review.

### Validating the entire PyChain blockchain

![screenshot of PyChain ledger section](images/pychain_ledger.png)

Click the **Validate Chain** button to validate the PyChain blockchain.  Each block on the PyChain blockchain contains a SHA-256 hash of all of the *previous* block's encoded attributes.  The chain is validated if every block's "previous hash" matches the actual hash of the previous block all the way from the Genesis (first) block through the last block.

Code snippet of blockchain validation method:

```python
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
```

### Dynamically adjusting the proof of work difficulty

![screenshot of Block Difficulty slider](images/block_difficulty.png)

The PyChain blockchain uses [proof of work](https://www.investopedia.com/terms/p/proof-work.asp) to secure it from malicious attacks.  In this example the miner must arrive at a hash for the current block that matches a pattern of *beginning zeroes*.  Block objects on the PyChain have a [nonce](https://www.investopedia.com/terms/n/nonce.asp) attribute that can be repeatedly set by miners to programmatically re-hash the block until the *beginning zeroes* requirement is met (See code example below).  When the requirement is met, the block can be added to the chain. The number of beginning zeroes is set via the **Block Difficulty** slider on the left side of the application.  The newly selected difficulty will take effect the next time the **Add Block** button is clicked to add a transaction.

Code snippet of proof of work method:

```python

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

```

### Viewing a specific raw block on the PyChain

![screenshot of Block Inspector dropdown list](images/block_inspector.png)

Transactions can be viewed in the **PyChain Ledger** section of the app, but can also be viewed in their *raw* form by using the **Block Inspector**.  This view shows the data as-is its native Python List.  To view the data, simply click the dropdown listbox and click on the desired transaction.

## Note on Demo

This is intended to be a demo of a custom-constructed blockchain to discuss key concepts and not a production-ready implementation.  Many improvements would be needed for such an endeavor including software engineering standards such as error handling and logging.  From a blockchain perspective, features would be needed that distribute the blockchain to nodes as well as facilitate communication between them.

## Contributors

- Jacob Rougeau

## License

MIT
