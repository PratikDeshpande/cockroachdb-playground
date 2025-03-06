

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
import time

# TODO: This is algo 2 in the paper. Implement
def sendToLeaseHolder(operation: dict)->dict:
    print(f"sending OPERATION {operation} to lease holder node")

    returnValue = None
    if operation.get("Type") != None and operation["Type"] == "READ":
        returnValue = "value_2001"

    time.sleep(2)
    timestamp = time.time()
    return {
        "operation": operation,
        "returnValue": returnValue,
        "timestamp": timestamp,
    }

def processTransaction(operations: list[dict]):
    inflightOperations = []
    transactionTimeStamp = time.time()


    for operation in operations:
        operation['timestamp'] = transactionTimeStamp

        if operation['commit'] == True:
            operation['dependencies'] = inflightOperations
        else:
            # operation.dependencies = operationP in inflightlight ops such that operationP key == operation.key # basically all the depencency operations that have the same key
            operationDependences = [operationPrime for operationPrime in inflightOperations if operationPrime['K'] == operation['K']]
            operation['dependencies'] = operationDependences


            # remove operation's dependencies from inflight operations, and add operation itself to inflight ops
            inflightOperations = [inflightOperation for inflightOperation in inflightOperations if inflightOperation in operation['dependencies']]
            inflightOperations.append(operation)

        # send operation to lease holder and await response
        response = sendToLeaseHolder(operation)
        print(f"response from lease holder: {response}")

        # if response time tamp is greater than op timestamp
            # if operation k is the same between (txn timestamp, response time stamp):
                # transactionTimeStamp = response["timestamp"]
            # else:
                # throw error
        # send response to SQL Layer
        # if operation is commit operation
            # notify lease holder to commit transaction


# Assumption: Transaction has been broken down into a series of sequential operations by SQL layer, with the last operation being 'commit'
operations = [
    {
        "Type": "READ",
        "K": "key_1001",
        "V": None,
        "commit": False
    },
    {
        "Type": "WRITE",
        "K": "key_1001",
        "V": 534673,
        "commit": False
    },
    {
        "Type": "READ",
        "K": "key_1005",
        "V": None,
        "commit": False
    },
    {
        "Type": "WRITE",
        "K": "key_1005",
        "V": "ssaftasf",
        "commit": False
    },
    {
        "Type": "READ",
        "K": "key_1005",
        "V": None,
        "commit": True
    },

]


print(f"operations: {operations}")

processTransaction(operations)
