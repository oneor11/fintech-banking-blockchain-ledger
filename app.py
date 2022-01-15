""" Contains UI presentation and input logic.

    Leverages Streamlit to define input controls that leverage
    blockchain classes that control the addition of Blocks to the
    PyChain blockchain.

"""
import streamlit as st
import pandas as pd
from blockchain.pychain import PyChain
from blockchain.block import Block
from blockchain.record import Record

@st.cache(allow_output_mutation=True)
def setup():
    print("Initializing Chain")
    return PyChain([Block("Genesis", 0)])


st.markdown("# Decentralized Banking Powered by PyChain")
st.markdown("## Store a Transaction Record in the PyChain")

pychain = setup()

# INPUT SECTION ===========================================

sender = st.text_input(
    label = 'Sender: ',
    value = '',
    max_chars = 25
)

receiver = st.text_input(
    label = 'Receiver: ',
    value = '',
    max_chars = 25
)

amount = st.text_input(
    label = 'Amount: ',
    value = '0.00',
)

if st.button("Add Block"):
    prev_block = pychain.chain[-1]
    prev_block_hash = prev_block.hash_block()

    new_block = Block(
        record = Record(sender=sender, receiver=receiver, amount=amount),
        creator_id = 42,
        prev_hash = prev_block_hash)

    pychain.add_block(new_block)
    st.balloons()

st.markdown("## The PyChain Ledger")
# =========================================================


# INFORMATIONAL SECTION ===================================

pychain_df = pd.DataFrame(pychain.chain).astype(str)
st.write(pychain_df)

if st.button("Validate Chain"):
    st.write(pychain.is_valid())
#==========================================================


# SIDEBAR SECTION =========================================

difficulty = st.sidebar.slider("Block Difficulty", 1, 5, 2)
pychain.difficulty = difficulty

st.sidebar.write("# Block Inspector")
selected_block = st.sidebar.selectbox(
    "Which block would you like to see?", pychain.chain
)

st.sidebar.write(selected_block)
#==========================================================
