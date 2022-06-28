#include "lists.h"

/**
 * check_cycle - evaluates if a linked list contains a cycle
 * @list: linked-list to be evaluated
 *
 * Return: 1 (if there is a cycle) or 0 (No cycle)
 */
int check_cycle(listint_t *list)
{
	listint_t **temp, *curr;

	temp = &list;
	curr = list;

	if (*temp == NULL)
		return (0);

	while (curr != NULL)
	{
		curr = curr->next;
		if (curr == *temp)
			return (1);
	}
	return (0);
}
