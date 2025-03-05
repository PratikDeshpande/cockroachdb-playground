

"""
PSEUDO CODE

TODO: Implement as server processing transactions

# Receive a series of requested KV operations from SQL layer (part of transaction)

Operation: (Key to read, commit?) | (Key to update value, Value to update, commit?)


Set inflightOps to []         # these are ops that haven't been replicated (or commited)
set transactionTimeStamp to now

for each operation received:
    operation.timeStamp = transactionTimeStamp
    if operation.commit: # not sure if this means the operation is already replicated or if its a 'commit' designation for an operation
        operation.dependencies = inflightOps        # set dependencies to current inflight ops [why?]
    else:
        operation.dependencies = operationP in inflightlight ops such that operationP key == operation.key # basically all the depencency operations that have the same key
        add operation  # remove operation's dependencies from inglight operations, and ad doperation itself to inflight ops

    #send operation to lease holder and await response
    response = await sendToLeaseHolder(operation)

    if response.timestamp > operation.timestamp:
        if operation.key hasn't changed between (transactionTimeStamp, rsponse.timestamp)
            transactionTimeStamp = response.timestamp  # if the Key hasn't been updated between txn time and lease holder response time, update the transaction timestamp with leaseholder response time
        else:
            fail trasaction
    send response to SQL Layer
    if operation.commit
        asyncronously notify leaseholder to commit operation (or transaction?)
        



"""

# Assumption: Transaction has been broken down into a series of sequential operations by SQL layer, with the last operation being 'commit'
operations = [
    {
        "Type": "READ",
        "K": "key_1001",
        "V": None,
        "commit": False
    },
    {
        "Type": "READ",
        "K": "key_1001",
        "V": None,
        "commit": False
    },
    {
        "Type": "READ",
        "K": "key_1001",
        "V": None,
        "commit": False
    },
    {
        "Type": "READ",
        "K": "key_1001",
        "V": None,
        "commit": False
    },
    {
        "Type": "READ",
        "K": "key_1001",
        "V": None,
        "commit": True
    },

]


print(f"operations: {operations}")

