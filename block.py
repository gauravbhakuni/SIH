import hashlib

# Function to extract CIDs from a text file
def extract_cids_from_file(file_path):
    cids = []
    with open(file_path, 'r') as file:
        for line in file:
            # Assuming each line contains "Uploaded Row CID: CID_VALUE"
            if line.startswith("Uploaded Row CID: "):
                cid = line[len("Uploaded Row CID: "):].strip()
                cids.append(cid)
    return cids

def hashGenerator(data):
    result = hashlib.sha256(data.encode()).hexdigest()
    return result

class Block:
    def __init__(self, cid, hash, prev_hash):
        self.cid = cid  # Store the CID instead of generic data
        self.hash = hash
        self.prev_hash = prev_hash

class Blockchain:
    def __init__(self, file_path):
        hashLast = hashGenerator('gen_last')
        hashStart = hashGenerator('gen_hash')

        genesis = Block('YOUR_GENESIS_CID', hashStart, hashLast)
        self.chain = [genesis]

        cids = extract_cids_from_file(file_path)
        for cid in cids:
            self.add_block(cid)

    def add_block(self, cid):
        prev_hash = self.chain[-1].hash
        data_to_hash = cid + prev_hash
        hash = hashGenerator(data_to_hash)
        block = Block(str(cid), hash, prev_hash)
        self.chain.append(block)

    def cid_exists(self, target_cid):
        # Check if the given CID exists in the blockchain
        for block in self.chain:
            if block.cid == target_cid:
                return True
        return False

if __name__ == "__main__":
    # Path to your text file containing CIDs
    file_path = 'data.txt'

    # Extract CIDs from the file
    cids = extract_cids_from_file(file_path)

    # Create a blockchain instance
    bc = Blockchain(file_path)

    # Check the existence of each CID
    for cid in cids:
        exists = bc.cid_exists(cid)
        print(f"CID {cid} exists in the blockchain: {exists}")
