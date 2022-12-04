#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
  * is_palindrome - checks if a singly linked list is a palindrome.
  * @head: single list
  * Return: 1 if it is a palin or 0 if not
  */

int is_palindrome(listint_t **head)
{
	int len = 0, num[4500], pal = 1, i = 0;
	listint_t *copyh = *head;

	if (!*head || !((*head)->next))
		return (1);

	for (i = 0; copyh; i++, copyh = copyh->next)
		num[i] = copyh->n;

	for (len = i, i = 0; i < len; i++)
	{
		if (num[i] != num[len - 1 - i])
		{
			pal = 0;
			break;
		}
	}

	return (pal);
}
