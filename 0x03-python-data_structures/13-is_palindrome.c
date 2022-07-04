#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * is_palindrome_util - determines if a linked-list is a palindrome
 * @left: left side of the evaluation
 * @right: right side of the evaluation
 *
 * Return: 1 (true) or 0 (false)
 */
int is_palindrome_util(listint_t **left, listint_t *right)
{
	int is_pal, is_pal1;

	if (right == NULL)
		return (1);
	is_pal = is_palindrome_util(left, right->next);
	if (is_pal == 0)
		return (0);
	is_pal1 = ((*left)->n == right->n);
	*left = (*left)->next;
	return (is_pal1);
}

/**
 * is_palindrome - checks if linked list is a palindrome
 * @head: pointer to the head node
 *
 * Return: 1 (Palindrome) or 0 (Not A Palindrome)
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL)
		return (0);
	else
		return (is_palindrome_util(head, *head));
}
