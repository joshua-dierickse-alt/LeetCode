/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    int pairSum(ListNode* head) {
        ListNode* t = head;
        ListNode* h = head;
        ListNode* p = nullptr;
        ListNode* n = nullptr;

        while (h) {
            h = h->next;
            if (h) h = h->next;

            n = t->next;
            t->next = p;
            p = t;
            t = n;
        }

        int m = 0;

        while (p && t) {
            m = max(m, p->val + t->val);
            p = p->next;
            t = t->next;
        }

        return m;
    }
};