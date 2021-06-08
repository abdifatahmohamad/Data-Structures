// Common Hash function example:
const hash = (key, size) => {
    let hashedKey = 0;

    for(let i=0; i<key.length; i++){
        hashedKey = key.charCodeAt(i);
    }

    return hashedKey % size;
}

// Create our hashTable class
class HashTable{
    constructor(){
        this.size = 20;
        this.buckets = Array(this.size);

        // Store hashMapsh using ES6 maps
        for(let i=0; i<this.buckets.length; i++){
            this.buckets[i] = new Map();
        }
    }
    // Create insert method:
    insert(key, value){
        // To get the index of the array to store our values, we need to hash the key
        let idx = hash(key, this.size);
        // Access the buckets at the above idx
        this.buckets[idx].set(key, value);
    }

    // Create remove method:
    remove(key){
        // To get the index of the array to store our values, we need to hash the key
        let idx = hash(key, this.size);
        // Store the value to be deleted in a variable
        let deleted = this.buckets[idx].get(key);
        // Delete the item
        this.buckets[idx].delete(key);
        return deleted;
    }

    // Create search method:
    search(key){
        // To get the index of the array to store our values, we need to hash the key
        let idx = hash(key, this.size);
        return this.buckets[idx].get(key);
    }
}

const hashTable = new HashTable();

hashTable.insert('Vandam', 'John');
hashTable.insert('Micheal', 'Dave');
hashTable.insert('Teslo', 'Montinho');
hashTable.insert('Bitcoin', 'Cardano');
hashTable.insert('BitTorrent', 'Shiba');
hashTable.insert('Safemoon', 'Pundi X');
hashTable.insert('Ethereum', 'Litcoin');

hashTable.search('Bitcoin');
hashTable.search('Ethereum');
hashTable.search('Vandam');

hashTable.remove('BitTorrent');
hashTable.remove('Micheal');

console.log(hashTable);