long BINARY_1S = 0b1111111111111111111111111111111111111111111111111111111111111111;

typedef struct {
    unsigned long arr[1000001 / 64 + 1];
} MyHashSet;


MyHashSet* myHashSetCreate() {
    return (MyHashSet*)calloc(1, sizeof(MyHashSet));
}

void myHashSetAdd(MyHashSet* obj, int key) {
    obj->arr[key / 64] |= 1UL << (key % 64);
}

void myHashSetRemove(MyHashSet* obj, int key) {
    obj->arr[key / 64] &= BINARY_1S - (1UL << (key % 64));
}

bool myHashSetContains(MyHashSet* obj, int key) {
    return (obj->arr[key / 64] & (1UL << (key % 64))) > 0;
}

void myHashSetFree(MyHashSet* obj) {
    free(obj);
}

/**
 * Your MyHashSet struct will be instantiated and called as such:
 * MyHashSet* obj = myHashSetCreate();
 * myHashSetAdd(obj, key);
 
 * myHashSetRemove(obj, key);
 
 * bool param_3 = myHashSetContains(obj, key);
 
 * myHashSetFree(obj);
*/