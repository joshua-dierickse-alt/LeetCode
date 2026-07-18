typedef struct {
    bool arr[1000001]    
} MyHashSet;


MyHashSet* myHashSetCreate() {
    MyHashSet* my_hash_set = (MyHashSet*) malloc(sizeof(MyHashSet));

    for (int i = 0; i < 1000001; i++)
        my_hash_set->arr[i] = false;

    return my_hash_set;
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