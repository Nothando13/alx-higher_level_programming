#!/usr/bin/python3
a = 89
b = 10
<<<<<<< HEAD
print("a={:d} - b={:d}".format(a, b))
=======
a, b = b, a
print("={:d} - b={:d}".format(a, b))
>>>>>>> ffdd96fbd78609e11136213d5dad2e112d69e95e

vi 13-is_palindrome.c

#include "lists.h"

/**
 * reverse_listint - reverses a linked list
<<<<<<< HEAD
 * @head: pointer tp the first node in the list
 *
 * Return: pointer to the first node in the new list
 */
void reverse_listint(listint_t **head)
{
  listint_t *prev = NULL;
  listint_t *current = *head;
  listint_t *next;

  while (current)
    {
      next = current->next;
      current->next = prev;
      prev = current;
      current = next;
   }
  
 *head = prev;
=======
 * @head: pointer to the first node in the list
 *
 * Return: pointer to the first node in new list
 */
void reverse_listint(listint_t **head)
{
        listint_t *prev = NULL;
        listint_t *current = *head;
        listint_t *next = NULL;

      while (current)
        {
            next = current->next;
            current->next = prev;
            prev = current;
            current = next;
        }
      
      *head = prev;
>>>>>>> ffdd96fbd78609e11136213d5dad2e112d69e95e
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: double pointer to the linked list
 *
 * Return: 1 if it is, 0 if not
 */
<<<<<<< HEAD
int is_palindrome(listint_t **head)
{
  listint_t *slow = *head, *fast = *head, *temp = *head, *dup = NULL;

  if (*head == NULL || (*head)->next == NULL)
    return (1);

  while (1)
    {
      fast = fast->next->next;
      if (!fast)
    {
      dup = slow->next;
      break;
    }
      if (!fast->next)
    {
      dup = slow->next->next;
      break;
    }
      slow = slow->next;
    }

  reverse_listint(&dup);

  while (dup && temp)
    {
      if (temp->n == dup->n)
    {
      dup = dup->next;
      temp = temp->next;
    }
      else
    return (0);
    }

  if (!dup)
    return (1);

  return (0);
}

=======
int is palindrome(listint_t **head, *fast = *head, *temp = *head, *dup = NULL;
{        
        if (*head == NULL || (*head)->next == NULL
            return (1);

        while (1)
        {
            fast = fast->next->next;
            if (!fast)
        {
            dup = slow->next;
            break;
        }
            if (!fast->next)
        {
            dup = slow->next->next;
            break;
        }
            slow = slow->next;
        }
        reverse_listint(&dup);
        {
            if (temp->n == dup->n)
        {
            dup = dup->next;
            temp = temp->next;
        }
            else
          return (0);
          }

        if (!dup)
          return (1);

        return (0);
}
>>>>>>> ffdd96fbd78609e11136213d5dad2e112d69e95e
