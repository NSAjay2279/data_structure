#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef enum
{
  TYPE_INT,
  TYPE_STRING
} DataType;

typedef union
{
  int i;
  char *s;
} DataValue;

typedef struct
{
  DataType type;
  DataValue value;
} Element;

typedef struct
{
  Element *data;
  int count;
  int capacity;
} Stack;

void init(Stack *s)
{
  s->data = NULL;
  s->count = 0;
  s->capacity = 0;
}

void push(Stack *s, DataType type, DataValue value)
{
  if (s->count == s->capacity)
  {
    s->capacity = s->capacity == 0 ? 1 : s->capacity * 2;
    s->data = (Element *)realloc(s->data, s->capacity * sizeof(Element)); // Cast to Element*
    if (s->data == NULL)
    {
      printf("Memory allocation failed\n");
      exit(1);
    }
  }
  s->data[s->count].type = type;
  if (type == TYPE_STRING)
  {
    s->data[s->count].value.s = strdup(value.s); // Duplicate string to avoid pointer issues
  }
  else
  {
    s->data[s->count].value = value;
  }
  s->count++;
}

Element pop(Stack *s)
{
  if (s->count == 0)
  {
    printf("Stack is empty\n");
    Element empty = {TYPE_INT, {0}}; // Return empty element
    return empty;
  }
  s->count--;
  Element result = s->data[s->count];
  // Optional: Shrink if count is less than half capacity
  if (s->count > 0 && s->count <= s->capacity / 2)
  {
    s->capacity = s->count;
    s->data = (Element *)realloc(s->data, s->capacity * sizeof(Element)); // Cast to Element*
    if (s->data == NULL)
    {
      printf("Realloc failed during shrink\n");
      exit(1);
    }
  }
  return result;
}

Element peek(Stack *s)
{
  return s->data[s->count - 1];
}

int size(Stack *s)
{
  return s->count;
}

void print_element(Element e)
{
  if (e.type == TYPE_INT)
  {
    printf("%d", e.value.i); // Fixed: e.value.i
  }
  else if (e.type == TYPE_STRING)
  {
    printf("%s", e.value.s); // Fixed: e.value.s
  }
}

int main()
{
  Stack myStack;
  init(&myStack);

  // Push int
  DataValue v1 = {.i = 1};
  push(&myStack, TYPE_INT, v1);

  // Push int
  DataValue v2 = {.i = 2};
  push(&myStack, TYPE_INT, v2);

  // Peek and print
  Element p = peek(&myStack);
  print_element(p);
  printf("\n");

  // Pop and print
  Element popped = pop(&myStack);
  print_element(popped);
  printf("\n");

  // Peek again
  p = peek(&myStack);
  print_element(p);
  printf("\n");

  // Push string
  DataValue v3 = {.s = (char *)"freeCodeCamp"}; // Cast to char* to fix C++ warning
  push(&myStack, TYPE_STRING, v3);

  // Print size
  printf("%d\n", size(&myStack));

  // Peek
  p = peek(&myStack);
  print_element(p);
  printf("\n");

  // Pop
  popped = pop(&myStack);
  print_element(popped);
  printf("\n");

  // Peek
  p = peek(&myStack);
  print_element(p);
  printf("\n");

  // Free memory
  for (int i = 0; i < myStack.count; i++)
  {
    if (myStack.data[i].type == TYPE_STRING)
    {
      free(myStack.data[i].value.s);
    }
  }
  free(myStack.data);
  return 0;
}
