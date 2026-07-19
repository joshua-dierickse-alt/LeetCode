struct Trie {
    bool complete_word;
    struct Trie* arr[26];
};

typedef struct Trie Trie;

Trie* trieCreate() {
    Trie *trie = calloc(1, sizeof(Trie));

    return trie;
}

void trieInsert(Trie* obj, char* word) {
    char c = word[0];

    if (c == '\0') {
        obj->complete_word = true;
        return;
    }

    c -= 'a';

    if (obj->arr[c] == NULL)
        obj->arr[c] = calloc(1, sizeof(Trie));

    trieInsert(obj->arr[c], word + 1);
}

Trie* getNode(Trie *obj, char *word) {
    char c = word[0];

    if (c == '\0')
        return obj;

    c -= 'a';

    if (obj->arr[c] == NULL)
        return NULL;

    return getNode(obj->arr[c], word + 1);
}

bool trieSearch(Trie* obj, char* word) {
    Trie *node = getNode(obj, word);

    return node != NULL && node->complete_word;
}

bool trieStartsWith(Trie* obj, char* prefix) {
    Trie *node = getNode(obj, prefix);

    return node != NULL;
}

void trieFree(Trie* obj) {
    if (obj == NULL)
        return;

    for (int i = 0; i < 26; i++)
        trieFree(obj->arr[i]);

    free(obj);
}

/**
 * Your Trie struct will be instantiated and called as such:
 * Trie* obj = trieCreate();
 * trieInsert(obj, word);
 
 * bool param_2 = trieSearch(obj, word);
 
 * bool param_3 = trieStartsWith(obj, prefix);
 
 * trieFree(obj);
*/