/*
 * Problem #6 [Hard]
 * An XOR linked list is a more memory efficient doubly linked list.
 * Instead of each node holding next and prev fields, it holds a
 * field named both, which is an XOR of the next node and the
 * previous node. Implement an XOR linked list; it has an
 * add(element) which adds the element to the end, and a get(index)
 * which returns the node at index.
 *
 * If using a language that has no pointers (such as Python), you can
 * assume you have access to get_pointer and dereference_pointer
 * functions that converts between nodes and memory addresses.
 */

#include <stdio.h>
#include <stdlib.h>

struct xornode {
    long int xor;
    int value;
};
typedef struct xornode xornode;

xornode *head;
void add(int);
void print_list();
xornode *get(int);
void get_and_print(int);

void main(int argc, char **argv) {
    printf("Start\n");
    for (int i = 0; i < 19; i += 1) add(i);
    print_list();
    for (int i = 0; i < 20; i += 1) {
        get_and_print(i);
    }
}

xornode *make_node(int value) {
    xornode *result = malloc(sizeof(xornode));
    result->value = value;
    result->xor = 0;
    return result;
}

void add(int value) {
    if (!head) {
        head = make_node(value);
        head->xor = 0;
        return;
    }
    xornode *current = head;
    long int prev = 0;
    while (current->xor) {
        long int next = current->xor ^ prev;
        prev = (long int)current;
        current = (xornode *)next;
    }
    xornode *elem = make_node(value);
    current->xor = (long int)elem ^ (long int)prev;
}

xornode *get(int index) {
    if (!head) return NULL;
    xornode *current = head;
    long int prev = 0;
    for (int i = 0; i < index; i += 1) {
        if (!current->xor) return NULL;
        long int next = current->xor ^ prev;
        prev = (long int)current;
        current = (xornode *)next;
    }
    return current;
}

void get_and_print(int index) {
    xornode *node = get(index);
    if (!node) {
        printf("%d => nil\n", index);
    } else {
        printf("%d => %d\n", index, node->value);
    }
}

void print_list() {
    if (!head) return;
    xornode *current = head;
    long int prev = 0;
    int index = 0;
    printf("%d) %d %p\n", index++, current->value, (void *)current->xor);
    while (current->xor) {
        long int next = current->xor ^ prev;
        prev = (long int)current;
        current = (xornode *)next;
        printf("%d) %d %p\n", index++, current->value, (void *)current->xor);
    }
}
