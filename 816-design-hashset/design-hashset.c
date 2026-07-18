typedef struct {
    bool arr[1000001];
} MyHashSet;


MyHashSet* myHashSetCreate() {
    return (MyHashSet*) calloc(1, sizeof(MyHashSet));
}

void myHashSetAdd(MyHashSet* obj, int key) {
    obj->arr[key] = true;
}

void myHashSetRemove(MyHashSet* obj, int key) {
    obj->arr[key] = false;
}

bool myHashSetContains(MyHashSet* obj, int key) {
    return obj->arr[key];
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