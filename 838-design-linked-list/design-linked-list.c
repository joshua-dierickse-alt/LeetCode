typedef struct Node {
    int val;
    struct Node* next;
} Node;

typedef struct {
    Node* head;
    Node* tail;
    int size;
} MyLinkedList;


MyLinkedList* myLinkedListCreate() {
    MyLinkedList* obj = (MyLinkedList*)malloc(sizeof(MyLinkedList));
    obj->head = (Node*)malloc(sizeof(Node));
    obj->tail = (Node*)malloc(sizeof(Node));
    obj->head->next = obj->tail;
    obj->tail->next = NULL;
    obj->size = 0;
    return obj;
}

Node* myLinkedListGetNode(MyLinkedList* obj, int index) {
    if (index > obj->size) return NULL;

    Node* node = obj->head;

    for (int i = 0; i < index; i++)
        node = node->next;
    
    return node;
}

int myLinkedListGet(MyLinkedList* obj, int index) {
    Node* node = myLinkedListGetNode(obj, index + 1);

    if (node == NULL)
        return -1;
    
    return node->val;
}

void myLinkedListAddAtIndex(MyLinkedList* obj, int index, int val) {
    Node* node = myLinkedListGetNode(obj, index);

    if (node == NULL) return;

    Node* old_next = node->next;
    node->next = (Node*)malloc(sizeof(Node));
    node->next->val = val;
    node->next->next = old_next;
    obj->size += 1;
}

void myLinkedListAddAtHead(MyLinkedList* obj, int val) {
    myLinkedListAddAtIndex(obj, 0, val);
}

void myLinkedListAddAtTail(MyLinkedList* obj, int val) {
    myLinkedListAddAtIndex(obj, obj->size, val);
}

void myLinkedListDeleteAtIndex(MyLinkedList* obj, int index) {
    Node* node = myLinkedListGetNode(obj, index);

    if (index < 0 || index >= obj->size) return;

    if (node == NULL) return;

    Node* old_next = node->next;

    node->next = node->next->next;
    free(old_next);
    obj->size -= 1;
}

void myLinkedListFree(MyLinkedList* obj) {
    Node* node = obj->head;

    while (node) {
        Node* old_node = node;
        node = node->next;
        free(old_node);
    }
    
    free(obj);
}

/**
 * Your MyLinkedList struct will be instantiated and called as such:
 * MyLinkedList* obj = myLinkedListCreate();
 * int param_1 = myLinkedListGet(obj, index);
 
 * myLinkedListAddAtHead(obj, val);
 
 * myLinkedListAddAtTail(obj, val);
 
 * myLinkedListAddAtIndex(obj, index, val);
 
 * myLinkedListDeleteAtIndex(obj, index);
 
 * myLinkedListFree(obj);
*/