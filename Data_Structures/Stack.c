#include <stdio.h>
#include <stdlib.h>

typedef struct {
  int *data;
  int count;
  int capacity;
} Stack;

void init(Stack *s) {
  s->data = NULL;
  s->count = 0;
  s->capacity = 0;
}

void push(Stack *s, int value) {
  if (s->count == s->capacity) {
    s->capacity = s->capacity == 0 ? 1 : s->capacity * 2;
    s->data = realloc(s->data, s->capacity * sizeof(int));
    if (s->data == NULL) {
      printf("Memory allocation failed\n");
      exit(1);
    }
  }
  s->data[s->count++] = value;
}

int pop(Stack *s) {
  if (s->count == 0) {
    printf("Stack is empty\n");
    return -1; // Error value
  }
  int result = s->data[--s->count];
  // Optional: Shrink if count is less than half capacity (to avoid frequent realloc)
  if (s->count > 0 && s->count <= s->capacity / 2) {
    s->capacity = s->count; // Shrink to current count
    s->data = realloc(s->data, s->capacity * sizeof(int));
    if (s->data == NULL) {
      printf("Realloc failed during shrink\n");
      exit(1);
    }
  }
  return result;
}

int size(Stack *s) {
  return s->count;
}

int peek(Stack *s) {
  return s->data[s->count - 1];
}

int main() {
  Stack myStack;
  init(&myStack);
  push(&myStack, 1);
  push(&myStack, 2);
  printf("%d\n", peek(&myStack));
  printf("%d\n", pop(&myStack));
  printf("%d\n", peek(&myStack));
  // Free memory
  free(myStack.data);
  return 0;
}
